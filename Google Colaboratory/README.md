# Sumário

- [COMMIT NO GITHUB](#commit-no-github)
- [TRABALHANDO COM GPU](#trabalhando-com-gpu)
- [SALVANDO E LENDO MODELOS DE MACHINE LEARNING NO GOOGLE DRIVE](#salvando-e-lendo-modelos-de-machine-learning-no-google-drive)
  - [MÉTODO 1](#método-1)
    - [Efetuando as configurações de conexão com o drive](#efetuando-as-configurações-de-conexão-com-o-drive)
    - [Salvando um modelo já treinado](#salvando-um-modelo-já-treinado)
    - [Fazendo upload do modelo treinado](#fazendo-upload-do-modelo-treinado)
  - [MÉTODO 2](#método-2)
    - [Efetuando as configurações de conexão com o drive](#efetuando-as-configurações-de-conexão-com-o-drive)
    - [Salvando um modelo já treinado](#salvando-um-modelo-já-treinado)
    - [Fazendo upload do modelo treinado](#fazendo-upload-do-modelo-treinado)
- [CRIANDO E SALVANDO GIFS](#criando-e-salvando-gifs)

# COMMIT NO GITHUB

Se tiver um notebook já salvo no GitHub e queira editá-lo a partir do google colaboratory, basta seguir os passos:

- 1 - Copie o url do repositório como se fosse fazer um clone dele.
- 2 - Abra o [google colaboratory](https://colab.research.google.com/notebooks/welcome.ipynb#recent=true)
- 3 - Nele você pode ir em "File -> Open notebook", conforme a imagem abaixo.

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/Google%20Colaboratory/Imagens/GitHub/Figura_1.png?raw=true)

- 4 - Após clicar em "Open notebook" aparecerá a tela da figura abaixo, no espaço indicado cole o url do repositório.

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/Google%20Colaboratory/Imagens/GitHub/Figura_2.png?raw=true)

- 5 - Edite o notebook.
- 6 - Para efetuar o commit no github vá em "File -> Save a copy on GitHub", como indicado abaixo.

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/Google%20Colaboratory/Imagens/GitHub/Figura_3.png?raw=true)

- 7 - Agora irá aparecer a tela abaixo, nela verifique se o repositório, o branch e o nome estão corretos, caso afirmativo basta clicar em "ok".

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/Google%20Colaboratory/Imagens/GitHub/Figura_4.png?raw=true)

> OBS 1.: Caso deixe a opção "Include a link to Colaboratory" o arquivo que será salvo no github receberá uma pequena imagem no início que será um link para poder abrir o arquivo diretamente do github para o colaboratory, assim não precisando efetuar as etapas de 1 a 4.

> OBS 2.: Caso não coloque o nome do arquivo igual ao original, será criado um novo arquivo que irá coexistir com o antigo.

# TRABALHANDO COM GPU

Uma das maiores vantagens do google colaboratory é trabalhar com GPUs direto da nuvem. Para poder aproveitar desse recurso é bem simples.

- 1 - Vá em "Edit -> Notebook Settings", conforme a imagem abaixo.

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/Google%20Colaboratory/Imagens/GPU/Figura_1.png?raw=true)

- 2 - Ao aparecer a tela indicada na figura abaixo, em "Hardware accelerator" escolha a opção "GPU" conforme os indicativos da imagem.

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/Google%20Colaboratory/Imagens/GPU/Figura_2.png?raw=true)

# SALVANDO E LENDO MODELOS DE MACHINE LEARNING NO GOOGLE DRIVE

## MÉTODO 1

### Efetuando as configurações de conexão com o drive

Primeiro de tudo certifique-se de que o navegador está logado na sua conta google. Pois só assim o colab será capaz de efetuar os passos a seguir.

> **É necessário efetuar todos esses códigos de configuração sempre que tiver um novo notebook**

Copie o código abaixo e execute.

> Irá aparecer um link, click nele e isso te direcionará para uma pagina da google gerando um código que deve ser copiado e colado no lugar que se abrirá no output da célula.

```Python
from google.colab import drive
drive.mount('/content/gdrive')
```

Para ver as pastas que contem dentro do seu drive, utilize o comando.

```python
!ls "gdrive/My Drive"
```

E pronto, para salvar ou carregar seus modelos no google drive basta indicar o caminho correto

```python
gdrive/My Drive/diretório"
```

### Salvando um modelo já treinado

```Python
model.save('gdrive/My Drive/Colab Notebooks/my_model.h5')
```

### Fazendo upload do modelo treinado

```Python
model = keras.models.load_model('gdrive/My Drive/Colab Notebooks/my_model.h5')
```

## MÉTODO 2

### Efetuando as configurações de conexão com o drive

Primeiro de tudo certifique-se de que o navegador está logado na sua conta google. Pois só assim o colab será capaz de efetuar os passos a seguir.

> **É necessário efetuar todos esses códigos de configuração sempre que tiver um novo notebook**

Copie o código abaixo e execute.

> Irá aparecer um link, click nele e isso te direcionará para uma pagina da google gerando um código que deve ser copiado e colado no lugar que se abrirá no output da célula.

```Python
!apt-get install -y -qq software-properties-common python-software-properties module-init-tools
!add-apt-repository -y ppa:alessandro-strada/ppa 2>&1 > /dev/null
!apt-get update -qq 2>&1 > /dev/null
!apt-get -y install -qq google-drive-ocamlfuse fuse

from google.colab import auth
auth.authenticate_user()
from oauth2client.client import GoogleCredentials
creds = GoogleCredentials.get_application_default()
import getpass
```

Agora rode o segundo grupo de comando, que também retornará um link, siga os mesmos procedimentos anteriores.

```Python
!google-drive-ocamlfuse -headless -id={creds.client_id} -secret={creds.client_secret} < /dev/null 2>&1 | grep URL
vcode = getpass.getpass()
!echo {vcode} | google-drive-ocamlfuse -headless -id={creds.client_id} -secret={creds.client_secret}
```

Execute mais esse grupo de comandos.

```Python
!mkdir -p drive
!google-drive-ocamlfuse drive
```

Agora já é possível navegar pelas pastas do google drive utilizando os comandos do linux antecedidos por ''!''.

### Salvando um modelo já treinado

```Python
model.save('drive/Colab Notebooks/my_model.h5')
```

### Fazendo upload do modelo treinado

```Python
model = keras.models.load_model('drive/Colab Notebooks/my_model.h5')
```

# CRIANDO E SALVANDO GIFS

```Python
import matplotlib.animation as animation
ims = []
fig = plt.figure()
for i in x_train_false_img:
    im = plt.imshow(i.reshape(28,28))
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=500, blit=True, repeat_delay=100)
ani.save('gdrive/My Drive/Colab Notebooks/Figura_3.gif', writer='pillow')
```
