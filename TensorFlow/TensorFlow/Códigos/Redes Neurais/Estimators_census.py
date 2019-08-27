import pandas as pd
import tensorflow as tf

#----------------Coloca a base de dados na variável 'base'--------------------#
base = pd.read_csv('census.csv')
base.head()

#-------------------Convertendo >50 para 1 e <=50 para 0----------------------#
def converte_classe(rotulo):
    if rotulo == ' >50K':
        return 1
    else:
        return 0

base.income = base.income.apply(converte_classe)

#----------Alocando os valores das colunas em previsores e classes------------#
X = base.drop('income', axis = 1)
y = base.income

#-------------Dividindo a base de dados entre treinamento e teste-------------#
from sklearn.model_selection import train_test_split
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, y, test_size = 0.3)

#-------------------------Criando uma coluna categórica-----------------------#
workclass = tf.feature_column.categorical_column_with_hash_bucket(key = 'workclass', hash_bucket_size = 100) # colocando o hash muito alto, acaba que não existem tantos subatributos no atributo, dai ele procura automaticamente por todos e já os divide
education = tf.feature_column.categorical_column_with_hash_bucket(key = 'education', hash_bucket_size = 100)
marital_status = tf.feature_column.categorical_column_with_hash_bucket(key = 'marital-status', hash_bucket_size = 100)
occupation = tf.feature_column.categorical_column_with_hash_bucket(key = 'occupation', hash_bucket_size = 100)
relationship = tf.feature_column.categorical_column_with_hash_bucket(key = 'relationship', hash_bucket_size = 100)
race = tf.feature_column.categorical_column_with_hash_bucket(key = 'race', hash_bucket_size = 100)
country = tf.feature_column.categorical_column_with_hash_bucket(key = 'native-country', hash_bucket_size = 100)

sex = tf.feature_column.categorical_column_with_vocabulary_list(key = 'sex', vocabulary_list=[' Male', ' Female']) # esse é um jeito diferente de fazer a divisão dos atributos. Porém só é viável se tiver poucos subatributos

#----------Efetuando uma nova transformação nas variáveis categoricas---------#
embedded_workclass = tf.feature_column.embedding_column(workclass, dimension = 9)
embedded_education = tf.feature_column.embedding_column(education, dimension = len(base.education.unique()))
embedded_marital = tf.feature_column.embedding_column(marital_status, dimension = len(base['marital-status'].unique()))
embedded_occupation = tf.feature_column.embedding_column(occupation, dimension = len(base.occupation.unique()))
embedded_relationship = tf.feature_column.embedding_column(relationship, dimension = len(base.relationship.unique()))
embedded_race = tf.feature_column.embedding_column(race, dimension = len(base.race.unique()))
embedded_sex = tf.feature_column.embedding_column(sex, dimension = len(base.sex.unique()))
embedded_country = tf.feature_column.embedding_column(country, dimension = len(base['native-country'].unique()))

#---------------Efetuando a padronização dos atributos numéricos--------------#
base.age.mean() # 38.58
base.age.std() # 13.64

def padroniza_age(valor):
    return tf.divide(tf.subtract(tf.cast(valor, tf.float32), tf.constant(38.58)), tf.constant(13.64))

def padroniza_finalweight(valor):
    return tf.divide(tf.subtract(tf.cast(valor, tf.float32), tf.constant(189778.36)), tf.constant(105549.977))

def padroniza_education(valor):
    return tf.divide(tf.subtract(tf.cast(valor, tf.float32), tf.constant(10.08)), tf.constant(2.57))

def padroniza_capitalgain(valor):
    return tf.divide(tf.subtract(tf.cast(valor, tf.float32), tf.constant(1077.64)), tf.constant(7385.29))

def padroniza_capitalloos(valor):
    return tf.divide(tf.subtract(tf.cast(valor, tf.float32), tf.constant(87.30)), tf.constant(402.96))

def padroniza_hour(valor):
    return tf.divide(tf.subtract(tf.cast(valor, tf.float32), tf.constant(40.43)), tf.constant(12.34))

#----------agora vamos criar uma coluna para as variáveis numéricas-----------#
age = tf.feature_column.numeric_column(key = 'age', normalizer_fn = padroniza_age)
final_weight = tf.feature_column.numeric_column(key = 'final-weight', normalizer_fn = padroniza_finalweight)
education_num = tf.feature_column.numeric_column(key = 'education-num', normalizer_fn = padroniza_education)
capital_gain = tf.feature_column.numeric_column(key = 'capital-gain', normalizer_fn = padroniza_capitalgain)
capital_loos = tf.feature_column.numeric_column(key = 'capital-loos', normalizer_fn = padroniza_capitalloos)
hour = tf.feature_column.numeric_column(key = 'hour-per-week', normalizer_fn = padroniza_hour)


colunas_rna = [age, embedded_workclass, final_weight, embedded_education, education_num,
               embedded_marital, embedded_occupation, embedded_relationship,
               embedded_race, embedded_sex,
               capital_gain, capital_loos, hour, embedded_country]

#--------------------------Cria o bloco de treinamento------------------------#
funcao_treinamento = tf.estimator.inputs.pandas_input_fn(x = X_treinamento, y = y_treinamento,
                                                        batch_size = 32, num_epochs = None, shuffle = True)

#---------------------------Criando classificador-----------------------------#
classificador = tf.estimator.DNNClassifier(hidden_units = [8, 8], feature_columns=colunas_rna, n_classes=2)
classificador.train(input_fn = funcao_treinamento, steps = 10000)

#-------Criando o bloco para efetuar a avaliação da base de dados teste-------#
funcao_teste = tf.estimator.inputs.pandas_input_fn(x = X_teste, y = y_teste, batch_size = 32,
                                                  num_epochs = 1, shuffle = False)

#-------------------------------Avaliando o modelo----------------------------#
classificador.evaluate(input_fn=funcao_teste)
