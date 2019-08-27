import tensorflow as tf
import numpy as np

#--------------------------Criando os previsores------------------------------#
X = np.array([[0,0], [0,1], [1,0], [1,1]])

#----------------------------Criando a classe---------------------------------#
y = np.array([[1], [0], [0], [1]])

#-----------------Definindo numero de neurônios por camada--------------------#
neuronios_entrada = 2
neuronios_oculta = 3
neuronios_saida = 1

#-----------------------Definindo os pesos iniciais---------------------------#
W = {'oculta': tf.Variable(tf.random_normal([neuronios_entrada, neuronios_oculta]), name = 'w_oculta'),
     'saida': tf.Variable(tf.random_normal([neuronios_oculta, neuronios_saida]), name = 'w_saida')}

#------------------------------Criando os bias--------------------------------#
b = {'oculta': tf.Variable(tf.random_normal([neuronios_oculta]), name = 'b_oculta'),
     'saida': tf.Variable(tf.random_normal([neuronios_saida]), name = 'b_saida')}


#------Criando place holder para receber os dados que vão aos neurônios-------#
xph = tf.placeholder(tf.float32, [4, neuronios_entrada], name = 'xph')
yph = tf.placeholder(tf.float32, [4, neuronios_saida], name = 'yph')

#---------------------------Criando os blocos do grafo------------------------#
#                                                                             #
#--------Criando bloco da multiplicação entre entrada e camada oculta---------#
camada_oculta = tf.add(tf.matmul(xph, W['oculta']), b['oculta'])
camada_oculta_ativacao = tf.sigmoid(camada_oculta)

#----------Criando bloco da multiplicação entre camada oculta e saída---------#
camada_saida = tf.add(tf.matmul(camada_oculta_ativacao, W['saida']), b['saida'])
camada_saida_ativacao = tf.sigmoid(camada_saida)

#----------------------Criando bloco que calcula o erro-----------------------#
erro = tf.losses.mean_squared_error(yph, camada_saida_ativacao)
otimizador = tf.train.GradientDescentOptimizer(learning_rate = 0.3).minimize(erro)

#---------------------------Inicializando a variável--------------------------#
init = tf.global_variables_initializer()

#---------------------------Executando o treinamento--------------------------#
with tf.Session() as sess:
    sess.run(init)
    for epocas in range(10000):
        erro_medio = 0
        _, custo = sess.run([otimizador, erro], feed_dict = {xph: X, yph: y})
        if epocas % 200 == 0:
            erro_medio += custo / 4
            print(erro_medio)
    W_final, b_final = sess.run([W, b]) # pegando os valores dos pesos e bias finais

#-------------------------------------Teste-----------------------------------#
camada_oculta_teste = tf.add(tf.matmul(xph, W_final['oculta']), b_final['oculta'])
camada_oculta_ativacao_teste = tf.sigmoid(camada_oculta_teste)
camada_saida_teste = tf.add(tf.matmul(camada_oculta_ativacao_teste, W_final['saida']), b_final['saida'])
camada_saida_ativacao_teste = tf.sigmoid(camada_saida_teste)

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(camada_saida_ativacao_teste, feed_dict = {xph: X}))
