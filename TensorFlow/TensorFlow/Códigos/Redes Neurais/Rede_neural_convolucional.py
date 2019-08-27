import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
import tensorflow as tf

#----------Importando a base de dados mnist do dataset do TensorFlow----------#
# Cada imagem está na forma de uma lista com 784 posições -> matriz (28x28)   #
#-----------------------------------------------------------------------------#
mnist = input_data.read_data_sets('mnist/', one_hot = False) # Cria uma pasta com as imagens

#-----------------------Dividindo em teste e treinamento----------------------#
X_treinamento = mnist.train.images
y_treinamento = mnist.train.labels
X_teste = mnist.test.images
y_teste = mnist.test.labels

#-----------------------Transformando em arrays numpy-------------------------#
y_treinamento = np.asarray(y_treinamento, dtype = np.int32)
y_teste = np.asarray(y_teste, dtype = np.int32)

#----------------------------Mostrando um dígito------------------------------#
%matplotlib inline
plt.imshow(X_treinamento[2].reshape((28,28)), cmap = 'gray')
plt.title('Classe: ' + str(y_treinamento[2]))

#--------Criando um estimador para trabalhar com redes convolucionais---------#
def cria_rede(features, labels, mode): #features = x_treinamento, labels = y_treinamento -> precisa ser esses nomes para o tensorflow entender, mode = modo de treinamento, teste, previsão.. e ele é implicito, ou seja, não precisa passar

    # Camada de entrada precisa receber uma matriz, então precisamos dar um reshape para transformar de vetor para matriz
    entrada = tf.reshape(features['X'], [-1, 28, 28, 1]) # as imagens, batch_size(-1 = none), largura, altura, canais(RGB)

    #------------------------1ª camada de convolução--------------------------#
    # recebe [batch_size, 28, 28, 1]
    # retorna [batch_size, 28, 28, 32] # 32 filtros (quantidade de kernels) -> 32 imagens com 28x28
    convolucao1 = tf.layers.conv2d(inputs = entrada, filters = 32, kernel_size=[5,5], activation = tf.nn.relu, padding = 'same')

    #--------------------------1ª camada de Pooling---------------------------#
    # recebe [batch_size, 28, 28, 32]
    # retorna [batch_size, 14, 14, 32]
    pooling1 = tf.layers.max_pooling2d(inputs = convolucao1, pool_size = [2,2], strides = 2)

    #------------------------2ª camada de convolução--------------------------#
    # recebe [batch_size, 14, 14, 32]
    # retorna [batch_size, 14, 14, 64]
    convolucao2 = tf.layers.conv2d(inputs = pooling1, filters = 64, kernel_size = [5,5], activation = tf.nn.relu, padding = 'same')

    #--------------------------1ª camada de Pooling---------------------------#
    # recebe [batch_size, 14, 14, 64]
    # retorna [batch_size, 7, 7, 64]
    pooling2 = tf.layers.max_pooling2d(inputs = convolucao2, pool_size = [2,2], strides = 2)

    #------------------------Efetuando o flattening---------------------------#
    # recebe [batch_size, 7, 7, 64]
    # retornar [batch_size, 3136]
    flattening = tf.reshape(pooling2, [-1, 7 * 7 * 64])

    #-------------------------Criando a rede neural---------------------------#
    # 3136 (entradas) -> 1024 (oculta) -> 10 (saída)

    #------------------------Criando camada escondida-------------------------#
    # recebe [batch_size, 3136]
    # retornar [batch_size, 1024]
    densa = tf.layers.dense(inputs = flattening, units = 1024, activation = tf.nn.relu)

    #--------Zerando algumas das entradas para aliviar o processamento--------#
    # dropout 20%
    # só executa quando está fazendo o treinamento
    dropout = tf.layers.dropout(inputs = densa, rate = 0.2, training=mode == tf.estimator.ModeKeys.TRAIN)

    #----------------------------Camada de saída------------------------------#
    # recebe [batch_size, 1024]
    # retornar [batch_size, 10]
    saida = tf.layers.dense(inputs = dropout, units = 10)

    #-----------Convertendo as probabilidades para valores inteiros-----------#
    # 0.2 0.2 0.6 - 2
    previsoes = tf.argmax(saida, axis = 1)

    #-----------------------------Faz previsões-------------------------------#
    if mode == tf.estimator.ModeKeys.PREDICT:
        return tf.estimator.EstimatorSpec(mode = mode, predictions = previsoes)

    #--------------------------Verificando o erro-----------------------------#
    # para quando não temos o one_hot
    # só executa quando queremos treinar ou avaliar
    erro = tf.losses.sparse_softmax_cross_entropy(labels = labels, logits = saida)

    #---------------------------Faz o treinamento-----------------------------#
    if mode == tf.estimator.ModeKeys.TRAIN:
        otimizador = tf.train.AdamOptimizer(learning_rate = 0.001)
        treinamento = otimizador.minimize(erro, global_step = tf.train.get_global_step())
        return tf.estimator.EstimatorSpec(mode = mode, loss = erro, train_op = treinamento)

    #----------------------------Faz a avaliação------------------------------#
    if mode == tf.estimator.ModeKeys.EVAL:
        eval_metrics_ops = {'accuracy': tf.metrics.accuracy(labels = labels, predictions = previsoes)}
        return tf.estimator.EstimatorSpec(mode = mode, loss = erro, eval_metric_ops = eval_metrics_ops)

#-------------------------Criando o classificador-----------------------------#
classificador = tf.estimator.Estimator(model_fn = cria_rede)

#----------------------Criando bloco de treinamento---------------------------#
funcao_treinamento = tf.estimator.inputs.numpy_input_fn(x = {'X': X_treinamento}, y = y_treinamento, batch_size = 128, num_epochs = None, shuffle = True)

#---------------------------Executando o treinamento--------------------------#
classificador.train(input_fn=funcao_treinamento, steps = 200)

#---------------------Criando bloco para efetuar o teste----------------------#
funcao_teste = tf.estimator.inputs.numpy_input_fn(x = {'X': X_teste}, y = y_teste, num_epochs = 1, shuffle = False)

#-----------------------------Avaliando modelo--------------------------------#
resultados = classificador.evaluate(input_fn=funcao_teste)
resultados

#---------------------------Prevendo o X_teste[1]-----------------------------#
X_imagem_teste = X_teste[1]

X_imagem_teste = X_imagem_teste.reshape(1,-1)

funcao_previsao = tf.estimator.inputs.numpy_input_fn(x = {'X': X_imagem_teste}, shuffle = False)
pred = list(classificador.predict(input_fn = funcao_previsao))

pred[0]

plt.imshow(X_imagem_teste.reshape((28, 28)), cmap = 'gray')
plt.title('Classe prevista: ' + str(pred[0]))
