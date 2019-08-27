import tensorflow as tf

#----------------Coloca a base de dados na variável 'base'--------------------#
import pandas as pd
base = pd.read_csv('house_prices.csv')

#-----------------Escolhendo os atributos que utilizaremos--------------------#
colunas_usadas = ['price', 'bedrooms', 'bathrooms', 'sqft_living',
       'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
       'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
       'lat', 'long']

#------------------Mantendo apenas as colunas desejadas-----------------------#
base = pd.read_csv('house_prices.csv', usecols = colunas_usadas)

#--------------------------Escalonando os valores-----------------------------#
# Escalonando em normalização                                                 #
# Vamos utilizar o pandas para manipular os dados, por isso não temos o       #
# comando '.values' que transforma o dataframe em arry numpy.                 #
#-----------------------------------------------------------------------------#
from sklearn.preprocessing import MinMaxScaler
scaler_x = MinMaxScaler()
scaler_y = MinMaxScaler()
base.iloc[:,1:17] = scaler_x.fit_transform(base.iloc[:,1:17])
base.iloc[:,0:1] = scaler_y.fit_transform(base.iloc[:,0:1])

#----------Alocando os valores das colunas em previsores e classes------------#
# O y precisa ter somente um elemento para indicar coluna, assim o tipo dele  #
# fica sendo Series e tudo funciona.                                          #
#                                                                             #
# Esse processo de divisão da base deve ser feito depois de escalonar, pois   #
# não é possível escalonar Series                                             #
#-----------------------------------------------------------------------------#
x = base.iloc[:,1:17]
y = base.iloc[:,0] #não pode ter a coluna, só as linhas.

#-------------Dividindo a base de dados entre treinamento e teste-------------#
from sklearn.model_selection import train_test_split
x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(x, y, test_size = 0.3)

#---------Criando varias colunas com a key trocando automaticamente-----------#
colunas = [tf.feature_column.numeric_column(key = c) for c in colunas_usadas[1:17]]

#-------------------------------Criando o grafo-------------------------------#
#                                                                             #
#--------------Bloco para efetuar o treinamento e a avaliação-----------------#
funcao_treinamento = tf.estimator.inputs.pandas_input_fn(x_treinamento, y_treinamento,
                                                        batch_size = 32, num_epochs = None, shuffle = True)

#-----------Criando bloco para efetuar a avaliação da base de teste-----------#
funcao_teste = tf.estimator.inputs.pandas_input_fn(x = x_teste, y = y_teste,
                                                   batch_size = 32, num_epochs = 10000, shuffle = False)

#----------------------------Cria o regressor---------------------------------#
regressor = tf.estimator.LinearRegressor(feature_columns=colunas)

#----------------------------Efetua o treinamento-----------------------------#
regressor.train(input_fn=funcao_treinamento, steps = 10000)

#---------------------------Verificando as metricas---------------------------#
# average_loss baixo significa que o algoritmo se adaptou bem ao problema     #
#-----------------------------------------------------------------------------#
metricas_treinamento = regressor.evaluate(input_fn=funcao_treinamento, steps = 10000)
metricas_teste = regressor.evaluate(input_fn=funcao_teste, steps = 10000)
print(f'metricas de treinamento: {metricas_treinamento}')
print(f'metricas de teste: {metricas_teste}')

#-----------Criando bloco para efetuar a previsão da base de teste------------#
funcao_previsao = tf.estimator.inputs.pandas_input_fn(x = x_teste, shuffle = False)

#----------------------------Efetuando previsões------------------------------#
previsoes = list(regressor.predict(input_fn=funcao_previsao))
valores_previsoes = []
for p in previsoes:
    valores_previsoes.append(p['predictions'])

#----------------Calculando o erro absoluto e o quadrático--------------------#
# Primeiro precisamos inverter o escalonamento, porém a y está no formato de  #
# series que é da forma (dimensão,), então precisamos efetuar um reshape nela #
#-----------------------------------------------------------------------------#
valores_previsoes = scaler_y.inverse_transform(valores_previsoes)
y_teste = scaler_y.inverse_transform(y_teste.values.reshape(-1,1))

from sklearn.metrics import mean_absolute_error, mean_squared_error
erro_absoluto = mean_absolute_error(y_teste, valores_previsoes)
erro_quadratico = mean_squared_error(y_teste, valores_previsoes)
print(f'O erro absoluto foi: {erro_absoluto} \nO erro quadrático foi: {erro_quadratico}')
