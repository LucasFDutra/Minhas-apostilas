from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#----------Importando a base de dados mnist do dataset do TensorFlow----------#
# já cria as variáveis dummy                                                  #
# Cada imagem está na forma de uma lista com 784 posições -> matriz (28x28)   #
#-----------------------------------------------------------------------------#
mnist = input_data.read_data_sets('mnist/', one_hot = True) # Cria uma pasta com as imagens

#-----------------------Dividindo em teste e treinamento----------------------#
X_treinamento = mnist.train.images
y_treinamento = mnist.train.labels
X_teste = mnist.test.images
y_teste = mnist.test.labels

#----------------------------Mostrando um dígito------------------------------#
%matplotlib inline
plt.imshow(X_treinamento[102].reshape((28,28)), cmap = 'gray')
plt.title('Classe: ' + str(np.argmax(y_treinamento[102])))

#----------------------------Dividindo os batchs------------------------------#
X_batch, y_batch = mnist.train.next_batch(128) # cada batch tem 128 elementos

#-----------------------Criando os neurônios de entrada-----------------------#
neuronios_entrada = X_treinamento.shape[1] # 784 neurônios de entrada

#------------------Criando os neurônios da 1ª camada oculta-------------------#
neuronios_oculta1 = int((X_treinamento.shape[1] + y_treinamento.shape[1]) / 2) # 397 neurônios

#------------------Criando os neurônios da 2ª camada oculta-------------------#
neuronios_oculta2 = neuronios_oculta1 # 397 neurônios

#------------------Criando os neurônios da 3ª camada oculta-------------------#
neuronios_oculta3 = neuronios_oculta1 # 397 neurônios

#-------------------Criando os neurônios de camada de saída-------------------#
neuronios_saida = y_treinamento.shape[1] # 10 neurônios
neuronios_saida

#-----------------------Definindo os pesos iniciais---------------------------#
W = {'oculta1': tf.Variable(tf.random_normal([neuronios_entrada, neuronios_oculta1])),
     'oculta2': tf.Variable(tf.random_normal([neuronios_oculta1, neuronios_oculta2])),
     'oculta3': tf.Variable(tf.random_normal([neuronios_oculta2, neuronios_oculta3])),
     'saida': tf.Variable(tf.random_normal([neuronios_oculta3, neuronios_saida]))
}

#------------------------------Criando os bias--------------------------------#
b = {'oculta1': tf.Variable(tf.random_normal([neuronios_oculta1])),
     'oculta2': tf.Variable(tf.random_normal([neuronios_oculta2])),
     'oculta3': tf.Variable(tf.random_normal([neuronios_oculta3])),
     'saida': tf.Variable(tf.random_normal([neuronios_saida]))
}

#-------Criando placeholder para receber os dados que vão aos neurônios-------#
xph = tf.placeholder('float', [None, neuronios_entrada])
yph = tf.placeholder('float', [None, neuronios_saida])

#---------------------------Criando os blocos do grafo------------------------#
def mlp(x, W, bias):
    camada_oculta1 = tf.nn.relu(tf.add(tf.matmul(x, W['oculta1']), bias['oculta1']))
    camada_oculta2 = tf.nn.relu(tf.add(tf.matmul(camada_oculta1, W['oculta2']), bias['oculta2']))
    camada_oculta3 = tf.nn.relu(tf.add(tf.matmul(camada_oculta2, W['oculta3']), bias['oculta3']))
    camada_saida = tf.add(tf.matmul(camada_oculta3, W['saida']), bias['saida'])
    return camada_saida

modelo = mlp(xph, W, b)

#----------------------Criando bloco que calcula o erro-----------------------#
erro = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits = modelo, labels = yph))
otimizador = tf.train.AdamOptimizer(learning_rate = 0.0001).minimize(erro)

#------------------------Criando bloco dos previsores-------------------------#
previsoes = tf.nn.softmax(modelo)
previsoes_corretas = tf.equal(tf.argmax(previsoes, 1), tf.argmax(yph, 1)) #compara com as respostas corretas

#---------------------Criando bloco para calcular acertos---------------------#
taxa_acerto = tf.reduce_mean(tf.cast(previsoes_corretas, tf.float32))

#---------------------------Executando o treinamento--------------------------#
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoca in range(5000):
        X_batch, y_batch = mnist.train.next_batch(128)
        _, custo = sess.run([otimizador, erro], feed_dict = {xph: X_batch, yph: y_batch})
        if epoca % 100 == 0:
            acc = sess.run([taxa_acerto], feed_dict = {xph: X_batch, yph: y_batch})
            print('época: ' + str((epoca + 1)) + ' erro: ' + str(custo) + ' acc: ' + str(acc))

    print('Treinamento concluído')
    print(sess.run(taxa_acerto, feed_dict = {xph: X_teste, yph: y_teste}))
