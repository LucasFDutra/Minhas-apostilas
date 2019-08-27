import tensorflow as tf
import numpy as np

#--------------------------Criando os previsores------------------------------#
X = np.array([[0.0, 0.0],
              [0.0, 1.0],
              [1.0, 0.0],
              [1.0, 1.0]])

#----------------------------Criando a classe---------------------------------#
y = np.array([[0.0], [1.0], [1.0], [1.0]])

#-----------------------Definindo os pesos iniciais---------------------------#
W = tf.Variable(tf.zeros([2, 1], dtype = tf.float64))

#-----------------------Criando a função de ativação--------------------------#
def step(x):
    return tf.cast(tf.to_float(tf.math.greater_equal(x, 1)), tf.float64)

#---------------------------Inicializando a variável--------------------------#
init = tf.global_variables_initializer()

#---------------------------Criando os blocos do grafo------------------------#
#                                                                             #
#--------------------Bloco de produto da matriz X pelos pesos-----------------#
camada_saida = tf.matmul(X, W)

#--------------------------Bloco da função de ativação------------------------#
camada_saida_ativacao = step(camada_saida)

#---------------------------Bloco de calculo do erro--------------------------#
erro = tf.subtract(y, camada_saida_ativacao)

#---------------------------Bloco do calculo do delta-------------------------#
delta = tf.matmul(X, erro, transpose_a = True)
treinamento = tf.assign(W, tf.add(W, tf.multiply(delta, 0.1)))

#---------------------------Executando o treinamento--------------------------#
with tf.Session() as sess:
    sess.run(init)
    epoca = 0
    for i in range(15):
        epoca += 1
        erro_total, _ = sess.run([erro, treinamento]) #erro de cada amostra
        erro_soma = tf.reduce_sum(erro_total) # soma os erros do vator anterior
        print('Época:', epoca, ' Erro: ', sess.run(erro_soma)) # vendo erro por época
        if erro_soma.eval() == 0.0: # se não houver erro o código para
            break
    W_final = sess.run(W) # garda o valor final dos pesos

#-------------------------------------Teste-----------------------------------#
camada_saida_teste = tf.matmul(X, W_final)
camada_saida_ativacao_teste = step(camada_saida_teste)
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(camada_saida_ativacao_teste))
