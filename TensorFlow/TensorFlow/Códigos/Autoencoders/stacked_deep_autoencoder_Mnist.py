from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

#-------------------------Reseta grafos existentes----------------------------#
tf.reset_default_graph()

#------------------------Importando a base de dados---------------------------#
mnist = input_data.read_data_sets('mnist/', one_hot = True)
X = mnist.train.images

#-----------------Definindo número de neurônios por camada--------------------#
# encoder
neuronios_entrada = 784
neuronios_oculta1 = 128

# dado/imagem codificada
neuronios_oculta2 = 64

# decoder
neuronios_oculta3 = neuronios_oculta1
neuronios_saida = neuronios_entrada

#---------------------------Criando placeholder-------------------------------#
xph = tf.placeholder(tf.float32, [None, neuronios_entrada])

#--------------------------Inicializa os pessos-------------------------------#
# Estruturas para inicialização dos pesos:                                    #
# Xavier => He (no tensorflow) ele inicializa os pesos de forma escalonada    #
# Xavier: Se adapta melhor a função sigmoid                                   #
# He: se adapta melhor a função relu                                          #
#-----------------------------------------------------------------------------#
inicializador = tf.variance_scaling_initializer()

#-------------------------Definindo os pesos iniciais-------------------------#
W = {'encoder_oculta1': tf.Variable(inicializador([neuronios_entrada, neuronios_oculta1])),
     'encoder_oculta2': tf.Variable(inicializador([neuronios_oculta1, neuronios_oculta2])),
     'decoder_oculta3': tf.Variable(inicializador([neuronios_oculta2, neuronios_oculta3])),
     'decoder_saida': tf.Variable(inicializador([neuronios_oculta3, neuronios_saida]))
}

#-------------------------Definindo os bias iniciais--------------------------#
b = {'encoder_oculta1': tf.Variable(inicializador([neuronios_oculta1])),
     'encoder_oculta2': tf.Variable(inicializador([neuronios_oculta2])),
     'decoder_oculta3': tf.Variable(inicializador([neuronios_oculta3])),
     'decoder_saida': tf.Variable(inicializador([neuronios_saida]))
}

#-----------------------------Criando as camadas------------------------------#
camada_oculta1 = tf.nn.relu(tf.add(tf.matmul(xph, W['encoder_oculta1']), b['encoder_oculta1']))
camada_oculta2 = tf.nn.relu(tf.add(tf.matmul(camada_oculta1, W['encoder_oculta2']), b['encoder_oculta2']))
camada_oculta3 = tf.nn.relu(tf.add(tf.matmul(camada_oculta2, W['decoder_oculta3']), b['decoder_oculta3']))
camada_saida = tf.nn.relu(tf.add(tf.matmul(camada_oculta3, W['decoder_saida']), b['decoder_saida']))

#-----------------------Criando os blocos de treinamento----------------------#
erro = tf.losses.mean_squared_error(xph, camada_saida)
otimizador = tf.train.AdamOptimizer(learning_rate = 0.001)
treinamento = otimizador.minimize(erro)
batch_size = 128

#--------------------------Efetuando o treinamento----------------------------#
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoca in range(50):
        numero_batches = mnist.train.num_examples // batch_size
        for i in range(numero_batches):
            X_batch, _ = mnist.train.next_batch(batch_size)
            custo, _ = sess.run([erro, treinamento], feed_dict = {xph: X_batch})
        print('época: ' + str(epoca + 1) + ' erro: ' + str(custo))

    imagens_codificadas = sess.run(camada_oculta2, feed_dict = {xph: X}) #Pegando as imagens codificadas
    imagens_decodificadas = sess.run(camada_saida, feed_dict = {xph: X}) #Pegando as imagens decodificadas

#--------------------Exibindo 5 imagens para comparar-------------------------#
import numpy as np
numero_imagens = 5
imagens_teste = np.random.randint(X.shape[0], size = numero_imagens)
imagens_teste

plt.figure(figsize = (18, 18))
for i, indice_imagem in enumerate(imagens_teste):
    #Imagens originais
    eixo = plt.subplot(10, 5, i + 1)
    plt.imshow(X[indice_imagem].reshape(28, 28))
    plt.xticks(())
    plt.yticks(())
    #Imagens codificadas
    eixo = plt.subplot(10, 5, i + 1 + numero_imagens)
    plt.imshow(imagens_codificadas[indice_imagem].reshape(8, 8))
    plt.xticks(())
    plt.yticks(())
    #Imagens Decodificadas
    eixo = plt.subplot(10, 5, i + 1 + numero_imagens * 2)
    plt.imshow(imagens_decodificadas[indice_imagem].reshape(28, 28))
    plt.xticks(())
    plt.yticks(())
