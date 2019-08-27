# **Apostila de python**

Autor: Lucas Felipe Dutra

**ANTES DE QUALQUER COISA, VEJA ESSE VIDEO [AQUI](https://www.youtube.com/watch?v=9w3o9NHXqu0&list=PLMdYygf53DP5Sc6yFYs6ZmjsuuA2fu0TK) PARA APRENDER MAIS SOBRE CLEAN CODE**

# **1. FERRAMENTAS**

Além de diversos cursos e livros que pode-se achar para python, um dos melhores lugares para se aprender a linguagem é com a propria documentação, que é muito bem organizada e de fácil entendimento. Segue o [link](https://docs.python.org/3/tutorial/index.html).

Abaixo você verá, na ordem de indicação, algumas alternativas de softwares que nos permitem programar em python (Para quem gosta de IDE veja o pycharm - tópico 5).

- **1 - Google colaboratory:** É um jupyter notebook que roda totalmente em nuvem e não precisa de nenhuma configuração extra, tudo já está pronto, é só programar.

  - Site: [Google colaboratory](https://colab.research.google.com/notebooks/welcome.ipynb#recent=true)
  - Tutorial: [Get started with Google Colaboratory](https://www.youtube.com/watch?v=inN8seMm7UI)

- **2 - Jupyter notebook:** O google colaboratory é um jupyter notebook, porém em nuvem. O jupyter roda na sua máquina, logo precisará configurar, porém sua interface gráfica roda via browser.

  - Site: [Jupyter notebook](https://jupyter.org/)
  - Tutorial: [Quick introduction to Jupyter Notebook](https://www.youtube.com/watch?v=jZ952vChhuI)

- **3 - Visual Studio Code** É um editor de texto simples, porém possui diversas extensões que deixam ele melhor do que uma IDE

  - Site: [Vscode](https://code.visualstudio.com/)

- **4 - Atom:** É um editor de texto simples, porém possui diversas extensões que deixam ele melhor do que uma IDE

  - Site: [Atom](https://atom.io/)

- **5 - PyCharm:** Para quem gosta de IDE.
  - Site: [PyCharm](https://www.jetbrains.com/pycharm/)

## 1.1 CONFIGURANDO O SEU COMPUTADOR

Caso não tenha optado por usar o google colaboratory então você vai precisar configurar seu computador.

### **1.1.1 Instalando o python**

Para instalar o python em qualquer sistema operacional recomendo assistir o vídeo [Instalando o Python3 e o IDLE](https://www.youtube.com/watch?v=VuKvR1J2LQE&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=3).

**Para usuários linux:** O python já vem instalado nas distribuições linux. Verifique com o comando no terminal:

```sh
python3 --version
```

Porém se no seu caso ele não estiver instalado então rode o comando:

- Para Debian/Ubuntu/Linux Mint

```sh
sudo apt-get install python3
```

- Para OpenSUSE

```sh
sudo zypper install python3
```

- Para Fedora

```sh
sudo dnf install python3
```

- Para RedHat

```sh
sudo yum install python3
```

### **1.1.2 Instalando o jupyter notebook**

#### 1.1.2.1 Linux

Digite os comandos abaixo em seu terminal:

```sh
sudo apt install python3-dev python3-pip

sudo python3 -m pip install --upgrade pip

sudo python3 -m pip install jupyter
```

#### 1.1.2.2 Windows

Digite os comandos no cmd:

```sh
python -m pip install --upgrade pip

python -m pip install jupyter
```

> **OBS.: Caso o path do comando python não esteja indicado, o cmd não irá reconhecer o comando. Caso isso aconteça veja o vídeo: [How to add Python Path to Environment Variables in Windows 10](https://www.youtube.com/watch?v=Y2q_b4ugPWk), mas atenção a qual versão do python especificamente você está usando.**

### 1.1.3 Instalando o Vscode

Abra o link do site, baixe o instalador e de dois cliques. Clique em ctrl+n para iniciar um novo arquivo e o salve com a extensão `.py` por exemplo: `meu_primeiro_programa.py` e o vscode já pedirá para instalar uma extensão, recomendo que a instale (vai aparecer um popup com um botão escrito instalar) e pronto, ele já está pronto para programar em python

### 1.1.4 Instalando o atom

Para instalar e configurar o atom veja o vídeo [Tutorial Programando em Python com Atom](https://www.youtube.com/watch?v=0YD-Qjs9HDg).

### **1.1.5 Instalando o pycharm**

Para instalar o pycharm é necessário possuir primeiramente o python, e então depois você pode instalá-lo. E para instalar o pycharm em windows e mac recomendo assistir o vídeo [Instalando o PyCharm e o QPython3](https://www.youtube.com/watch?v=ElRd0cbXIv4&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=6).

**Para usuários linux:** não sigam o vídeo, pois é bem mais simples do que o método que ele utilizou, basta entrar na loja da sua distribuição e o pycharm community estará lá para instalar. Se caso não houver ele na sua sua loja, veja o video.

# 2. IDENTAÇÃO

Veja algumas caracteristicas do python:

- **Comentários:** Para criar comentários utilize o caracter `#`.

- **Fim de comando:** O final de um comando é identificado quando acaba a linha.

```python
print('olá') # comando 1
print('mundo') # comando 2
```

- **Bloco de código** Um bloco de código é representado por tabulação.

```python
for i in range(10): # inicia o bloco do loop
    print(i) # linha 1 do loop
    print(i+1) # linha 2 do loop
print('olá mundo') # não está mais dentro do loop
```

- **Declaração de variáveis:** Não é necessário declarar variáveis. Ou seja, basta apenas ir utilizando e atribuindo valor às variáveis durante o código que o python entenderá o tipo de variável a qual corresponde. Sendo que os tipos de variável existentes são:
  - String (str): Para textos.
  - Inteiros (int): Para números inteiros.
  - Flutuante (float): Para números reais.

```python
a = 'teste' # str
b = 15 # int
c = 3.141592 #float
```

# **3. INTERAÇÃO USUÁRIO/SOFTWARE**

Os comando de entrada e saída de dados já estão implementados nativamente no python, ou seja, não é necessário importar bibliotecas para efetuar a comunicação com teclado ou monitor.

## 3.1 RECEBER ENTRADA

Para receber dados do teclado utilizamos o comando `input`.

```python
Variável = tipo (input('texto'))
```

Porém quando recebemos uma entrada do teclado, o python entende essa entrada como sendo uma string, logo, se quisermos entrar com outro tipo de dados devemos efetuar uma conversão. Veja o exemplo abaixo.

```python
N = int(input('digite um número: '))
F = float(input('digite um número: '))
```

Também é possível receber múltiplas entradas de uma única vez, com o auxílio do comando `split`. Veja o exemplo abaixo em que receberemos dois números inteiros.

```python
split('o_que_vai_espaçar_os_valores)
```

```python
N1, N2 = input('digite os números: ').split(' ') # um espaço irá separar os valores
```

Uma desvantagem do comando split é que os dados vão obrigatoriamente ser strings. Mas depois é só converter.

## 3.2 IMPRIMIR NA TELA

Para mostrar informações na tela vamos utilizar o comando `print`, que atualmente segue dois modos para ser utilizado.

```python
print('texto {}, {}'.format(a, b))
print(f'texto {a}, {b}')
```

- **Para o comando .format:** O caracter `{}` indica a posição que a variável que está dentro de `.format` irá aparecer no texto, sendo que a ordem importa.
- **Para o comando f:** Nesse caso a variável deve ser colocada dentro de `{}`.

> OBS.: Veja que em nenhum momento é necessário colocar à qual tipo a variável pertence, os comandos ''format'' ou ''f'' já identificam tudo, e com o ''print'' é possivel mostar até listas completas sem precisar de um loop.

- **Exemplo:** Para o exemplo abaixo irei alocar previamente um valor a uma dada variável, adicionarei outro valor a outra variável, somarei as duas e mostrarei o resultado.

  ```Python
  a = 40
  b = int(input('digite o número a ser somado com {}: '.format(a)))
  print(f'o resultado da soma é {a+b}')
  ```

- Saída:
  ```Python
  digite o número a ser somado com 40: 20
  o resultado da soma é 60
  ```

# **4. ESTRUTURAS COMPOSTAS**

Como vimos acima, uma variável simples pode armazenar apenas um dado por vez, seja ele um int, float ou string. Porém, se quisermos armazenar em um mesmo lugar vários dados devemos utilizar estruturas compostas.

As estruturas compostas estão divididas em.

- Listas
- Tuplas
- Dicionários

Sendo que cada uma tem suas finalidades.

## 4.1 LISTAS

- Uma lista já possui dimensões "ilimitadas" (dependendo apenas do tamanho da sua memória).

- Uma lista é dada por um conjunto de variáveis dentro entre couchetes. Sendo que começamos a contar as posições em zero, ou seja, var_0 é a posição 0, var_1 é a posição 1, e assim por diante.
  - Veja a representação de uma lista: `[var_0, var_1,..., var_n]`

Veja a seguir quase tudo que é possível fazer com uma lista.

### **4.1.1 Declaração**

```python
lista = [] #lista limpa
lista = ['a', 1, 2.3] #lista pré-definida
```

### **4.1.2 Acessar um termo**

```python
lista[posição_do_termo]
```

### **4.1.3 Inserindo novos termos**

```python
lista.append(variável)
```

### **4.1.4 Incorporando uma lista à outra**

```python
lista.extend(outra_lista)
```

### **4.1.5 Inserindo elemento em uma posição específica**

```python
lista.insert(posição, valor_a_ser_inserindo)
```

### **4.1.6 Excluindo termo**

```python
lista.remove(termo_a_ser_removido)

del lista[inicio:fim]
```

O primeiro método vai elimina por valor, já o segundo elimina por posição. Ou seja, se tivermos uma lista `[1,2,3,1]` e mandarmos retirar o valor o segundo valor 1 os resultados serão:

```
lista.remove(1) # lista final: [2,3,1] -> não cumpre a função quando temos um número mais de uma vez
del lista[3:4] # lista final: [1,2,3]
```

### **4.1.7 Remove um item e o retorna**

```python
lista.pop(posição_do_termo_a_ser_retornado)
```

Caso não exista argumento, o comando irá retornar o ultimo elemento da lista.

### **4.1.8 Limpando uma lista**

```python
lista.clear()

lista = []
```

### **4.1.9 Obter índice de um elemento**

```python
lista.index(termo, inicio)
```

A busta é feita por valor, ou seja o que a função retorna é o valor da menor posição na lista em que se encontra o termo desejado. Se “inicio” tiver valor, ele pesquisara somente a frente dessa posição, caso contrário a pesquisa partirá da posição 0.

### **4.1.10 Obter o número de vezes que um termo X aparece na lista**

```python
lista.count(x)
```

### **4.1.11 Copiando uma lista**

```python
nova_lista = lista.copy()
```

### **4.1.12 Retornar o tamanho de uma lista**

```python
len(lista)
```

### **4.1.13 Inverter os elementos**

```python
lista.reverse()
```

### **4.1.14 Ordenar uma lista**

```python
lista_ordenada = sorted(lista)
```

### **4.1.15 Maior termo da lista**

```python
max(lista)
```

### **4.1.16 Exemplos**

- Exemplo:

  ```Python
  # Declaração
  lista = []
  lista_2 = [1,2,3]
  ```

- Exemplo:

  ```Python
  # Inserindo Termos
  lista.append(a)
  lista.append(b)
  print(lista)
  ```

- Saída:

  ```Python
  [40, 20]
  ```

- Exemplo:

  ```Python
  # Utilizando comando input para carregar uma lista método 1
  tamanho_da_lista = 2
  lista = []
  for i in range(tamanho_da_lista):
      lista.append(int(input(f'digite o {i} valor: ')))
  print(lista)
  ```

- Saída:

  ```Python
  digite o 0 valor: 20
  digite o 1 valor: 40
  [20, 40]
  ```

- Exemplo:

  ```Python
  # Utilizando comando input para carregar uma lista método 2
  lista = [int(i) for i in input('digite os valores espaçados: ').split(' ')]
  print(lista)

  # Veja que nesse método não é necessário definir o tamanho da lista
  ```

- Saída:

  ```Python
  digite os valores espaçados: 20 40
  [20, 40]
  ```

- Exemplo:

  ```Python
  # Incorporando uma lista a outra
  lista.extend(lista_2)
  print(lista)
  ```

- Saída:

  ```Python
  [20, 40, 1, 2, 3]
  ```

- Exemplo:

  ```Python
  # Inserindo elemento em uma posição qualquer da lista
  lista.insert(3,9)
  print(lista)
  ```

- Saída:

  ```Python
  [20, 40, 1, 9, 2, 3]
  ```

- Exemplo:

  ```Python
  # Excluindo termo
  lista.remove(9)
  print(lista)
  ```

- Saída:

  ```Python
  [20, 40, 1, 2, 3]
  ```

- Exemplo:

  ```Python
  # Remove um item e o retorna
  lista.pop(1)
  ```

- Saída:

  ```Python
  40
  ```

- Exemplo:

  ```Python
  # Limpando uma lista
  lista.clear()
  print(lista)
  ```

- Saída:

  ```Python
  []
  ```

- Exemplo:

  ```Python
  # Obter índice de um elemento
  lista = [1,2,3,1]
  lista.index(2)
  ```

- Saída:

  ```Python
  1
  ```

- Exemplo:

  ```Python
  # Obter o número de vezes que um termo x aparece na lista
  lista.count(1)
  ```

- Saída:

  ```Python
  2
  ```

- Exemplo:

  ```Python
  # Copiando uma lista
  lista_nova = lista.copy()
  print(lista_nova)
  ```

- Saída:

  ```Python
  [1, 2, 3, 1]
  ```

- Exemplo:

  ```Python
  # Retornando o tamanho de uma lista
  len(lista)
  ```

- Saída:

  ```Python
  4
  ```

- Exemplo:

  ```Python
  # Inverter os elementos de uma lista
  lista.reverse()
  print(lista)
  ```

- Saída:

  ```Python
  [1, 3, 2, 1]
  ```

- Exemplo:

  ```Python
  # Ordenando uma lista
  lista_ordenada = sorted(lista)
  print(lista_ordenada)
  ```

- Saída:

  ```Python
  [1, 1, 2, 3]
  ```

- Exemplo:

  ```Python
  # Maior termo de uma lista
  max(lista)
  ```

- Saída:

  ```Python
  3
  ```

### **4.1.17 Listas aninhadas**

Uma lista aninhada é uma lista que se encontra dentro de outra lista.

- Lista normal: `[var_0, var_1,..., var_n]`
- Lista aninhada: `[[var_0,..., var_n1],..., [var_0,..., var_nm]]`

> OBS.: Veja que as listas não precisão ter as mesmas dimensões. E também é possível colocar mais listas dentro de listas, assim sendo é possível criar uma lista com n dimensões.

#### 4.1.17.1 Declaração

Uma lista aninhada é declaráda do mesmo jeito que uma lista normal, ou seja:

```python
lista_aninhada = [] #lista limpa
lista_aninhada = [[1,2,3],[1,25]] #lista pré-definida
```

#### 4.1.17.2 Acessando termos

```python
lista_aninhada[termo_dim_1][termo_dim_2]...[termo_dim_n]
```

Agora se quiser preencer uma lista aninhada em tempo de execução, veja o exemplo abaixo:

- Exemplo:

  ```Python
  # Criando uma matriz 3x3 método 1
  matriz = []
  for i in range(0,3):
      vetor = []
      for j in range(0,3):
          vetor.append(i)
      matriz.append(vetor)
  print(matriz)
  ```

- Saída:

  ```Python
  [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
  ```

- Exemplo:

  ```Python
  # Criando uma matriz 3x3 método 2

  matriz = [[int(i) for i in input('digite: ').split(' ')] for x in range(3)]
  print(matriz)
  ```

- Saída:

  ```Python
  digite: 0 0 0
  digite: 1 1 1
  digite: 2 2 2
  [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
  ```

#### 4.1.17.3 Algumas características de listas aninhadas

- Os comandos empregados para uma lista também se aplicam à uma matriz.

- Porém o comando de cópia não é muito bem executado. Para efetuar a cópia faça:

- Exemplo:

  ```Python
  matriz_copia = []
  def cópia(matriz_copia):
      matriz_2 = [matriz_copia[i].copy() for i in range(len(matriz_copia))]
      return matriz_2

  print(cópia(matriz))
  ```

- Saída:

  ```Python
  [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
  ```

#### 4.1.17.4 Matriz transposta

- Exemplo:

  ```Python
  matriz_transposta = []
  matriz_transposta = list(zip(*matriz))
  print(matriz_transposta)
  ```

- Saída:

  ```Python
  [(0, 1, 2), (0, 1, 2), (0, 1, 2)]
  ```

Veja que as listas internas à matriz, são diferentes, elas são tuplas. Tuplas são imutáveis, e para trabalhar melhor com elas é bom que as converta para listas. Para converter toda a matriz deve-se:

- Exemplo:

  ```Python
  for i in range(0,len(matriz_transposta)):
      matriz_transposta[i] = list(matriz_transposta[i])

  print(matriz_transposta)
  ```

- Saída:

  ```Python
  [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
  ```

## 4.2 TUPLAS

A tupla é uma variável composta, que é muito semelhante à uma lista. Porém uma tupla é imutável, ou seja, ela deve receber seus termos assim que é declarada, e posteriormente é impossível inserir novos termos, retirar termos ou trocar termos.

É possível gerar tuplas aninhadas assim como em listas, porém elas possuem as mesmas limitações de uma tupla simples. E também é possível gerar uma lista de tuplas, e uma tupla de listas.

### **4.2.1 Declaração**

```python
tupla = ('termo 1', 'termo 2', ..., 'termo n')
tupla = ('termo 1', [var_0, var_1,..., var_n])
```

### **4.2.2 Acessar elementos da tupla**

```python
tupla[posição do termo]
```

### **4.2.3 Iincorporando uma tupla à outra**

```python
tupla_3 = tupla_1 + tupla_2
```

### **4.2.4 Limpando uma tupla**

```python
tupla = ()
```

### **4.2.5 Obter Índice de um elemento**

```python
tupla.index(termo, inicio)
```

A busta é feita por valor, ou seja o que a função retorna é o valor da menor posição na tupla em que se encontra o termo desejado. Se “inicio” tiver valor, ele pesquisara somente a frente dessa posição, caso contrário a pesquisa partirá da posição 0.

### **4.2.6 Obter o número de vezes que um termo X aparece na tupla**

```python
tupla.count(x)
```

### **4.2.7 Retornar o tamanho de uma tupla**

```python
len(tupla)
```

### **4.2.8 Ordenar uma tupla**

```python
tupla_ordenada = tuple(sorted(tupla))
```

O comando `sorted` retorna uma lista, por isso o comando `tuple` para poder converter para tupla.

### **4.2.9 Maior termo da tupla**

```python
max(tupla)
```

### **4.2.10 Convertendo uma tupla em uma lista**

```python
lista = list(tupla)
```

### **4.2.11 Apagar uma tupla**

```python
del(tupla)
```

### **4.2.12 Exemplos**

- Exemplo:

  ```python
  # Declaração
  tupla_1 = (1,2,3)
  tupla_2 = (4,5,6)
  ```

- Exemplo:

  ```python
  # Acessar elementos da tupla
  tupla_1[1]
  ```

- Saída:

  ```Python
  2
  ```

- Exemplo:

  ```python
  # Incorporando uma tupla a outra
  c = tupla_1 + tupla_2
  print(c)
  ```

- Saída:

  ```Python
  (1, 2, 3, 4, 5, 6)
  ```

- Exemplo:

  ```python
  # Limpando uma tupla
  tupla_1 = ()
  print(tupla_1)
  ```

- Saída:

  ```Python
  ()
  ```

- Exemplo:

  ```python
  # Obter índice de um elemento
  tupla = (1,2,3,1)
  tupla.index(2)
  ```

- Saída:

  ```Python
  1
  ```

- Exemplo:

  ```python
  # Obter o número de vezes que um termo x aparece na tupla
  tupla.count(1)
  ```

- Saída:

  ```Python
  2
  ```

- Exemplo:

  ```python
  # Retornando o tamanho de uma tupla
  len(tupla)
  ```

- Saída:

  ```Python
  4
  ```

- Exemplo:

  ```python
  # Ordenando uma tupla
  tupla_ordenada = tuple(sorted(tupla))
  print(tupla_ordenada)
  ```

- Saída:

  ```Python
  (1, 1, 2, 3)
  ```

- Exemplo:

  ```python
  # Maior termo de uma tupla
  max(tupla)
  ```

- Saída:

  ```Python
  3
  ```

- Exemplo:

  ```python
  # Convertendo uma tupla em uma lista
  lista = list(tupla)
  print(lista)
  ```

- Saída:

  ```Python
  [1, 2, 3, 1]
  ```

- Exemplo:

  ```python
  # Apager uma tupla
  del(tupla)
  ```

## 4.3 DICIONÁRIOS

Dicionários não são imutáveis como as tuplas. Dentre as diferenças que existem entre dicionários e listas temos:

- Não é possível criar um dicionário de dicionários, o que pode-se fazer é criar tuplas ou listas de dicionários. Ou dicionários de listas e tuplas.

- Em listas os índices eram numéricos, em dicionários os índices são literais. Ou seja:

  - Lista:
    - Estrutura:
      - `lista = [maçã, 100]`
    - Índices:
      - `[0,1]`
  - Dicionário:
    - Estrutura:
      - `dicionário = {maçã, 100}`
    - Índices:

      - `{fruta, massa}`

### **4.3.1 Declaração**

```python
dicionario = {}
dicionario = dict{}
dicionario = {'índice1': termo1, 'índice2': termo2, .., 'índice_n': termo_n}
dicionario = {'índice1': [var_0,..., var_n], 'índice2': termo2,..., 'índice_n': termo_n}
```

> OBS.: Os índices podem ser tanto strings como numéricos. Porém para strings é necessário utilizar aspas.

### **4.3.2 Inserindo termos**

```python
dicionario['novo_índice'] = novo_elemento
```

### **4.3.3 Acessar elementos do dicionário**

- Pegando todos os elementos do dicionário:

```python
dicionario.values()
```

- Pegando todos os índices do dicionário:

```python
dicionario.keys()
```

- Pegando tanto os elementos quanto os índices:

```python
dicionario.items()
```

- Pegando elemento especifico

```python
dicionario[indice]
```

### **4.3.4 Excluindo termo**

```python
del dicionario[índice]
```

### **4.3.5 Remove um item e o retorna**

```python
dicionario.pop(índice)
```

### **4.3.6 Limpando um dicionário**

```python
dicionario.clear()
```

### **4.3.7 Copiando um dicionário**

```python
novo_dicionario = dicionario.copy()
```

### **4.3.8 Retornar o tamanho de um dicionário**

```python
len(dicionario)
```

### **4.3.9 Ordenar um dicionário**

```python
dicionario_ordenado = dict(sorted(dicionario.items()))
```

### **4.3.10 Maior termo do dicionário**

- Maior elemento

```python
max(dicionario.values())
```

> OBS.: Só funciona se todos os elementos forem do mesmo tipo.

- Maior índice

```python
max(dicionario.keys())
```

> OBS.: Só funciona se todos os índices forem do mesmo tipo.

### **4.3.11 Exemplos**

- Exemplo:

  ```python
  # Declaração
  dicionario = {'nome do filme': 'star wars',
              'ano': 1997}
  ```

- Exemplo:

  ```python
  # Inserindo Termos
  dicionario['diretor'] = 'george lucas'
  ```

- Exemplo:

  ```python
  # Pegando todos os elementos do dicionário:
  dicionario.values()
  ```

- Saída:

  ```python
  dict_values(['star wars', 1997, 'george lucas'])
  ```

- Exemplo:

  ```python
  # Pegando todos os índices do dicionário:
  dicionario.keys()
  ```

- Saída:

  ```python
  dict_keys(['nome do filme', 'ano', 'diretor'])
  ```

- Exemplo:

  ```python
  # Pegando tanto os elementos quanto os índices:
  dicionario.items()
  ```

- Saída:

  ```python
  dict_items([('nome do filme', 'star wars'), ('ano', 1997), ('diretor', 'george lucas')])
  ```

- Exemplo:

  ```python
  # Pegando elemento especifico
  dicionario['nome do filme']
  ```

- Saída:

  ```python
  'star wars'
  ```

- Exemplo:

  ```python
  ## Excluindo termo
  del dicionario['diretor']
  print(dicionario)
  ```

- Saída:

  ```python
  {'nome do filme': 'star wars', 'ano': 1997}
  ```

- Exemplo:

  ```python
  # Remove um item e o retorna
  dicionario.pop('ano')
  print(dicionario)
  ```

- Saída:

  ```python
  {'nome do filme': 'star wars'}
  ```

- Exemplo:

  ```python
  # Limpando um dicionário
  dicionario.clear()
  print(dicionario)
  ```

- Saída:

  ```python
  {}
  ```

- Exemplo:

  ```python
  # Copiando um dicionário
  dicionario = {'nome do filme': 'star wars', 'ano': 1997}
  novo_dicionario = dicionario.copy()
  print(novo_dicionario)
  ```

- Saída:

  ```python
  {'nome do filme': 'star wars', 'ano': 1997}
  ```

- Exemplo:

  ```python
  # Retorna o tamanho de um dicionário
  len(dicionario)
  ```

- Saída:

  ```python
  2
  ```

- Exemplo:

  ```python
  # Ordena um dicionário
  dicionario_ordenado = dict(sorted(dicionario.items()))
  print(dicionario_ordenado)
  ```

- Saída:

  ```python
  {'ano': 1997, 'nome do filme': 'star wars'}
  ```

- Exemplo:

  ```python
  # Maior índice
  max(dicionario.keys())
  ```

- Saída:

  ```python
  'nome do filme'
  ```

# **5. ESTRUTURAS DE REPETIÇÃO**

As estruturas de repetição são utilizadas quando queremos efetuar uma mesma tarefa n vezes, ou até que uma dada condição seja atingida.

## 5.1 FOR

```python
for i in range(de_onde, até_onde, passo):
    Código...
```

- Exemplo:

  ```Python
  for i in range(0,10,2):
      print(i)
  ```

- Saída:

  ```Python
  0
  2
  4
  6
  8
  ```

### **5.1.1 For com listas**

```python
for i in lista:
```

- Exemplo:

  ```Python
  lista = [10,2,32,1]

  for i in lista:
      print(i)
  ```

- Saída:

  ```Python
  10
  2
  32
  1
  ```

### **5.1.1 For com tuplas**

```python
for i in tupla:
```

- Exemplo:

  ```Python
  tupla = (10,2,32,1)

  for i in tupla:
      print(i)
  ```

- Saída:

  ```Python
  10
  2
  32
  1
  ```

### **5.1.1 For com dicionários**

**Percorrendo apenas elementos:**

```python
for i in dicionario.values():
```

- Exemplo:

  ```Python
  dicionario = {'nome do filme': 'star wars',
              'ano': 1997}

  for i in dicionario.values():
      print(i)
  ```

- Saída:

  ```Python
  star wars
  1997
  ```

**Percorrendo apenas índices:**

```python
for i in dicionario.keys():
```

Considerando o mesmo dicionário de antes

- Exemplo:

  ```Python
  for i in dicionario.keys():
      print(i)
  ```

- Saída:

  ```Python
  nome do filme
  ano
  ```

````

**Percorrendo elementos e índices:**
```python
for i,j in dicionario.items():
````

- Exemplo:

  ```Python
  for i,j in dicionario.items():
      print(i, j)
  ```

- Saída:

  ```Python
  nome do filme star wars
  ano 1997
  ```

## 5.2 WHILE

```python
while (condições):
    Código...
```

- Exemplo:

  ```Python
  while(a > 35 ):
      print(a)
      a -= 1
  ```

- Saída:

  ```Python
  40
  39
  38
  37
  36
  ```

# **6. CONDICIONAIS**

## 6.1 IF

```python
if condição:
    Código...
```

## 6.2 ELIF

É uma condição que só é analisada caso a condição em if não seja atendida.

```python
elif condição_2:
    Código...
```

## 6.3 ELSE

Engloba tudo que for o contrário das condições impostas nos if’s e nos elif.

```python
else:
    Código...
```

## 6.4 OPERADORES

- **and:** Condição 'a' e condição 'b' devem ser atendidas.
- **or:** Condição 'a' ou condição 'b' devem ser atendidas.
- **maior:** >
- **maior ou igual:** >=
- **menor:** <
- **menor ou igual:** <=

- **diferente:** !=
- **igual:** ==

- **Verdadeiro:** True

- **Falso:** False

* Exemplo:

  ```Python
  a = 10
  b = 30

  if a == 1 and b == 2:
      print('if')
  elif a == 30 or a == 20:
      print('elif')
  else:
      print('else')
  ```

* Saída:

  ```Python
  else
  ```

# **7. FUNÇÕES**

Funções são blocos de código em que colocam-se tarefas que serão utilizadas várias vezes durante o código.

```python
def nome_da_função(parâmetro_1, parâmetro_2...):
    Código..
    return o_que_deve_retornar
```

O return não é obrigatório.

- Exemplo:

    ```Python
    def função(a,b):
        c = a+b
        return c

    soma = função(1,2)
    print(soma)
    ```

- Saída:

    ```Python
    3
    ```

# **8. PROGRAMAÇÃO ORIENTADA A OBJETO**

## 8.1 CRIAÇÃO DE CLASSES

- Toda classe precisa ter a função `__init__` e toda função precisa ter o parâmetro `self`.

```python 
class nome_da_classe:
    def __init__(self, parâmetro_1, parâmetro_2):
        # Adicione tudo o que quiser para iniciar assim que a classe for chamada.
        
        # Para declarar uma variável dentro do init
        self.var_1 = x
        self.var_2 = parâmetro_1
        
        # Todas as variáveis que aqui estão podem ser usadas em outras funções da classe
        
    def uma_função_qualquer(self,parâmetros_da_função):
        Código_da_função
```

- Exemplo:

    ```Python
    class person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def print_objetc(self):
            print('Meu nome é {}, e eu tenho {} anos.'.format(self.name, self.age))


    name = 'João'
    age = 18

    person1 = person(name,age)
    person1.print_objetc()
    ```

- Saída:

    ```Python
    Meu nome é João, e eu tenho 18 anos.
    ```

## 8.2 HERANÇA

Herança é o nome dado para a relação entre uma classe mãe e uma classe filha. A filha herda os métodos e os atributos da classe mãe, ou seja, se a mãe faz uma coisa 'x', a filha também fará, se a classe mãe possui y, a classe filha também. Porém, é possível que a classe filha herde somente uma das duas coisas.

### **8.2.1 Herdando apenas os métodos**

- Exemplo

    ```Python
    class pai:
        def __init__(self):
            print('classe pai')
        def função_pai(self):
            print('função pai')

    # Para fazer a herança coloque o nome da classe pai dentro do parenteses da classe filha.
    class filha(pai):
        def __init__(self):
            print('classe filha')
        def função_filha(self):
            print('função filha')
    ```

    - Chamada 1:

        ```Python
        # Criação do objeto pai e filha.
        p = pai()     # irá exibir o init da classe pai.
        f = filha()   # irá exibir o init da classe filha.
        ```

    - Saída 1:

        ```Python
        classe pai
        classe filha
        ```

    - Chamada 2:

        ```Python
        # Execução da função_pai
        p.função_pai()
        ```

    - Saída 2:

        ```Python
        função pai
        ```

    - Chamada 3

        ```Python
        # Execução da função_filha
        f.função_filha()
        ```

    - Saída 3:

        ```Python
        função filha
        ```

    - Chamada 4:

        ```Python
        # A classe filha pode chamar e executar a função_pai.
        f.função_pai()
        ```

    - Saída:

        ```Python
        função pai
        ```

### **8.2.2 Herdando apenas os atributos**

- Exemplo:

    ```Python
    class pai:
        def __init__(self,peso,altura,cabelo):
            print('classe pai')
            self.peso = peso
            self.altura = altura
            self.cabelo = cabelo
        def função_pai(self):
            print('função pai')
            print(self.peso, self.altura, self.cabelo)

    # Herda o construtor do pai.
    class filha(pai):
        def __init__(self, peso, altura, cabelo):
            super().__init__(peso,altura,cabelo) # Passa os parâmetros para a classe pai
        def função_filha(self):
            print(self.peso, self.altura, self.cabelo)
            print('função filha')
    ```

    - Chamada 1:

        ```Python
        # Inicia a classe pai.
        p = pai(80,180,'preto')
        ```

    - Saída 1:

        ```Python
        classe pai
        ```

    - Chamada 2:

        ```Python
        # Executa a função_pai
        p.função_pai()
        ```

    - Saída 2:

        ```Python
        função pai
        80 180 preto
        ```

    - Chamada 3:

        ```Python
        # Inicia a classe filha.
        f = filha(20,160,'loiro')
        # Como a filha herdou os atributos de pai, o print da classe pai é quem aparece.
        ```

    - Saída 3:

        ```Python
        classe pai
        ```

    - Chamada 4:

        ```Python
        # Ao adicionar parâmetros diferentes para filha os parâmetros de pai não foram alterados.
        p.função_pai()
        ```

    - Saída 4:

        ```Python
        função pai
        80 180 preto
        ```

    - Chamada 5:

        ```Python
        # Veja que a classe filha possui parâmetros diferentes da classe pai, assim como esperado.
        f.função_filha()
        ```

    - Saída 5:

        ```Python
        20 160 loiro
        função filha
        ```

    - Chamada 6:

        ```Python
        # Se executarmos a função_pai apartir da filha, aparecerão os parâmetros da filha.
        f.função_pai()
        ```

    - Saída 6:

        ```Python
        função pai
        20 160 loiro
        ``` 

> OBS.: Quando houver apenas uma classe superior, utilize o super para fazer a herança do construtor.


### **8.2.3 Herança múltipla**

- Exemplo:

    ```Python
    class pai:
        def __init__(self):
            print('classe pai')
        def função_pai(self):
            print('função pai')

    class mãe:
        def __init__(self):
            print('classe mãe')
        def função_mãe(self):
            print('função mãe')

    class filha(pai,mãe):
        def __init__(self):
            print('classe filha')
            pai.__init__(self)
            mãe.__init__(self)
            #com super().__init__() ele herdaria os atributos somente de primeira classe.
    ```

    - Chamada 1:

        ```Python
        f = filha()
        ```

    - Saída 1:

        ```Python
        classe filha
        classe pai
        classe mãe
        ```

    - Chamada 2:

        ```Python
        f.função_pai()  
        ```

    - Saída 2:

        ```Python
        função pai
        ```

    - Chamada 3:

        ```Python
        f.função_mãe()
        ```

    - Saída 3:

        ```Python
        função mãe
        ```

### **8.2.4 Herança com superposição**

Aqui teremos uma classe filha substituindo um método da classe pai.

- Exemplo:

    ```Python
    class pai:
        def __init__(self):
            print('classe pai')
        def função_pai(self):
            print('função pai')
        def teste_de_superposição(self):
            print('teste pai')
            
    # Coloque o mesmo nome para a função em questão, tanto na classe pai como na filha.
    class filha(pai):
        def __init__(self):
            print('classe filha')
        def teste_de_superposição(self):
            print('teste filha')
    ```

    - Chamada 1:

        ```Python
        p = pai()
        ```

    - Saída 1:

        ```Python
        classe pai
        ```

    - Chamada 2:

        ```Python
        f = filha()
        ```

    - Saída 2:

        ```Python
        classe filha
        ```

    - Chamada 3:

        ```Python
        p.função_pai()
        ```

    - Saída 3:

        ```Python
        função pai
        ```

    - Chamada 4:

        ```Python
        p.teste_de_superposição()
        ```

    - Saída 4:

        ```Python
        teste pai
        ```

    - Chamada 5:

        ```Python
        f.função_pai()
        ```

    - Saída 5:

        ```Python
        função pai
        ```

    - Chamada 6:

        ```Python
        # Note que agora a função mesmo existindo na classe pai, não exibe o print que se encontra lá.
        f.teste_de_superposição()
        ```

    - Saída 6:

        ```Python
        teste filha
        ```