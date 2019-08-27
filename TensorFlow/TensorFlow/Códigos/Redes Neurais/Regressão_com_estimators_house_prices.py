import pandas as pd
import tensorflow as tf
from sklearn.metrics import mean_absolute_error

#----------------Coloca a base de dados na variável 'base'--------------------#
base = pd.read_csv('house_prices.csv')

#-----------------Escolhendo os atributos que utilizaremos--------------------#
colunas_usadas = ['price', 'bedrooms', 'bathrooms', 'sqft_living',
       'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
       'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
       'lat', 'long']

#------------------Mantendo apenas as colunas desejadas-----------------------#
base = pd.read_csv('house_prices.csv', usecols = colunas_usadas)

#--------------------------Escalonando os valores-----------------------------#
from sklearn.preprocessing import MinMaxScaler
scaler_x = MinMaxScaler()
base[['bedrooms', 'bathrooms', 'sqft_living',
       'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
       'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
       'lat', 'long']] = scaler_x.fit_transform(base[['bedrooms', 'bathrooms', 'sqft_living',
       'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
       'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
       'lat', 'long']])

scaler_y = MinMaxScaler()
base[['price']] = scaler_y.fit_transform(base[['price']])

#----------Alocando os valores das colunas em previsores e classes------------#
X = base.drop('price', axis = 1)
y = base.price

#---------Criando varias colunas com a key trocando automaticamente-----------#
colunas = [tf.feature_column.numeric_column(key = c) for c in colunas_usadas[1:17]]

#-------------Dividindo a base de dados entre treinamento e teste-------------#
from sklearn.model_selection import train_test_split
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, y, test_size = 0.3)

#-------------------------------Criando o grafo-------------------------------#
#                                                                             #
#--------------Bloco para efetuar o treinamento e a avaliação-----------------#
funcao_treinamento = tf.estimator.inputs.pandas_input_fn(x = X_treinamento, y = y_treinamento, batch_size = 32,
                                                        num_epochs = None, shuffle = True)

#----------------------------Cria o regressor---------------------------------#
regressor = tf.estimator.DNNRegressor(hidden_units = [8, 8, 8], feature_columns=colunas)

#----------------------------Efetua o treinamento-----------------------------#
regressor.train(input_fn = funcao_treinamento, steps = 20000)

#-----------Criando bloco para efetuar a previsão da base de teste------------#
funcao_previsao = tf.estimator.inputs.pandas_input_fn(x = X_teste, shuffle = False)

#----------------------------Efetuando previsões------------------------------#
previsoes = list(regressor.predict(input_fn=funcao_previsao))

valores_previsao = []
for p in previsoes:
    valores_previsao.append(p['predictions'])

#----------------Calculando o erro absoluto e o quadrático--------------------#
# Primeiro precisamos inverter o escalonamento, porém a y está no formato de  #
# series que é da forma (dimensão,), então precisamos efetuar um reshape nela #
#-----------------------------------------------------------------------------#
valores_previsao = scaler_y.inverse_transform(valores_previsao)
y_teste = scaler_y.inverse_transform(y_teste.values.reshape(-1,1))

from sklearn.metrics import mean_absolute_error, mean_squared_error
erro_absoluto = mean_absolute_error(y_teste, valores_previsao)
erro_quadratico = mean_squared_error(y_teste, valores_previsao)
print(f'O erro absoluto foi: {erro_absoluto} \nO erro quadrático foi: {erro_quadratico}')
