import tensorflow as tf

#----------------Coloca a base de dados na variável 'base'--------------------#
import pandas as pd
base = pd.read_csv('census.csv')

#-------------------Convertendo >50 para 1 e <=50 para 0----------------------#
# basicamente um encoder                                                      #
#-----------------------------------------------------------------------------#
def converte_classe(rotulo):
    if rotulo == ' >50K':
        return 1
    else:
        return 0

base['income'] = base['income'].apply(converte_classe) # Efetua a conversão

#----------Alocando os valores das colunas em previsores e classes------------#
# colocando todos os atributos em x exceto o income que vai para y            #
#-----------------------------------------------------------------------------#
X = base.drop('income', axis = 1)
y = base['income']


#-----------------Transformando o atributo idade em categórico----------------#
# o motivo disso é simplesmente para mostrar como se faz                      #
# para vermos melhor as faixas de idade plotaremos o histograma               #
#                                                                             #
# boundaries recebe as faixas                                                 #
#-----------------------------------------------------------------------------#
%matplotlib inline
base.age.hist()

idade = tf.feature_column.numeric_column('age') #Criando uma coluna numérica para receber a idade

idade_categorica = [tf.feature_column.bucketized_column(idade, boundaries=[20,30,40,50,60,70,80,90])] # efetuando a transformação

#-----------Criando uma lista com os atributos que são categóricos------------#
nome_colunas_categoricas = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country']

#-------------------------Criando uma coluna categórica-----------------------#
#precisamos passar o que tem dentro de cada uma, exemplo, sexo: temos que passar homem e mulher
#para ver o que tem dentro dos atributos utilize o comando 'X['atributo'].unique(). Porém o
#comando tf.feature_column.categorical_column_with_vocabulary_list juntamente com um for fará esse trabalho para nós
colunas_categoricas = [tf.feature_column.categorical_column_with_vocabulary_list(key = c, vocabulary_list=X[c].unique()) for c in nome_colunas_categoricas]

#----------agora vamos criar uma coluna para as variáveis numéricas-----------#
nome_colunas_numericas = ['final-weight', 'education-num', 'capital-gain', 'capital-loos', 'hour-per-week']
colunas_numericas = [ tf.feature_column.numeric_column(key = c) for c in nome_colunas_numericas ]

#------------criando uma coluna para receber o conjunto de todas--------------#
colunas = idade_categorica + colunas_categoricas + colunas_numericas

#-------------Dividindo a base de dados entre treinamento e teste-------------#
from sklearn.model_selection import train_test_split
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, y, test_size = 0.3)

#-------------------------------Criando o grafo-------------------------------#
#                                                                             #
#-----------------------Criando o bloco de treinamento------------------------#
funcao_treinamento = tf.estimator.inputs.pandas_input_fn(x = X_treinamento, y = y_treinamento,
                                                        batch_size = 32, num_epochs = None, shuffle = True)

#---------------------------Criando o classificador---------------------------#
classificador = tf.estimator.LinearClassifier(feature_columns=colunas)

#----------------------------Efetua o treinamento-----------------------------#
classificador.train(input_fn=funcao_treinamento, steps = 10000)

#-----------Criando bloco para efetuar a previsão da base de teste------------#
funcao_previsao = tf.estimator.inputs.pandas_input_fn(x = X_teste, shuffle = False)

#----------------------------Efetuando previsões------------------------------#
previsoes = list(classificador.predict(input_fn=funcao_previsao))

previsoes_final = []
for p in previsoes:
    previsoes_final.append(p['class_ids'])

#----------------------------Verificando precisão-----------------------------#
from sklearn.metrics import accuracy_score
taxa_acerto = accuracy_score(y_teste, previsoes_final)
