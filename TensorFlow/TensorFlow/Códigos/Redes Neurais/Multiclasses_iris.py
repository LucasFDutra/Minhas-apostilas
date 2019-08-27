from sklearn import datasets
import tensorflow as tf
import numpy as np

#----------Importando a base de dados iris do dataset do sklearn-------------#
iris = datasets.load_iris()

#--------------------------Criando os previsores------------------------------#
X = iris.data

#----------------------------Criando a classe---------------------------------#
y = iris.target

#--------------------------------Escalonando----------------------------------#
from sklearn.preprocessing import StandardScaler
scaler_x = StandardScaler()
X = scaler_x.fit_transform(X)

#-----------------------Criando variáveis do tipo dummy-----------------------#
from sklearn.preprocessing import OneHotEncoder
onehot = OneHotEncoder(categorical_features = [0])
y = y.reshape(-1, 1)
y = onehot.fit_transform(y).toarray()

#-----------------------Dividindo em teste e treinamento----------------------#
from sklearn.model_selection import train_test_split
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, y, test_size = 0.3)

#-----------------------Criando os neurônios de entrada-----------------------#
neuronios_entrada = X.shape[1] # Pega a quantidade de termos que tem na linha 1 de X, ou seja, ele pega o número de atributos.

#--------------------Criando os neurônios de camada oculta--------------------#
neuronios_oculta = int(np.ceil((X.shape[1] + y.shape[1]) / 2)) # Essa equação foi para retirar a quantidade de neurônios na camada oculta, mas não é obrigatório

#-------------------Criando os neurônios de camada de saída-------------------#
neuronios_saida = y.shape[1] # Indicando 3 neurônios de saída

#-----------------------Definindo os pesos iniciais---------------------------#
W = {'oculta': tf.Variable(tf.random_normal([neuronios_entrada, neuronios_oculta])),
     'saida': tf.Variable(tf.random_normal([neuronios_oculta, neuronios_saida]))}

#------------------------------Criando os bias--------------------------------#
b = {'oculta': tf.Variable(tf.random_normal([neuronios_oculta])),
     'saida': tf.Variable(tf.random_normal([neuronios_saida]))}

#-------Criando placeholder para receber os dados que vão aos neurônios-------#
xph = tf.placeholder('float', [None, neuronios_entrada])
yph = tf.placeholder('float', [None, neuronios_saida])

#---------------------------Criando os blocos do grafo------------------------#
def mlp(x, W, bias):
    camada_oculta = tf.add(tf.matmul(x, W['oculta']), bias['oculta'])
    camada_oculta_ativacao = tf.nn.relu(camada_oculta) # utiliza a função relu na camada oculta
    camada_saida = tf.add(tf.matmul(camada_oculta_ativacao, W['saida']), b['saida']) # ainda não definiu a função de ativação
    return camada_saida

modelo = mlp(xph, W, b)

#----------------------Criando bloco que calcula o erro-----------------------#
erro = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits = modelo, labels = yph))
otimizador = tf.train.AdamOptimizer(learning_rate = 0.0001).minimize(erro)

#--------------------------Definindo o batch size-----------------------------#
batch_size = 8

#-------------------Verificando quantas divisões ocorrerão--------------------#
batch_total = int(len(X_treinamento) / batch_size)

#---------------------------Executando o treinamento--------------------------#
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoca in range(3000):
        erro_medio = 0.0
        X_batches = np.array_split(X_treinamento, batch_total) #Pegando os registros dividindo em 13 batchs com 8 registros cada
        y_batches = np.array_split(y_treinamento, batch_total)
        for i in range(batch_total): # Roda todos os batchs a cada época
            X_batch, y_batch = X_batches[i], y_batches[i]
            _, custo = sess.run([otimizador, erro], feed_dict = {xph: X_batch, yph: y_batch})
            erro_medio += custo / batch_total
        if epoca % 500 == 0: # exibe o erro a cada 500 épocas
            print('Época: ' + str((epoca + 1)) + ' erro: ' + str(erro_medio))
    W_final, b_final = sess.run([W, b]) # Pegando o resultado dos pesos e bias finais

#--------------------------------Previsões------------------------------------#
# r1: retorna o valor sem passar por função de ativação                       #
# r2: retorna os valores para cada classe após passarem pela função softmax   #
# r3: pega o maior valor de probabilidade dentre as classes e atribui o valor #
#    correspondente daquela classe: 0, 1, 2                                   #
#-----------------------------------------------------------------------------#
previsoes_teste = mlp(xph, W_final, b_final)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    r1 = sess.run(previsoes_teste, feed_dict = {xph: X_teste}) # Valores que estão na saída da rede neural
    r2 = sess.run(tf.nn.softmax(r1))
    r3 = sess.run(tf.argmax(r2, 1))

#--------------------Verificando a precisão do algoritmo----------------------#
y_teste2 = np.argmax(y_teste, 1) # agrupando as dummy em uma única coluna

from sklearn.metrics import accuracy_score
taxa_acerto = accuracy_score(y_teste2, r3)
taxa_acerto
