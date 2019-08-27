import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd

#----------------Alocando a base de dados à variavel 'base'-------------------#
# A base de dados em questão são os preços das ações da petrobas              #
#-----------------------------------------------------------------------------#
base = pd.read_csv('petr4.csv')

#-------------------------Apagando registros com nan--------------------------#
base = base.dropna()

#--------------------Pegando apenas os valores de abertura--------------------#
# Vamos prever o valor de abertura futura com base nas aberturas passadas     #
#-----------------------------------------------------------------------------#
base = base.iloc[:,1].values
#%matplotlib inline
plt.plot(base)

#------Iremos prever os 30 valores a frente utilizando os 30 anteriores-------#
periodos = 30
previsao_futura = 1 # Vamos pegar apenas 1 periodo (30 dias)

#---------------------------------Previsores----------------------------------#
X = base[0:(len(base) - (len(base) % periodos))]
X_batches = X.reshape(-1, periodos, 1)

#-----------------------------------Classe------------------------------------#
y = base[1:(len(base) - (len(base) % periodos)) + previsao_futura]
y_batches = y.reshape(-1, periodos, 1)

#--------------------------------Base de testes-------------------------------#
X_teste = base[-(periodos + previsao_futura):]
X_teste = X_teste[:periodos] #fica apenas com 30 registros
X_teste = X_teste.reshape(-1, periodos, 1)
y_teste = base[-(periodos):]
y_teste = y_teste.reshape(-1, periodos, 1)

#-------------------Resetando possíveis grafos já existentes------------------#
tf.reset_default_graph()

#----------------------Definindo quantidades de neurônios---------------------#
entradas = 1
neuronios_oculta = 100
neuronios_saida = 1 # é um problema de regressão, logo deve-se ter somente uma saída

#Criando placeholder
xph = tf.placeholder(tf.float32, [None, periodos, entradas])
yph = tf.placeholder(tf.float32, [None, periodos, neuronios_saida])

#---------------------Criando uma célula de memória LSTM----------------------#
# Cada celula irá se transformar em uma camada oculta                         #
#-----------------------------------------------------------------------------#
def cria_uma_celula():
    return tf.contrib.rnn.LSTMCell(num_units = neuronios_oculta, activation = tf.nn.relu)

#-----------------------Cria varias celulas de memória------------------------#
# Para criar varias celulas é utilizada a função cria_uma_celula em um for    #
#-----------------------------------------------------------------------------#
def cria_varias_celulas():
    celulas =  tf.nn.rnn_cell.MultiRNNCell([cria_uma_celula() for i in range(4)])
    return celulas

#------------------------Cria celulas na camada oculta------------------------#
celula = cria_varias_celulas()

#-----------------------Cria celulas na camada de saída-----------------------#
celula = tf.contrib.rnn.OutputProjectionWrapper(celula, output_size = 1)

#-----------------------------Bloco de treinamento----------------------------#
saida_rnn, _ = tf.nn.dynamic_rnn(celula, xph, dtype = tf.float32)
erro = tf.losses.mean_squared_error(labels = yph, predictions = saida_rnn)
otimizador = tf.train.AdamOptimizer(learning_rate = 0.001)
treinamento = otimizador.minimize(erro)

#---------------------------Efetuando o treinamento---------------------------#
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for epoca in range(1000):
        _, custo = sess.run([treinamento, erro], feed_dict = {xph: X_batches, yph: y_batches})
        if epoca % 100 == 0:
            print(epoca + 1, ' erro: ', custo)

    previsoes = sess.run(saida_rnn, feed_dict = {xph: X_teste}) #efetua a previsão

#----------------------------Verificar a precisão-----------------------------#
import numpy as np
y_teste.shape
y_teste2 = np.ravel(y_teste)

previsoes2 = np.ravel(previsoes)

from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_teste2, previsoes2)

#--------------------mostrando os valores reais e previstos-------------------#
plt.plot(y_teste2, label = 'Valor real')
plt.plot(previsoes2, label = 'Previsões')
plt.legend()
