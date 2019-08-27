import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#-------------------------Reseta grafos existentes----------------------------#
tf.reset_default_graph()

#--------------------Carregamento da base de dados----------------------------#
mnist = input_data.read_data_sets('mnist/', one_hot = True)

#------------------------Criando o placeholder--------------------------------#
ruido_ph = tf.placeholder(tf.float32, [None, 100]) #Valores aleatórios que serão as entradas
imagens_reais_ph = tf.placeholder(tf.float32, [None, 784])

#-----------------------Criando a rede do gerador-----------------------------#
def gerador(ruido, reuse = None):
    with tf.variable_scope('gerador', reuse = reuse):
        # 100 -> 128 -> 128 -> 784
        camada_oculta1 = tf.nn.relu(tf.layers.dense(inputs = ruido, units = 128))
        camada_oculta2 = tf.nn.relu(tf.layers.dense(inputs = camada_oculta1, units = 128))
        camada_saida = tf.layers.dense(inputs = camada_oculta2, units = 784, activation = tf.nn.tanh)
        return camada_saida

#--------------------Criando a rede do discriminador--------------------------#
# Logits são as previsões que não passaram pela função de ativação            #
#-----------------------------------------------------------------------------#
def discriminador(X, reuse = None):
    with tf.variable_scope('discriminador', reuse = reuse):
        # 784 -> 128 -> 128 -> 1
        camada_oculta1 = tf.nn.relu(tf.layers.dense(inputs = X, units = 128))
        camada_oculta2 = tf.nn.relu(tf.layers.dense(inputs = camada_oculta1, units = 128))
        logits = tf.layers.dense(camada_oculta2, units = 1)
        return logits

#-----------Passando para o discriminador as imagens fake e as reais----------#
logits_imagens_reais = discriminador(imagens_reais_ph)
logits_imagens_ruido = discriminador(gerador(ruido_ph), reuse = True)

#---------------Erros para as imagens reais e as imagens fake-----------------#
erro_discriminador_real = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits = logits_imagens_reais, labels = tf.ones_like(logits_imagens_reais) * (0.9)))
erro_discriminador_ruido = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits = logits_imagens_ruido, labels = tf.zeros_like(logits_imagens_ruido)))
erro_discriminador = erro_discriminador_real + erro_discriminador_ruido
erro_gerador = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits = logits_imagens_ruido, labels = tf.ones_like(logits_imagens_ruido)))

#--------Seleciona as variáveis passíveis de serem usadas para treinar--------#
variaveis = tf.trainable_variables()

#-----------Aloca as variáveis selecionadas para o discriminador--------------#
variaveis_discriminador = [v for v in variaveis if 'discriminador' in v.name]
print([v.name for v in variaveis_discriminador])

#--------------Aloca as variáveis selecionadas para o gerador-----------------#
variaveis_gerador = [v for v in variaveis if 'gerador' in v.name]
print([v.name for v in variaveis_gerador])

#--------Blocos de treinamento para o discriminador e para o gerador----------#
treinamento_discriminador = tf.train.AdamOptimizer(learning_rate = 0.001).minimize(erro_discriminador, var_list = variaveis_discriminador)
treinamento_gerador = tf.train.AdamOptimizer(learning_rate = 0.001).minimize(erro_gerador, var_list = variaveis_gerador)

#-------------------------Efetuando o treinamento-----------------------------#
batch_size = 100
amostras_teste = []
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoca in range(300):
        numero_batches = mnist.train.num_examples // batch_size
        for i in range(numero_batches):
            batch = mnist.train.next_batch(batch_size)
            imagens_batch = batch[0].reshape((100, 784))
            imagens_batch = imagens_batch * 2 - 1
            batch_ruido = np.random.uniform(-1, 1, size = (batch_size, 100))
            _, custod = sess.run([treinamento_discriminador, erro_discriminador], feed_dict = {imagens_reais_ph: imagens_batch, ruido_ph: batch_ruido})
            _, custog = sess.run([treinamento_gerador, erro_gerador], feed_dict = {ruido_ph: batch_ruido})
        if epoca % 50 == 0:
            print('época: ' + str(epoca + 1) + ' erro D: ' + str(custod) + ' erro G: ' + str(custog))
        ruido_teste = np.random.uniform(-1, 1, size = (1, 100))
        imagem_gerada = sess.run(gerador(ruido_ph, reuse = True), feed_dict = {ruido_ph: ruido_teste})
        amostras_teste.append(imagem_gerada)

#------------------------Vendo a imagem que foi gerada------------------------#
# 1ª época
plt.imshow(amostras_teste[0].reshape(28,28))
# 10ª época
plt.imshow(amostras_teste[10].reshape(28,28))
# 20ª época
plt.imshow(amostras_teste[20].reshape(28,28))
# 30ª época
plt.imshow(amostras_teste[30].reshape(28,28))
# 40ª época
plt.imshow(amostras_teste[40].reshape(28,28))
# 50ª época
plt.imshow(amostras_teste[50].reshape(28,28))
# 200ª época
plt.imshow(amostras_teste[200].reshape(28,28))

plt.imshow(amostra.reshape(28,28))

batch = mnist.train.next_batch(100)
batch[0].shape
imagens_batch = batch[0].reshape((100, 784))

imagens_batch.shape

imagens_batch[0]

imagens_batch = imagens_batch * 2 - 1
imagens_batch[0]

r.shape

r

r2

plt.imshow(amostras_teste[299].reshape(28,28))
