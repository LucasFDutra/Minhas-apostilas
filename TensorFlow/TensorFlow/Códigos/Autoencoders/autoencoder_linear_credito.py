import pandas as pd
import tensorflow as tf

#------------------------TRABALHANDO COM OS DADOS-----------------------------#
#                                                                             #
#----------------Coloca a base de dados na variável 'base'--------------------#
base = pd.read_csv('credit_data.csv')
base = base.drop('i#clientid', axis = 1)
base = base.dropna()

#--------------------------Escalonando as variáveis---------------------------#
from sklearn.preprocessing import StandardScaler
scaler_x = StandardScaler()
base[['income', 'age', 'loan']] = scaler_x.fit_transform(base[['income', 'age', 'loan']])
X = base.drop('c#default', axis = 1)
y = base['c#default']

#--------------------------CRIANDO O AUTOENCODER------------------------------#
#                                                                             #
#---------------Define a quantidade de neurônios em cada camada---------------#
# 3 -> 2 -> 3
neuronios_entrada = 3
neuronios_oculta = 2
neuronios_saida = neuronios_entrada

#---------------------------Criando placeholder-------------------------------#
xph = tf.placeholder(tf.float32, shape = [None, neuronios_entrada])

#---------------------------Criando as camadas--------------------------------#
# fully_connected: conecta todos os neurônios de uma camada com os da proxima #
#-----------------------------------------------------------------------------#
from tensorflow.contrib.layers import fully_connected
camada_oculta = fully_connected(inputs = xph, num_outputs = neuronios_oculta, activation_fn = None)
camada_saida = fully_connected(inputs = camada_oculta, num_outputs = neuronios_saida)

#---------------Cria os blocos de treinamento do autoencoder------------------#
erro = tf.losses.mean_squared_error(labels = xph, predictions = camada_saida)
otimizador = tf.train.AdamOptimizer(0.01)
treinamento = otimizador.minimize(erro)

#-----------------------------Efetua o treinamento----------------------------#
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoca in range(1000):
        custo, _ = sess.run([erro, treinamento], feed_dict = {xph: X})
        if epoca % 100 == 0:
            print('erro: ' + str(custo))
    X2d_encode = sess.run(camada_oculta, feed_dict = {xph: X}) #Vai ter os valores que estão na camada oculta
    X3d_decode = sess.run(camada_saida, feed_dict = {xph: X}) #Vai ter os valores que estão na camada de saída

#-------------------------Verificando o modelo--------------------------------#
X2 = scaler_x.inverse_transform(X)
X3d_decode2 = scaler_x.inverse_transform(X3d_decode)

from sklearn.metrics import mean_absolute_error
mae_income = mean_absolute_error(X2[:,0], X3d_decode2[:,0])
mae_age = mean_absolute_error(X2[:,1], X3d_decode2[:,1])
mae_loan = mean_absolute_error(X2[:,2], X3d_decode2[:,2])

#----CRIANDO E TRABALHANDO COM A REDE NEURAL PARA EFETUAR A CLASSIFICAÇÃO-----#
#                                                                             #
#-------------------------Base de dados codificada----------------------------#
X_encode = pd.DataFrame({'atributo1': X2d_encode[:,0], 'atributo2': X2d_encode[:,1], 'classe': y})

import tensorflow as tf
colunas = [tf.feature_column.numeric_column(key = column) for column in X_encode.columns]

#-------------------Divide em base de dados e treinamento---------------------#
from sklearn.model_selection import train_test_split
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X_encode, y, test_size = 0.3, random_state = 0)
funcao_treinamento = tf.estimator.inputs.pandas_input_fn(x = X_treinamento, y = y_treinamento, batch_size = 8, num_epochs = None, shuffle = True)

#--------------------------Criando o classificador----------------------------#
classificador = tf.estimator.DNNClassifier(feature_columns = colunas, hidden_units = [4, 4])
classificador.train(input_fn = funcao_treinamento, steps = 1000)

#------------------Criando bloco de teste para avaliação----------------------#
funcao_teste = tf.estimator.inputs.pandas_input_fn(x = X_teste, y = y_teste, batch_size = 8, num_epochs = 1000, shuffle = False)

#----------------------------Avaliando o modelo-------------------------------#
metricas_teste = classificador.evaluate(input_fn = funcao_teste, steps = 1000)
metricas_teste
