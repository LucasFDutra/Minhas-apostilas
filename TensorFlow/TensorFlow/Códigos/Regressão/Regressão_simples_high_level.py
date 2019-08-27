import tensorflow as tf
#----------------Coloca a base de dados na variável 'base'--------------------#
import pandas as pd
base = pd.read_csv('house_prices.csv')

#----------Alocando os valores das colunas em previsores e classes------------#
x = base.iloc[:, 5:6].values
y = base.iloc[:, 2:3].values

#--------------------------Escalonando os valores-----------------------------#
from sklearn.preprocessing import StandardScaler
scaler_x = StandardScaler()
scaler_y = StandardScaler()
x = scaler_x.fit_transform(x)
y = scaler_y.fit_transform(y)

#-------------Dividindo a base de dados entre treinamento e teste-------------#
from sklearn.model_selection import train_test_split
x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(x, y, test_size = 0.3)

#----------Cria uma coluna para posteriormente receber os atributos-----------#
colunas = [tf.feature_column.numeric_column('x', shape = [1])]

#-------------------------------Criando o grafo-------------------------------#
# 'x' indica que a coluna que criamos anteriormente receberá os valores.      #
# shuffle=True indica que queremos que os dados venham de forma aleatório.    #
#-----------------------------------------------------------------------------#
#                                                                             #
#-----------------------Bloco para efetuar o treinamento----------------------#
funcao_treinamento = tf.estimator.inputs.numpy_input_fn({'x': x_treinamento}, y_treinamento,
                                                        batch_size = 32, num_epochs = None,
                                                        shuffle = True)

#--------------------------Bloco para efetuar o teste-------------------------#
funcao_teste = tf.estimator.inputs.numpy_input_fn({'x': x_teste}, shuffle = False) # os dados virão ordenados 1,2,...

#-----------------------------Criando Regressor-------------------------------#
regressor = tf.estimator.LinearRegressor(feature_columns=colunas)

#----------------------------Efetua o treinamento-----------------------------#
regressor.train(input_fn = funcao_treinamento, steps = 10000)

#----------------------------Efetuando previsões------------------------------#
previsoes = list(regressor.predict(input_fn = funcao_teste)) # Resulta em uma lista de dicionários. Sendo que o valor da previsão está em 'prediction'
valroes_previstos = []
for p in previsoes:
    valroes_previstos.append(p['predictions'])

#----------------Calculando o erro absoluto e o quadrático--------------------#
# para isso é primeiramente necessário inverter o escalonamento das previsoes #
# e de y.                                                                     #
#-----------------------------------------------------------------------------#
y_teste = scaler_y.inverse_transform(y_teste)
valroes_previstos = scaler_y.inverse_transform(valroes_previstos)

from sklearn.metrics import mean_absolute_error, mean_squared_error
erro_absoluto = mean_absolute_error(y_teste, valroes_previstos)
erro_quadratico = mean_squared_error(y_teste, valroes_previstos)
print(f'O erro absoluto foi: {erro_absoluto} \nO erro quadrático foi: {erro_quadratico}')
