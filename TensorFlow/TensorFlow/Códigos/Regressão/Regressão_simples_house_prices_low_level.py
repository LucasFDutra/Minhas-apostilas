import tensorflow as tf
#----------------Coloca a base de dados na variável 'base'--------------------#
import pandas as pd
base = pd.read_csv('house_prices.csv')
base.head()

#----------Alocando os valores das colunas em previsores e classes------------#
X = base.iloc[:, 5:6].values
y = base.iloc[:, 2:3].values

#--------------------------Escalonando os valores-----------------------------#
from sklearn.preprocessing import StandardScaler
scaler_x = StandardScaler()
scaler_y = StandardScaler()
x = scaler_x.fit_transform(x)
y = scaler_y.fit_transform(y)

#-------------------Exibindo a distribuição dos registros---------------------#
import matplotlib.pyplot as plt
%matplotlib inline
plt.scatter(x, y)

#----------Definindo os valores iniciais para a equação de regressão----------#
np.random.seed(1) #esse seed(valor) força a sempre sair o mesmo valor
b_0, b_1 = np.random.rand(2) #cria um vetor de duas posições com números aleatórios
b0 = tf.Variable(b_0, name = 'b0')
b1 = tf.Variable(b_1, name = 'b1')

#------------Passando o Banco de dados para um placeholder--------------------#
# Para o processo de treinamento não demorar muito, é recomendado passar as   #
# amostras pouco a pouco, o batch_size define quantas amostras serão passadas #
# por vez.                                                                    #
#-----------------------------------------------------------------------------#
batch_size = 32
xph = tf.placeholder(tf.float32, [batch_size, 1])
yph = tf.placeholder(tf.float32, [batch_size, 1])

#-------------------------Criando os blocos do grafo--------------------------#

#-------------------------------Bloco de erro---------------------------------#
y_modelo = b0 + b1*xph # definindo equação da reta
erro = tf.losses.mean_squared_error(yph, y_modelo) # y resposta real, a formula é o previsto.

#------------------------Bloco de otimização do erro--------------------------#
otimizador = tf.train.GradientDescentOptimizer(learning_rate = 0.001)

#-----------------------------Bloco do regressor------------------------------#
regressor = otimizador.minimize(erro) # procura minimizar o erro.

#---------------------------Iniciando as variáveis----------------------------#
init = tf.global_variables_initializer()

#------------------Efetuando as operações dentro da seção---------------------#
with tf.Session() as sess:
    sess.run(init) # inicializa as variáveis
    for i in range(10000): # efetua 10000 épocas de treinamento
        indices = np.random.randint(len(x), size = batch_size) # pega 32 indices dentre os atributos.
        feed = {xph: x[indices], yph: y[indices]} # aloca nos placeholders os valores sorteados.
        sess.run(regressor, feed_dict = feed)
    b0_final, b1_final = sess.run([b0, b1]) # retorna os valores finais de b_0 e b_1
print('valor final de b0: {} \nvalor final de b1: {}'.format(b0_final, b1_final))

#----Efetuando uma previsão utilizando os proprios valores da base de dados---#
previsoes = b0_final + b1_final * x
print(previsoes)

#---Exibindo a distribuição real dos registros e a reta de regressão linear---#
plt.plot(x, previsoes, color = 'red')
plt.plot(x, y, 'o')

#----------------Calculando o erro absoluto e o quadrático--------------------#
# para isso é primeiramente necessário inverter o escalonamento das previsoes #
# e de y.                                                                     #
#-----------------------------------------------------------------------------#
y1 = scaler_y.inverse_transform(y)
previsoes1 = scaler_y.inverse_transform(previsoes)

from sklearn.metrics import mean_absolute_error, mean_squared_error
erro_absoluto = mean_absolute_error(y1, previsoes1)
erro_quadratico = mean_squared_error(y1, previsoes1)
print(f'O erro absoluto foi: {erro_absoluto} \nOcerro quadrático foi: {erro_quadratico}')
