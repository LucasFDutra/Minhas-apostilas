# Basico de Como Usar o GitHub Via Terminal e Atom

Autor: Lucas Felipe Dutra

# Sumário

- [1. CRIANDO UMA CONTA](#1-criando-uma-conta)
- [2. CRIANDO UM REPOSITÓRIO](#2-criando-um-repositório)
- [3. SUBINDO ARQUIVOS PARA O REPOSITÓRIO](#3-subindo-arquivos-para-o-repositório)
- [4. BAIXANDO ARQUIVOS DO GITHUB](#4-baixando-arquivos-do-github)
- [5. EXCLUINDO REPOSITÓRIO](#5-excluindo-repositório)
- [6. UTILIZANDO O GITHUB PELO ATOM](#6-utilizando-o-github-pelo-atom)

# 1. CRIANDO UMA CONTA

Para criar uma conta no GitHub basta você acessar o [link](https://github.com/) Preencha os campos, e clique em `Sign up for GitHub` e siga em frente.

<img src = 'https://github.com/LucasFDutra/Minhas-apostilas/blob/master/GitHub/Imagens/Figura%201.png?raw=true' title = 'Figura 1'>

# 2. CRIANDO UM REPOSITÓRIO

Seguiremos um exemplo durante o tutorial utilizando um repositório chamado `teste`.

- **2.1** - Para criar um repositório no GitHub, você deve clicar no botão `New repository`.

<img src = 'https://github.com/LucasFDutra/Minhas-apostilas/blob/master/GitHub/Imagens/Figura%202.png?raw=true' title = 'Figura 2'>

- **2.2** - Agora você irá colocar o nome do seu repositório e depois clique no botão `Create repository`.

<img src = 'https://github.com/LucasFDutra/Minhas-apostilas/blob/master/GitHub/Imagens/Figura%203.png?raw=true' title = 'Figura 3'>

# 3. SUBINDO ARQUIVOS PARA O REPOSITÓRIO

- **3.1** - Após criar o repositório, copie o URL que se encontra no local indicado na figura.

<img src = 'https://github.com/LucasFDutra/Minhas-apostilas/blob/master/GitHub/Imagens/Figura%204.png?raw=true' title = 'Figura 4'>

- **3.2** - Abra o terminal, navegue até o diretório em que o repositório será clonado e clone o repositório com o comando: `git clone <url>`
  - Pelo exemplo utilizado, o comando no terminal será: `git clone https://github.com/LucasFDutra/lecture0.git`

* **3.3** - Crie um arquivo nessa pasta, no caso irei criar um programa em Python que gera uma lista de número de 0 a 10, e nomearei esse arquivo como lecture0.py.

<img src = 'https://github.com/LucasFDutra/Minhas-apostilas/blob/master/GitHub/Imagens/Figura%205.png?raw=true' title = 'Figura 5'>

- **3.4** - Para subir esse arquivo para o repositório no GitHub, precisamos avisá-lo que queremos comitar algum arquivo, logo iremos direcionar o terminal para o local desse arquivo e adicioná-lo a lista, para isso iremos dar o seguinte comando: `git add <nome do arquivo>`
  - Assim, seguindo o exemplo em questão: `git add lecture0.py`

> **OBS.:** Se quiser adicionar tudo que tem na pasta, digite: `git add -A`.

- **3.5** - Para dar o commit de o seguinte comando: `git commit -m “mensagem”`
  - Essa mensagem é obrigatória, o objetivo dela é garantir que fique mais fácil de identificar as versões do projeto.
  - Seguindo com o exemplo: `git commit -m “este é o primeiro commit”`

* **3.6** - Agora sim, para enviar o arquivo para o GitHub de o comando: `git push`
  E como podemos ver na figura, o arquivo agora se encontra no repositório.

<img src = 'https://github.com/LucasFDutra/Minhas-apostilas/blob/master/GitHub/Imagens/Figura%206.png?raw=true' title = 'Figura 6'>

# 4. BAIXANDO ARQUIVOS DO GITHUB

- **4.1** - Direcione o terminal para a pasta em seu computador que seja referente ao repositório.

* **4.2** - O comando para baixar o arquivo do github é: `git pull`

# 5. EXCLUINDO REPOSITÓRIO

- **5.1** - Na página do GitHub, vá até o repositório que deseja excluir. E clique em `Settings`.

<img src = 'https://github.com/LucasFDutra/Minhas-apostilas/blob/master/GitHub/Imagens/Figura%207.png?raw=true' title = 'Figura 7'>

- **5.2** - Rolando a página para baixo, você encontrará a `Danger Zone`. Clique em `Delete this repository` e siga o que é pedido.

<img src = 'https://github.com/LucasFDutra/Minhas-apostilas/blob/master/GitHub/Imagens/Figura%208.png?raw=true' title = 'Figura 8'>

# 6. UTILIZANDO O GITHUB PELO ATOM

Ao manipular um repositório vai [Atom](https://atom.io/), podemos coordenar não somente arquivos de código que foram editados nele, mas também qualquer arquivo que tenha sido editado em outra plataforma. Ou seja, com o Atom é possível manipular o repositório assim como todo client do GitHub.

- **6.1** - Crie um repositório conforme o _tópico 2_, e copie o URL conforme identificado na figura 4 no tópico 3.1.

* **6.2** - Abra o Atom e pressione `Ctrl+shift+p` para abir a barra de comandos e digite ocomando `GitHub: Clone`. A Janela da figura irá se abrir, e nela cole o URL do repositório, e escolha o diretório em que esse repositório ficará em seu computador clique em `Clone`.

<img src = 'https://github.com/LucasFDutra/Minhas-apostilas/blob/master/GitHub/Imagens/Figura%209.png?raw=true' title = 'Figura 9'>

- **6.3** - Modifique essa pasta conforme sua vontade. Abra o menu `git` na barra inferior, conforme indicado na figura.

<img src = 'https://github.com/LucasFDutra/Minhas-apostilas/blob/master/GitHub/Imagens/Figura%2010.png?raw=true' title = 'Figura 10'>

- **6.4** - De um duplo clique nos arquivos que deseja comitar ou clique em `Stage All`. Seja como escolher, preencha uma mensagem de commit e após commitar, clique em `push`, como indicado nas figuras.

<img src = 'https://github.com/LucasFDutra/Minhas-apostilas/blob/master/GitHub/Imagens/Figura%2011.png?raw=true' title = 'Figura 11' width=350 height=250>
<img src = 'https://github.com/LucasFDutra/Minhas-apostilas/blob/master/GitHub/Imagens/Figura%2012.png?raw=true' title = 'Figura 12'>

> **OBS.:** Porque fazer um novo Branch? Bom, o master é o seu projeto final, é aquele que aparece para ser baixado. Logo quando ainda está na fase de transição entre uma versão do software e próxima, deve-se comitar em outros branchs. A utilização deles também é necessária em projetos comunitários, pois quando uma pessoa modifica algo no código é conveniente que mais alguém avalie esse código antes de incorporá-lo no código master.

- **6.6** - Após fazer o commit em um outro branch pode-se ver no repositório, via navegador:

<img src = 'https://github.com/LucasFDutra/Minhas-apostilas/blob/master/GitHub/Imagens/Figura%2015.png?raw=true' title = 'Figura 15'>

Clicando em `Compare & pull request`, e descendo na tela, teremos uma visão online do que foi modificado entre as versões no novo Branch e a versão no master.

<img src = 'https://github.com/LucasFDutra/Minhas-apostilas/blob/master/GitHub/Imagens/Figura%2016.png?raw=true' title = 'Figura 16'>

Aqui vemos que a linha 10 em que continha o comando `print(‘oi’)` foi apagada e no seu lugar veio o comando `print(‘tchau’)`.

Se subirmos novamente veremos um botão `Create pull request` conforme a 1ª figura, se o pressionarmos veremos o botão `Marge pull request` conforme a 2ª figura.

<img src = 'https://github.com/LucasFDutra/Minhas-apostilas/blob/master/GitHub/Imagens/Figura%2017.png?raw=true' title = 'Figura 17'>
<img src = 'https://github.com/LucasFDutra/Minhas-apostilas/blob/master/GitHub/Imagens/Figura%2018.png?raw=true' title = 'Figura 18'>

Se clicarmos em `Merge pull request` estaremos dizendo ao GitHub que queremos incorporar as modificações ao arquivo master.

> **OBS 1.:** Se você já criou o repositório e vai trabalhar nele em um outro momento, apenas utilize o menu `File/Open folder` para abrir essa pasto em seu computador para que assim seja possível manipular esse repositório via Atom.

> **OBS 2.:** Se houverem modificações externas ao seu computador, ou seja, se outra pessoa trabalhando no projeto fez uma modificação, ou se você modificou algo online, é possível efetuar um pull através do Atom. Ele irá identificar que houveram alterações, e o botão de `pull` ficará no mesmo lugar que o de `push`.
