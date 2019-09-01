# Apostila de NodeJS

Autor: Lucas Felipe Dutra

**ANTES DE QUALQUER COISA, VEJA ESSE VIDEO [AQUI](https://www.youtube.com/watch?v=9w3o9NHXqu0&list=PLMdYygf53DP5Sc6yFYs6ZmjsuuA2fu0TK) PARA APRENDER MAIS SOBRE CLEAN CODE**

# Dicas

- [Curso da rocketseat](https://skylab.rocketseat.com.br)
- [Material de JavaScript](https://github.com/LucasFDutra/Minhas-apostilas/tree/master/JavaScript)

# Sumário

- [**1. INTRODUÇÃO**](#1-introdução)
- [**2. INSTALAÇÃO**](#2-instalação)
    - [**2.1 WINDOWS**](#21-windows)
    - [**2.2 LINUX (UBUNTU E DERIVADOS)**](#22-linux-(ubuntu-e-derivados))
    - [**2.3 LINUX (TODOS OS SISTEMAS)**](#23-linux-(todos-os-sistemas))
    - [**2.4 CONFIGURANDO VSCODE**](#24-configurando-vscode)
- [**3. INICIANDO APLICAÇÃO**](#3-iniciando-aplicação)
- [**4. EXPRESS**](#4-express)
- [**5. ROTAS**](#5-rotas)
- [**6. NODEMON**](#6-nodemon)
- [**7. MONGODB**](#7-mongodb)
    - [7.1 SEGURANÇA](#71-segurança)
    - [7.2 MONGODB COMPASS](#72-mongodb-compass)
- [**8. MODEL**](#8-model)
        - [8.1 VÁRIOS MODELS](#81-vários-models)
- [**9. COMUNICANDO COM BANCO DE DADOS**](#9-comunicando-com-banco-de-dados)
    - [9.1 CONTROLLER](#91-controller)
    - [9.2 ROUTES](#92-routes)
    - [9.3 SERVER.JS](#93-serverjs)
- [**10. REPASSANDO**](#10-repassando)
- [**11. INSOMNIA**](#11-insomnia)
    - [11.1 INSTALAÇÃO](#111-instalação)
    - [11.2 UTILIZAÇÃO](#112-utilização)
    - [11.3 OTIMIZANDO A UTILIZAÇÃO](#113-otimizando-a-utilização)
- [**12. CRUD**](#12-crud)
    - [12.1 CREATE](#121-create)
        - [**12.1.1 Controller**](#1211-controller)
        - [**12.1.2 Routes**](#1212-routes)
        - [**12.1.3 Server**](#1213-server)
        - [**12.1.4 Insomnia**](#1214-insomnia)
    - [12.2 READ](#122-read)
        - [**12.2.1 Controller**](#1221-controller)
        - [**12.2.2 Routes**](#1222-routes)
        - [**12.2.3 Insomnia**](#1223-insomnia)
    - [12.3 UPDATE](#123-update)
        - [**12.3.1 Controller**](#1231-controller)
        - [**12.3.2 Routes**](#1232-routes)
        - [**12.3.3 Insomnia**](#1233-insomnia)
    - [12.4 DELETE](#124-delete)
        - [**12.4.1 Controller**](#1241-controller)
        - [**12.4.2 Routes**](#1242-routes)
        - [**12.4.3 Insomnia**](#1243-insomnia)
- [**13. CORS**](#13-cors)
- [**14. RESUMO**](#14-resumo)

# **1. INTRODUÇÃO**

O nodeJS é uma plataforma que utiliza a engine V8 do google chrome, assim permitindo que utilizemos o JavaScript no backend.

# **2. INSTALAÇÃO**

Para trabalhar com o nodeJS no seu computador é preciso fazer a instalação do mesmo.

## **2.1 WINDOWS**

Vá no [site](https://nodejs.org/en/) do node e baixe o instalador e saia dando next

## **2.2 LINUX (UBUNTU E DERIVADOS)**

**Para sistemas da plataforma `deb` exceto linux mint 19.2.**

Se quiser a versão que sua distro disponibiliza, então digite o comando abaixo:

```sh
sudo apt-install nodejs
```

Mas se quiser uma versão mais atualiada da LTS do node (nesse momento a 10.x) utilize os comandos:

```sh
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -

sudo apt-get install -y nodejs
```

Agora para usuários de linux mint 19.2 caso rode os comandos acima, idependente de qual rodar vai baixar a versão 8.10, isso porque o script da versão 10.x não reconhece o sistema ainda, pois ele é muito recente (hoje é dia 15/07/19). Então eu peguei o script do proprio repositorio do node e modifiquei (onde estava escrito "tara" coloquei "tina") e subi o arquivo para esse repositório, então baixe ele e apenas rode os seguintes comando:

```sh
sudo ./setup_10.x

sudo apt-get install -y nodejs
```

> OBS.: Juntamente com o node vem o npm, que é um gerenciador de pacotes para node. Porém com esse comando ambos vêm um pouco desatualizados dependendo da sua distro, pois ele puxa direto do repositório da mesma.

Para ver se o node e o npm foram instalados corretamente utilize os comandos abaixo:

```sh
node --version

npm --version
```

as respostas devem ser respectivametne `v10.16.3` e `6.9.0`

## **2.3 LINUX (TODOS OS SISTEMAS)**

Veja maiores informações sobre o node para linux [aqui](https://github.com/nodesource/distributions/blob/master/README.md). Você encontra como instalar o node no seu pc (esse link veio a partir do site oficial do node na aba downloads)

## **2.4 CONFIGURANDO [VSCODE](HTTPS://CODE.VISUALSTUDIO.COM/)**

Recomendo utilizar o Visual studio code para programar, porém sinta-se a vontade para utilizar o que preferir, mas caso escolha trabalhar com o vscode, então baixe as extensões

- `ESLint` para deixar o código mais bonito e corrigir erros
- `Node Exec` para executar os códigos js precionando F8.

Caso queira dar uma olhada nesse link [aqui](https://blog.rocketseat.com.br/ambiente-desenvolvimento-javascript/). É do pessoal da rocketseat mostrando algumas configurações que eles sugerem para fazer no vscode para programar em JS.

Lembrando que assim iremos executar os códigos js na forma de node e não de frontend (browser).

# **3. INICIANDO APLICAÇÃO**

Escolha uma pasta para colocar seu projeto. E com o terminal apontado para essa pasta, execute:

```sh
npm init -y
```

> OBS.: Todos os comandos de terminal apartir de agora devem ser executados dentro da pasta `node-api` ou seja lá como você nomeou seu projeto. (Caso não deva ser executado nessa pasta eu informarei).

Esse comando criou um arquivo chamado `package.json`. Esse arquivo por enquanto está apenas com as informações do projeto, como por exemplo nome, versão, descrição, e outras coisas. Mas será nele que iremos colocar quais serão as nossas dependências e suas versões (as bibliotecas utilizadas).

No meu caso, criei uma aplicação de exemplo chamada [`node-api`](https://github.com/LucasFDutra/Minhas-apostilas/tree/master/NodeJS/node-api)

- A árvore de diretórios nesse momento fica:
  ```sh
  └── package.json
  ```

> Se gostou dessa representação de árvores de diretórios, abra seu terminal e instale o `tree` com `sudo apt install tree` depois vá para o diretório em que quer exibir a árvore e execute o comando `tree` e veja o resultado. No caso eu copiei e colei ele aqui entre o bloco gerado por ``` que a liguagem markdown me fornece.

# **4. EXPRESS**

O `express` é um micro framwork que vai nos auxiliar a trabalhar com rotas (endereços que podem ser acessados na api) e views (formas de visualização).

> OBS.: As views não são utilizadas quando se trabalha com API rest (API rest é quando o backend e o frontend são completamente separados mas claro que isso é uma explicação bem rasa, então se quiser aprofundar mais clique [aqui](https://www.youtube.com/watch?v=ghTrp1x_1As)).

Para instalar o express, abra o terminal e digite

```sh
sudo npm install express
```

Se for no arquivo `package.json` você verá que foi adicionada uma nova propriedade, de dependências na qual está o `express`.

> OBS.: Ao instalar um modulo, uma pasta chamada `node_modules` será criada, nela estarão o express e as dependências que ele precisa para funcionar.

Agora crie um arquivo `.js` que será o arquivo principal da aplicação, no meu caso será `server.js`.

- A árvore de diretórios nesse momento fica:

  ```sh
  ├── node_modules
  ├── package.json
  └── server.js
  ```

E dentro dele vamos colocar as seguintes linhas de código:

```JavaScript
const express = require("express")
```

O código acima mostra uma certa difença do modo usual de importar bibliotecas que o js tem. Quando estamos utilizando o node, vamos importar bibliotecas com essa estrutura.

```JavaScript
const variavel = require("biblioteca")
```

Note que se a biblioteca em questão estiver dentro de `node_modules` então a importação acontece igual ao que fizemos para o `express`, porém se a biblioteca for um arquivo criado pelo usuário e que esteja em outro diretório, então deve-se especificar o caminho do arquivo. Exemplo:

```JavaScript
const variavel = require("./libs/biblioteca.js")
```

Agora que temos o express na aplicação, para trabalhar com ele, vamos atribuir uma variável a ele

> OBS.: Pra quem manja de poo, esse negocio que vou fazer agora parece muito com a instanciação de um objeto. E pode usar essa analogia ai que vai dar certo - eu mesmo estou usando isso pra poder entender melhor.

```JavaScript
const express = require("express");

const app = express();

app.listen(3001);
```

O comando listen, faz com que a aplicação fique ouvindo a porta 3001 do nosso pc, então se abrirmos o browser nesse porta nos conseguiremos ver os retornos da nossa api. Abaixo vamos fazer exatamente isso.

Rode esse código digitando no teminal `node server.js` ele ficará esperando algo acontecer, dai abra seu browser e digite o endereço `http://localhost:3001/`

Mas não vai ter nada lá alem de um `Cannot GET /`, afinal a aplicação ainda não possui nenhuma tratativa de rotas.

# **5. ROTAS**

Para trabalhar com as rotas, precisamos utilizar o comando

```JavaScript
app.get("local", (req, res) => {/*função*/});
```

- `local`: é para onde a nossa aplicação irá, no caso se eu quiser que ela vá para a raiz, eu coloco `"/"`, mas por exemplo, eu poderia mandar ela para: `http://localhost:3001/teste`. Assim eu colocaria `"/teste"`

- req: contém todos os detalhes e informações de uma requisição feita ao servidor.

  - Por exemplo:
    - Parâmetros;
    - Corpo da requisição;
    - Cabeçalho;
    - Usuário;
    - Autenticação;
    - etc.

- res: contém a resposta que receberemos de acordo com a requisição

Tanto o req quanto o res possuem métodos, e eles serão explorados durante esse material. 

Por exemplo, podemos utilizar o método `send` para retornar algo como resposta.

```JavaScript
app.get("local", (req, res) => {
    res.send("Hello World");
});
```

Fazendo essa modificação no nosso arquivo server.js, ele ficará da seguinte forma:

- Arquivo `server.js`

  ```JavaScript
  const express = require("express");

  const app = express();

  app.get("/", (req, res) => {
    res.send("Hello World");
  });

  app.listen(3001);
  ```

E reexecutando o comando `node server.js` e abrindo o browser na porta `3001` bem na home (`"/"`) teremos a mensagem `'Hello World'` aparecendo.

> SUGESTÃO: Mude de `"/"` para `"/teste"` e coloque no browser `http://localhost:3001/teste` para ver o resultado. Será bom para entender como funcionam esses comandos de rota.

Se você seguiu a sugestão deve ter entendido que basicamente vamos usar o `get` para executar alguma coisa de acordo com a pagina que o usuário estiver acessando.

# **6. NODEMON**

Como já deve ter notado, não é legal ficar tendo que reiniciar o servidor a cada modificação feita, então é muito interessante que exista uma ferramenta para fazer tal tarefa automaticamente para gente. Assim a aplicação ficaria no modo live reload. E para isso mesmo que existe o `nodemon`.

Instale o mesmo dando o comando abaixo no terminal:

```sh
sudo npm install -D nodemon
```

> OBS.: O `-D` é para instalar como desenvolvedor, isso faz com que a dependência fique separada das outras, afinal ela é apenas para o ambiente de desenvolvimento. Afinal live reload não é necessário para a aplicação além do momento em que ela está sendo desenvolvida.

Agora para executar o nodemon, abra o arquivo `package.json` e insira a linha abaixo dentro dos scripts.

```JavaScript
{...
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "dev": "nodemon server.js"
  },
  ...
}
```

> OBS.: Não esqueça de por uma virguila na linha anterior. E server.js é aquele arquivo principal, e o nome "dev" pode ser substituido, mas mantenha a auteração nos proximos passos.

Ai agora quando for executar o servidor, não faremos mais `node server.js`. Agora faremos:

```sh
npm run dev
```

Agora sempre que modificar algo no código da aplicação e salvar o nodemon irá reiniciar o servidor automaticamente.

Sendo assim abra ai um terminal e deixe só para ele.

> OBS.: Ainda é necessário dar F5 na página do browser.

# **7. MONGODB**

Baixe a versão gratuita do banco de dados chamada mongoDB atlas, que pode ser encontrado [aqui](https://www.mongodb.com/cloud/atlas)

- Clique em `try free` e crie uma conta

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_01.png?raw=true)

- Você vai cair nessa tela aqui

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_02.png?raw=true)

- Role tudo para baixo e clique em `create cluster` (note que temos 512mb gratuitos para utilizarmos)

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_03.png?raw=true)

- Depois vai cair nessa tela abaixo e isso pode demorar um tempo

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_04.png?raw=true)

- Depois de criado vá em `Database Access` para criar um usuário e senha

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_05.png?raw=true)

- Vá em `add new user`

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_06.png?raw=true)

- Crie o usuário, e deixe marcada a opção `Read and write to any database` e adicione o usuário

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_07.png?raw=true)

- Vá em `network access`

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_08.png?raw=true)

- Crie um novo acesso em `add ip address` e depois permita que esse banco de dados seja acessado de qualquer lugar clicando em `Allow access from anywhere`

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_09.png?raw=true)

- Vá em `clusters` e clique em `connect`

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_10.png?raw=true)

- Selecione a opção `connect to your application`

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_11.png?raw=true)

- Agora deixe a tela seguinte com a configuração mostrada abaixo e clique em `copy`

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_12.png?raw=true)

- Agora abra o terminal e instale o `mongoose` com o comando

  ```sh
  sudo npm install mongoose
  ```

O mongoose vai permitir que nos comuniquemos com o banco de dados utilizando apenas sintax javascrip. Isso faz com que não precisemos utilizar aqueles comando `INSERT, INTO..` que os bancos de dados precisam

Agora vamos importar o mongoose para o arquivo sever.js com a linha

```JavaScript
const mongoose = require("mongoose");
```

E antes das rotas coloque o seguinte comando:

```JavaScript
mongoose.connect('url de conexão', {useNewUrlParser: true});
```

A url de conexão é aquela que pegamos do mongoDB ao clicar em `copy`. Assim nosso código ficará da seguinte forma:

- Arquivo `server.js`
  ```JavaScript
  const express = require("express");
  const mongoose = require("mongoose");

  // Iniciando o APP
  const app = express();

  // Iniciando o DB
  mongoose.connect(
    "mongodb+srv://lucasdatabase:lucasdatabase@cluster0-mtkkw.mongodb.net/test?retryWrites=true&w=majority",
    {
      useNewUrlParser: true
    }
  );

  // Primeira rota
  app.get("/", (req, res) => {
    res.send("Hello World");
  });

  app.listen(3001);
  ```

> OBS.: É que provavelmente você terá recebido esse url com `<username>` e `<password>` é só trocar pelo username e o password que você definiu no passo de criação da base de dados (lembre de retirar o sinal de <> também, veja meu exemplo).

> OBS.: O parametro `test` que está nessa url é o nome da tabela do banco de dados, porém se trocar esse nome e colocar qualquer outra coisa ele simplesmente criará esse novo banco de dados para você. Mas pode deixar teste mesmo.

> OBS.: O comando `useNewUrlParser` é para o mongoose identificar que estaremos utilizando o novo formato de url (evita um warning).

Pronto, nossa conexão com o banco de dados está feita.

## 7.1 SEGURANÇA

Esse banco de dados será deletado, por isso deixei a senha e username à mostra aqui, porém você não quer que o seu fique dessa forma, sendo assim o um jeito de proteger sua aplicação é colocar esse link de acesso em um arquivo `.json` (no caso criei um arquivo chamado `credentials.json`), e puxar a informação dele. E para evitar que esse arquivo suba para o github, coloque esse arquivo dentro do `.gitignore` para assim a url de acesso não ficar à mostra para o mundo (caso não tenha um arquivo `.gitignore` basta criar um dentro da pasta do projeto, veja árvore abaixo).

- A árvore de diretórios nesse momento fica:

  ```sh
  ├── credentials.json
  ├── node_modules
  ├── .gitignore
  ├── package.json
  └── server.js
  ```

- Arquivo `credentials.json`

  ```JavaScript
  {
      "mongoUrl": "mongodb+srv://lucasdatabase:lucasdatabase@cluster0-mtkkw.mongodb.net/test?retryWrites=true&w=majority"
  }
  ```

- Arquivo `server.js`

  ```JavaScript
  const express = require("express");
  const mongoose = require("mongoose");
  const mongoUrl = require("./credentials.json");

  // Iniciando o APP
  const app = express();

  // Iniciando o DB
  mongoose.connect(mongoUrl.mongoUrl, {
    useNewUrlParser: true
  });

  // Primeira rota
  app.get("/", (req, res) => {
    res.send("Hello World");
  });

  app.listen(3001);
  ```

- Arquivo `.gitignore`

  ```sh
  # credentials
  credentials.json
  ```

> OBS.: Essa mesma tecnica é utilizada para colocar apiKey, afinal essas keys também não são coisas que você quer por ai soltas.

## 7.2 MONGODB COMPASS

Se quiser verificar o que está acontecendo no seu banco de dados, de uma forma mais fácil do que ficar acessando o site do mongoDB, utilize o mongoDB compass, que é uma interface que irá trazer as informações do seu banco. Para baixar o mongodb compass community clique [aqui](https://www.mongodb.com/products/compass).

- Agora é só clicar em `try now`

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_13.png?raw=true)

- Clique em `tools` escolha a melhor versão para você e clique em `download`

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_14.png?raw=true)

- Agora abra o `mongoDB compass community` e depois vá no `mongoDB Atlas` (onde configurou seu banco de dados) e vá em cluster e clic em `connect` novamente e depois escolha a opção `connect with mongoDB compass`

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_15.png?raw=true)

- Ai você clica em `copy`

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_16.png?raw=true)

- Volte para o `mongoDB compass` e ele automaticamente identificará que existe uma url copiada e perguntará se quer importar ela para dentro da aplicação. Clique em sim

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_17.png?raw=true)

- Coloque o `username` e o `password` conforme havia configurado antes, e em `Autentication Database` coloque `admin`. E clique em `connect`.

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_18.png?raw=true)

> OBS.: Talves você veja a tabela que criou, ou talvez não, pois ainda não colocou nada nela.

# **8. MODEL**

O model representa uma tabela no banco de dados.

Crie dentro da pasta do projeto uma pasta chamada `src` e dentro da mesma crie uma pasta chamada `models`.

> OBS.: Claro que os nomes são opcionais, mas eles fazem sentido no mundo da programação, então meio que por convenção coloque esses nomes.

Agora, vamos criar dentro dessa pasta um arquivo `.js` que será nosso arquivo `model`. Coloque o nome dele de acordo com a url que você quer usar para chegar nele. Ou seja, se a aplicação fosse para utilizar cadastros de desenvolvedore, você poderia utilizar `Dev.js`, mas se fosse uma loja e quisessemos que esse url levasse aos produtos, iriamos colocar `Product.js`

- A árvore de diretórios nesse momento fica:

  ```sh
  ├── credentials.json
  ├── node_modules
  ├── package.json
  ├── server.js
  └── src
      └── models
          └── Products.js
  ```

> OBS.: Para seguir com o exemplo que estou estudando irei criar um arquivo chamado `Product.js`. Mas para utilizar de exemplo aqui eu sempre chamarei de `NomeDoModel`

Dentro de `Product.js` deve-se importar duas coisas do mongoose, o `Schema` e o `model`, para isso digite a seguinte linha:

```JavaScript
const { Schema, model } = require('mongoose')
```

Agora vamos criar a estrutura do nosso banco de dados, ou seja o esquema dele. Que é trazido da seguinte forma:

- Arquivo `NomeDoModel.js`

  ```Java
  const NomeDoSchema = new Schema(
    // registros que nossa base de dados irá receber
    {
      campo_1: {
        type: tipo_de_dados, // String, Integer, Array
        required: true_or_false // caso true -> obrigatorio de existir, caso false -> Opcional
      },
      campo_2: {
        type: tipo_de_dados,
        required: true_or_false
      }
    },
    // timestamps
    {
      timestamps: true
    }
  );

  module.exports = model('NomeDoModelo', NomeDoSchema); // exportar o esquema
  ```

O `timestamps` serve para gerar automaticamente duas colunas para nós, uma chamada `createdAt` e outra chamada `updatedAt` em cada registro da base de dados.

- `createdAt`: Armazena a data de criação de cada registro
- `updatedAt`: Armazena a data da ultima alteração do registro

Considerando o meu exemplo, o código fica:

- Arquivo `Project.js`

  ```JavaScript
  const { Schema, model } = require("mongoose");

  const ProductSchema = new Schema(
    {
      title: {
        type: String,
        required: true
      },
      description: {
        type: String,
        required: true
      },
      url: {
        type: String,
        required: true
      }
    },
    {
      timestamps: true
    }
  );

  module.exports = model("Product", ProductSchema);
  ```

Agora vá para dentro do arquivo server.js e faça a requisição do modulo. Para isso, coloque o comando abaixo da linha de conexão com o banco de dados (é impressindível que isso esteja depois da conexão).

```JavaScript
// Puxando os modulos
require('./src/models/NomeDoModel')
```

No meu exemplo fica assim:

```JavaScript
// Iniciando o DB
mongoose.connect(mongoUrl.mongoUrl, {
  useNewUrlParser: true
});

// Puxando os modulos
require('./src/models/Product')
```

### 8.1 VÁRIOS MODELS

Caso você tenha muitos modelos, não fica legal ficar dando `require` em todos eles, vai ficar umas 20 linhas só de require. Para melhorar isso utilize uma biblioteca chamada `require-dir` que faz a rquisição de tudo que está dentro de um diretório.

Instale a biblioteca:

```sh
sudo npm install require-dir
```

Importe ela para sua aplicação dentro de onde vai fazer essas requisições (no nosso caso dentro de server.js).

```JavaScript
const requireDir = require("require-dir");

// iniciando app
// iniciando banco
// requerindo modulos
requireDir('./src/models');
```

Agora para adicionar algo basta definir um `"objeto"` para o modelo

```JavaScript
const NomeDoModel = mongoose.model("NomeDoModel");
```

E dentro da nossa rota podemos mandar colocar algo dentro do banco utilizando o comando

```JavaScript
NomeDoModel.create({
  // passe o objeto de acordo com o schema criado
})
```

Seguindo o meu exemplo, podemos fazer da seguinte maneira:

```JavaScript
// Iniciando o APP
// Iniciando o DB
// Puxando os models

// Iniciando model
const Product = mongoose.model("Product");

// Primeira rota
app.get("/", (req, res) => {
  Product.create({
    title: "React Native",
    description: "Build native apps with React",
    url: "http://github.com/facebook/react-native"
  });

  return res.send("Hello World"); //ta aqui atoa
});
```

Se você for no mongoDB compass você verá que foi criada uma tabela com esses dados (recarregue o mongoDB compass, as vezes ele não atulizou).

# **9. COMUNICANDO COM BANCO DE DADOS**

Para melhorar a forma de como são feitas as requisições ao banco de dados, vamos criar duas coisas. As rotas, e os controladores.

As rotas tem por responsabilidade definir para onde o código vai de acordo com a url que temos.

Os controladores serão aqueles que executarão as tarefas no banco de dados, ou seja, inserção, exclusão, troca, etc.

## 9.1 CONTROLLER

Crie dentro da pasta `src` uma pasta chamada `controllers` e crie um arquivo para ser um controlador.

Um controlador pode controlar qualquer coisa, por exemplo, o seu model precisará de um controlador, afinal o controlador de um model irá fazer as requisições no banco de dados. Porém, se sua aplicação executar uma determinada tarefa que exija um processamento do backend, esse processamento será feito em um outro model.

Essa segmentação de controllers auxilia na distribuição de responsabilidades, e mantém o código mais organizado, sendo assim seu código ficará mais simples de ser entendido e de receber manutenção (e isso é muito importante).

Como por hora temos apenas um model, então crie um arquivo chamado `NomeDoModelController.js`, seguindo o exemplo terei um arquivo chamado `ProductController.js`.

- A árvore de diretórios nesse momento fica:
  ```sh
  ├── credentials.json
  ├── node_modules
  ├── package.json
  ├── server.js
  └── src
      ├── controllers
      │   └── ProductController.js
      └── models
          └── Products.js
  ```

A estrutura de um controller é composta basicamente de um objeto, que será exportado, abaixo temos o esqueleto básico de um controller:

```JavaScript
const NomeDoModel = require('../models/NomeDoModel')

module.exports = {
    // métodos
  }
}
```

Outro jeito de fazer um controller, seria com a estrutura abaixo

```JavaScript
const mongoose = require('mongoose');
const NomeDoModel = mongoose.model('NomeDoModel')

module.exports = {
    // métodos
  }
}
```

A diferença entre os dois é que no primeiro caso você não importa o mongoose diretamente, pois você importa o NomeDoModel, e lá já temos o mongoose, porém se você tentar utilizar o mongoose para alguma coisa nessa abordagem, não vai funcionar (utilizar o mongoose dentreo do arquivo controller). Já a segunda nos pegamos o modelo através da busca por modelos que o mongoose faz. Lembre-se de que quando criamos o modelo nos fizemos:

```JavaScript
module.exports = model("NomeDoModel", NomeDoModelSchema);
```

Ou seja, aqui nós jogamos o NomeDoModel para o nosso programa como sendo um model. Logo o mongoose consegue pegar ele quando damos o comando.

```JavaScript
const NomeDoModel = mongoose.model('NomeDoModel')
```

Ou seja, a escolha de como fazer isso vai de aplicação para aplicação, mas no final das contas não importa muito, afinal você pode fazer, sem nenhum problema o seguinte:

```JavaScript
const mongoose = require('mongoose');
const NomeDoModel = require('../models/NomeDoModel')

module.exports = {
    // métodos
  }
}
```

O que na minha opnião faz mais sentido, e é o que vou utilizar caso precise utilizar o mongoose dentro do arquivo de controle.

Mais para frente vou trazer alguns métodos possíveis para aplicarmos ao nosso modelo, ou seja, inserção, remoção... Mas agora já trarei um método para poder mostrar que está tudo funcionando.

Vou utilizar o método `find` que basicamente trará para nós o que está dentro do banco de dados, o que convenhamos é muito útil, e na verdade é o inicio de toda aplicação que utiliza banco de dados. No caso eu mostrarei como fica o arquivo `ProductController.js`

- Arquivo `ProductController.js`

  ```JavaScript
  const Product = require("../models/Product");

  module.exports = {
    async index(req, res) {
      const products = await Product.find();

      return res.json(products);
    }
  };
  ```

Caso não saiba o que é o `async/await`, veja o meu material de javaScript, mas dando um resumo o `async` indica que a função é assincrona (isso acontece porque o método find é assincrono, e se ele está dentro da função então é claro que ela também será assincrona) e o método `await` faz com que esperemos o retorno do método `find` para ai sim seguir com o código, que nesse caso retorna `products` (que é o que está dentro da nossa base de dados) em formato `json`.

> OBS.: ainda não tente abrir nada no seu navegador, pois sem ajustar o arquivo `server.js` e sem criar o arquivos de rotas não vai acontecer nada.

## 9.2 ROUTES

Dentro da pasta src crie um arquivo chamado `routes.js`.

Para te ajudar, até agora a nossa estrutura de arquivos é a seguinte:

```sh
├── credentials.json
├── node_modules
├── package.json
├── package-lock.json
├── server.js
└── src
    ├── controllers
    │   └── ProductController.js
    ├── models
    │   └── Product.js
    └── routes.js
```

A estrutura de um arquivo de rotas é bem simples.

```JavaScript
const express = require("express");
const routes = express.Router();

const NomeDoModelController = require("./controllers/NomeDoModelController");

// primeira rota
routes.get("/local", NomeDoModelController.index);
// outras rotas que quiser

module.exports = routes;
```

Aqui o que estamos fazendo é que ao acessarmos o endereço `/local` estaremos executando o método `index` criado no `NomeDoModelController.js`. Ou seja, estaremos recebendo como retorno o json da nossa tabela do banco de dados.

Indo para o exemplo, o arquivo `routes.js` ficará:

- Arquivo `routes.js`

  ```JavaScript
  const express = require("express");
  const routes = express.Router();

  const ProductController = require("./controllers/ProductController");

  // Minha rota
  routes.get("/products", ProductController.index);

  module.exports = routes;
  ```

## 9.3 SERVER.JS

Agora vamos reorganizar o arquivo `server.js` que nesse momento está da seguinte forma:

- Arquivo `server.js`

  ```JavaScript
  const express = require("express");
  const mongoose = require("mongoose");
  const mongoUrl = require("./credentials.json");
  const requireDir = require("require-dir");

  // Iniciando o APP
  const app = express();

  // Iniciando o DB
  mongoose.connect(mongoUrl.mongoUrl, {
    useNewUrlParser: true
  });
  // Puxando os models
  requireDir("./src/models")

  // Iniciando model
  const Product = mongoose.model("Product");

  // Primeira rota
  app.get("/", (req, res) => {
    Product.create({
      title: "React Native",
      description: "Build native apps with React",
      url: "http://github.com/facebook/react-native"
    });

    return res.send("Hello World"); //ta aqui atoa
  });
  ```

Como não queremos mais executar requisições ao banco de dados dentro desse arquivo, podemos retirar o `app.get`, também não precisamos mais puxar e nem iniciar os models. Mas em contra partida precisamos agora inserir nossas rotas. Para isso faremos o seguinte

```JavaScript
const routes = require("./src/routes");
// Iniciando o APP
// Iniciando o DB
// Rotas
app.use("/algumaCoisa", routes);
```

Antes de mostrar o como fica o arquivo `server.js` do exemplo, eu quero explicar a linha `app.use("/algumaCoisa", routes);`.

Dentro do `use` nos vamos passar dois parâmetros, que seriam a url e para onde que essa url irá nos mandar.

Ou seja, quando digitarmos no nosso navegador a url `http://localhost:3001/algumaCoisa` iremos cair dentro das nossas rotas. Mas primeiro quero que você entenda que se eu tivesse passado

```JavaScript
app.use("/teste", routes);
```

iriamos ter que digitar `http://localhost:3001/teste`

E caso eu tivesse passado:

```JavaScript
app.use("/", routes);
```

ou

```JavaScript
app.use(routes);
```

iriamos ter que digitar `http://localhost:3001/`

Sim, passando o `/` ou não passando nada teremos o mesmo efeito.

Agora vamos pensar olhando para as nossas rotas. Afinal podemos pensar como se esse `/algumaCoisa` fosse uma pasta, e que dentro dela temos vários arquivos, e esses arquivos são nossas rotas. Ou seja, vamos supor que temos as seguintes rotas:

```JavaScript
routes.get("/rotaA", ProductController.metodoA);
routes.get("/rotaB", ProductController.metodoB);
routes.get("/rotaC", ProductController.metodoC);
```

Para acessarmos cada uma dessas rotas teriamos que fazer respectivamente:

- Para `/algumaCoisa`

  ```
  http://localhost:3001/algumaCoisa/rotaA
  http://localhost:3001/algumaCoisa/rotaB
  http://localhost:3001/algumaCoisa/rotaC
  ```

- Para `/` ou nada

  ```
  http://localhost:3001/rotaA
  http://localhost:3001/rotaB
  http://localhost:3001/rotaC
  ```

Assim o arquivo `server.js` do exemplo fica com a seguinte cara:

- Arquivo `server.js`

  ```JavaScript
  const express = require("express");
  const mongoose = require("mongoose");
  const mongoUrl = require("./credentials.json");
  const routes = require("./src/routes");

  // Iniciando o APP
  const app = express();

  // Iniciando o DB
  mongoose.connect(mongoUrl.mongoUrl, {
    useNewUrlParser: true
  });

  // Rotas
  app.use("/api", routes);

  app.listen(3001);
  ```

Agora sim. Se você der o comando no terminal (dentro da pasta da aplicação) e abrir o seu navegador no seguinte url: `http://localhost:3001/api/products` e se você fez exatamente como eu quando fiz dentro do arquivo `server.js` nesse passo [aqui](#81-vários-models):

```JavaScript
  app.get("/", (req, res) => {
    Product.create({
      title: "React Native",
      description: "Build native apps with React",
      url: "http://github.com/facebook/react-native"
    });

    return res.send("Hello World"); //ta aqui atoa
  });
```

Você verá:

```JavaScript
[
  {
    _id: "5d688604192c832a6eb6be51",
    title: "React Native",
    description: "Build native apps with React",
    url: "http://github.com/facebook/react-native",
    createdAt: "2019-08-30T02:12:20.405Z",
    updatedAt: "2019-08-30T02:12:20.405Z",
    __v: 0
  }
]
```

> DICA: Se quiser visualizar arquivos json no seu navegador de uma forma mais agradável, eu recomendo instalar essa extensão para chrome [aqui](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc) e a mesma para firefox mozilla [aqui](https://addons.mozilla.org/pt-BR/firefox/addon/jsonview/)

# **10. REPASSANDO**

Caso tenha ficado confuso ou perdido vou repassar aqui rapidamente como as coisas tem que ficar.

- A estrutura de arquivos:

  ```sh
  ├── credentials.json
  ├── node_modules
  ├── package.json
  ├── package-lock.json
  ├── server.js
  └── src
      ├── controllers
      │   └── ProductController.js
      ├── models
      │   └── Product.js
      └── routes.js
  ```

- Instale as dependências:
  ```sh
  sudo npm install express
  sudo npm install require-dir
  sudo npm install -D nodemon
  ```

Adicione o nodemon como devDependencies e adicione o script em package.json

- Arquivo `package.json`

  ```JavaScript
  {
    "name": "node-api",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
      "test": "echo \"Error: no test specified\" && exit 1",
      "dev": "nodemon server.js"
    },
    "keywords": [],
    "author": "",
    "license": "ISC",
    "dependencies": {
      "express": "^4.17.1",
      "require-dir": "^1.2.0"
    },
    "devDependencies": {
      "nodemon": "^1.19.1"
    }
  }
  ```

- Arquivo `server.js`

  ```JavaScript
  const express = require("express");
  const mongoose = require("mongoose");
  const mongoUrl = require("./credentials.json");
  const routes = require("./src/routes");

  // Iniciando o APP
  const app = express();

  // Iniciando o DB
  mongoose.connect(mongoUrl.mongoUrl, {
    useNewUrlParser: true
  });

  // Rotas
  app.use("/api", routes);

  app.listen(3001);
  ```

- Arquvio `routes.js`

  ```JavaScript
  const express = require("express");
  const routes = express.Router();

  const ProductController = require("./controllers/ProductController");

  // Minha rota
  routes.get("/products", ProductController.index);

  module.exports = routes;
  ```

- Arquivo `ProductController.js`

  ```JavaScript
  const Product = require("../models/Product");

  module.exports = {
    async index(req, res) {
      const products = await Product.find();

      return res.json(products);
    }
  };
  ```

- Abra o terminal em `node-api` e digite o comando

  ```sh
  npm run dev
  ```

- Abra o navegador e entre em

  ```
  http://localhost:3001/api/products
  ```

# **11. INSOMNIA**

O insomnia vai nos ajudar a testar as rotas da nossa api. Apesar de já conseguirmos ver a saída no nosso browser, não é o melhor jeito possível, pois ali conseguimos ver basicamente só as rotas get. Não podemos testar rotas post (inserir algo no banco de dados. A gente chega lá).

> OBS.: Nessa seção não vou apresentar tudo que farei com o insomnia logo de cara, até porque nossa aplicação não tem muita coisa no momento. Então vou apenas mostar ele e mostrar o básico de sua utlização, ai nas seções mais seguintes conforme eu for utilizando ele trarei mais conteúdos sobre o mesmo.

## 11.1 INSTALAÇÃO

Digite em seu terminal;

```sh
echo "deb https://dl.bintray.com/getinsomnia/Insomnia /" | sudo tee -a /etc/apt/sources.list.d/insomnia.list

wget --quiet -O - https://insomnia.rest/keys/debian-public.key.asc | sudo apt-key add -

sudo apt-get install insomnia
```

## 11.2 UTILIZAÇÃO

- Dentro do Insomnia vá em `Insomnia -> create new workspace` de um nome pra ela.

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_20.png?raw=true)

- De um nome para esse workspace

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_21.png?raw=true)

- Agora do lado esquerdo veja que apareceu um botão com um +, clique nele e clique em `new request`.

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_22.png?raw=true)

- Clique em `GET` para ver os tipos de rotas que podemos escolher.

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_24.png?raw=true)

- Para saber qual tipo de rota você deve escolher veja de qual tipo dela no arquivo `routes.js`

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_25.png?raw=true)

> Veja que nesse caso do exemplo, temos uma rota do tipo `get`, logo iremos utilizar o `GET` no insomnia

- Agora depois de definido o nome, e o tipo, clique em `Create`

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_26.png?raw=true)

- Agora copie a url da rota a ser observada conforme a figura abaixo e clique em `Send`:

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_27.png?raw=true)

- Agora se tudo tiver dado certo, você verá a seguinte resposta:

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_28.png?raw=true)

## 11.3 OTIMIZANDO A UTILIZAÇÃO

Como você bem deve imaginar, nos não iremos monitorar apenas essa rota, iremos ver várias, dependendo do projeto podem ser dezenas. Mas em todas elas o modo criar o monitoramento é igual, e em todas elas precisaremos digitar a mesma url variando apenas a ultima rota. Ou seja, `http://localhost:3001/api` é sempre uma constante na aplicação. Sem falar caso nós mudarmos a nossa url (se deixar de ser localhost por exemplo) fica meio complicado de sairmos mudando em todos os arquivos, então é mais interessante que esteja salvo em algum lugar que essa parte é constante e depois nos mudamos somente nesse lugar (exatamente o mesmo principio do porque utilizar variáveis em alguma linguagem de programação, você atribui um valor a ela, e depois somente a chama, e caso queira mudar o valor dela, você muda em um só lugar e a mudança já vai para o restante). Então para facilitar nossa vida, vamos avisar o insomnia que isso é sempre contante.

- Vá em `No Environment -> Manage Environment`

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_29.png?raw=true)

- Coloque o mesmo que eu e clique em `Done`

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_30.png?raw=true)

- Agora vá mude o endereço de url conforme a imagem abaixo (digite base e espere um pouco que vai aparecer base_url isso indica que deu certo, mas mande um send novamente para ver se está tudo ok).

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_31.png?raw=true)

> OBS.: O insomnia não discarta a necessidade de você manter o servidor rodando em algum terminal (npm run dev).

# **12. CRUD**

Crude é um acronimo para

- C: Create (Criação de novos registros)
- R: Read (Ler, recuperar ou visualizar registros)
- U: Update (Atualização de registros)
- D: Delete (Deleta um registro)

Cada um desses itens, possui um método atrelado a eles no arquivo de rotas (métodos pré-definidos pelo mongoose) e também criaremos métodos para eles no nosso controller. Abaixo podemos ver uma tabela que mostra qual método corresponde a qual.

|     | routes | Controller |
| --- | ------ | ---------- |
| C   | post   | store      |
| R   | get    | show       |
| U   | put    | update     |
| D   | delete | destroy    |

## 12.1 CREATE

Para criar novas coisas, nos iremos utilizar do método `post`, e para isso remos fazer algumas modificações em nossos arquivos.

### **12.1.1 Controller**

Primeiro vamos ver a modificação do nosso controlador.

Nele iremos adicionar mais um método, que será chamado de `store` (você pode dar o nome que quiser, mas esse faz sentido). O método store tem a seguinte estrutura:

```JavaScript
async store(req, res) {
  const product = await Product.create(req.body); //Product é por conta do exemplo
  return res.json(product);
}
```

Traduzindo o que está escrito aqui: O método store vai receber uma requisição e retornará uma resposta. Sendo que essa requisição vai ter dentro de body (req.body) uma estrutura que será criada no nosso banco de dados em cima do model chamado `Product`, e isso que foi salvo será colocado no banco de dados, mas também será salvo na constante `product` que depois é retornada como um json.

Assim o controlador fica da seguinte forma:

- Arquivo `ProductController.js`

  ```JavaScript
  const Product = require("../models/Product");

  module.exports = {
    async index(req, res) {
      const products = await Product.find();

      return res.json(products);
    },

    async store(req, res) {
      const product = await Product.create(req.body);
      return res.json(product);
    }
  };
  ```

### **12.1.2 Routes**

Agora vamos fazer uma modificação no arquivo de rotas.

Nesse arquivo vamos colocar a seguinte rota:

```JavaScript
routes.post("/products", ProductController.store); //adicionar coisas
```

Se você prestou bastatne atenção, você deve ter notado que a rota é igual a rota get (/product), e pode estar pensando que vai haver confusão. Mas eu te digo que não, pois um esta com o método get e outro com o método post. A unica coisa que acontece aqui é que estamos dizendo para a aplicação que nessa url é possivel executar as duas coisas.

- Arquivo `routes.js`

  ```JavaScript
  const express = require("express");
  const routes = express.Router();

  const ProductController = require("./controllers/ProductController");

  // Minhas rotas
  routes.get("/products", ProductController.index); //pegar coisas
  routes.post("/products", ProductController.store); //adicionar coisas

  module.exports = routes;
  ```

### **12.1.3 Server**

Já o arquivo server.js ganha uma pequema modificação. Ganhado essa linha:

```JavaScript
app.use(express.json());
```

Que permite que mandemos para nossa aplicação expressões com o fomato `json`, e é exatamente o que faremos no insomnia (eu disse que ele seria util, e que o navegador não poderia fazer isso muito fácilmente)

mas primeiro, vamos dar uma olhada em como fica o arquivo `server.js`

- Arquivo `server.js`

```JavaScript
const express = require("express");
const mongoose = require("mongoose");
const mongoUrl = require("./credentials.json");
const routes = require("./src/routes");

// Iniciando o APP
const app = express();

// app.use(express.json());

// Iniciando o DB
mongoose.connect(mongoUrl.mongoUrl, {
  useNewUrlParser: true
});

// Criação
app.use(express.json());

// Rotas
app.use("/api", routes);

app.listen(3001);
```

> OBS.: `app.use(express.json());` tem que vir antes de `app.use("/api", routes);`

### **12.1.4 Insomnia**

- Crie uma nova requeste

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_32.png?raw=true)

- De um nome para ela e deixe ela com a mesma configuração da imagem abaixo (post com o body em formato json)

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_33.png?raw=true)

- Ajuste a url e escreva o json respeitando o nosso model

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_34.png?raw=true)

- Agora veja o resultado clicando em `Send`

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_35.png?raw=true)

- Vá no mongoDB compass e procure pelo seu banco de dados, e você vera salvos dois registros, o primeiro que utilizamos nos testes e o segundo que mandamos agora pelo insomnia

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_36.png?raw=true)

## 12.2 READ

Apesar de já termos falado do método `get`, vamos agora colocar isso para funcionar dentro do nosso controller para que ele nos retorne somente um registro, diferente do que fizemos com o index, que nos retorna uma lista com tudo que temos no nosso banco de dados.

E seguindo a mesma seguencia de raciocínio empregada anteriormente, vamos começar pelo controller, depois pelo routes.

O arquivo `server.js` não precisa de modificação.

### **12.2.1 Controller**

No arquivo de controle adicionaremos mais um método, que se parece bastante com o método `index`, porém agora iremos buscar o registro pelo seu ID, afinal de contas queremos encontrar apenas um registro. Mas ai precisamos passar esse ID para a nossa função, afinal ela precisa saber quem está procurando. E o jeito de fazer isso é com `req.params.id`, ou seja, dentro da requisição, temos parâmetros, e dentro dos parâmetros temos o id.

```JavaScript
  async show(req, res) {
    const product = await Product.findById(req.params.id);

    return res.json(product);
  }
```

O código completo está abaixo:

- Arquivo `ProductController.js`

  ```JavaScript
  const Product = require("../models/Product");

  module.exports = {
    async index(req, res) {
      const products = await Product.find();

      return res.json(products);
    },

    async store(req, res) {
      const product = await Product.create(req.body);
      return res.json(product);
    },

    async show(req, res) {
      const product = await Product.findById(req.params.id);

      return res.json(product);
    }
  };
  ```

### **12.2.2 Routes**

Agora precisamos passar essas informações para o nosso controlador, e faremos isso através da url. Ou seja, a nossa url conterá o parametro id a ser passado para o controlador.

```JavaScript
routes.get("/products/:id", ProductController.show); //ver coisas
```

Esse `:id` que temos é justamente a passagem do id pela rota, e isso é feito devido ao express.

- Arquivo `routes.js`

  ```JavaScript
  const express = require("express");
  const routes = express.Router();

  const ProductController = require("./controllers/ProductController");

  // Minhas rotas
  routes.get("/products", ProductController.index); //pegar coisas
  routes.post("/products", ProductController.store); //adicionar coisas
  routes.get("/products/:id", ProductController.show); //ver coisas

  module.exports = routes;
  ```

### **12.2.3 Insomnia**

Como precisamos passar um id valido para o nosso método show, vamos utilizar a request com o nome de `Index` para poder pegar um id valido.

- Depois de ter clicado em send nessa request você terá a lista de todos os registros do banco. E então copie o id de um deles

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_37.png?raw=true)

- Agora crie uma nova request do tipo get (chamarei de show) e adicione a url `base_url/products/id` sendo qeu esse id deve ser substituido pelo id que você copiou anteriormente

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_38.png?raw=true)

- Clicando em send você verá o registro referente à aquele id

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_39.png?raw=true)

## 12.3 UPDATE

Analogamente ao restante, irei fazer o controller primeiro, depois o routes e depois o insomnia. O server não requer mais mudanças.

### **12.3.1 Controller**

Aqui estaremos construindo uma mescla do create e do read, afinal precisamos encontrar um registro especifico e depois inserir algo nele.

Então a estrutura dessa modificação fica a seguinte:

```JavaScript
async update(req, res) {
  const product = await Product.findByIdAndUpdate(req.params.id, req.body, {new: true});

  return res.json(product);
}
```

Basicamente o que estamos fazendo é encontrar um determinado registro com o `params.id` e depois fazer uma modificação que veio no `body` da nossa aplicação. E para fazer isso nos utilizamos a função chamada `find by id and update` (esse nome não tem como ser mais intuitivo do que isso).

Mas agora o que seria aquele `{new: true}`, bom, isso indica para nossa função que é para retornar algo para a constante `product` somente depois de atualizar, pq se não o retorno acontece antes de atualizar, assim o `product` recebe a versão antiga. Mas no banco de dados tudo foi atualizado.

Uma observação a se fazer é que quando formos atualizar um determinado registro, não precisamos atualizar ele todo, podemos mandar somente um atributo e ele substituirá somente esse atributo.

### **12.3.2 Routes**

Agora no routes, vamos utilizar o método `put` e assim como o `post` ele precisa passar o id pelo endereço. Então ficamos com:

```JavaScript
routes.put("/products/:id", ProductController.update); //atualiza coisas
```

Agora podemos ver o arquivo completo:

- Arquivo `routes.js`

  ```JavaScript
  const express = require("express");
  const routes = express.Router();

  const ProductController = require("./controllers/ProductController");

  // Minhas rotas
  routes.get("/products", ProductController.index); //pegar coisas
  routes.post("/products", ProductController.store); //adicionar coisas
  routes.get("/products/:id", ProductController.show); //ver coisas
  routes.put("/products/:id", ProductController.update); //atualiza coisas
  module.exports = routes;
  ```

### **12.3.3 Insomnia**

- Copie um id valido, assim como fizemos na request `Show`, pois precisamos de um para fazer o update

- Crie uma nova request e de um nome à ela colocando-a como sendo do tipo `put` e coloque-a para receber um `json`.

- Configure o url para ficar do mesmo jeito que na request `Show` (`base_url/products/id`) e então escreve um json informando qual atributo trocar e como ele deve ficar. Na imagem abaixo eu troco somente o titulo do meu registro que antes era `React Native` para `React-Native`.

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_40.png?raw=true)

- Veja no mongoDB compass (recarregue o compass, mude de tabela para lista, uma hora ele vai)

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_41.png?raw=true)

## 12.4 DELETE

Analogamente ao restante, irei fazer o controller primeiro, depois o routes e depois o insomnia. O server não requer mais mudanças.

### **12.4.1 Controller**

Esse aqui chamaremos de `destroy`, e diferentemente dos outros que sempre estavamos retornando o produto, aqui não faz sentido fazermos isso, afinal não é para ter produto no final das contas.

E assim como no update, precisamos encontrar o registro para depois deletá-lo, então utilizaremos mais uma função com nome intuitivo: `findByIdAndRemove`

A estrutura fica a seguinte:

```JavaScript
async destroy(req, res){
  await Product.findByIdAndRemove(req.params.id);

  return res.send(); // retorna somente se foi bem ou mal sucedido
}
```

O arquivo completo fica:

- Arquivo `ProductController.js`

  ```JavaScript
  const Product = require("../models/Product");

  module.exports = {
    async index(req, res) {
      const products = await Product.find();

      return res.json(products);
    },

    async store(req, res) {
      const product = await Product.create(req.body);
      return res.json(product);
    },

    async show(req, res) {
      const product = await Product.findById(req.params.id);

      return res.json(product);
    },

    async update(req, res) {
      const product = await Product.findByIdAndUpdate(req.params.id, req.body, {
        new: true
      });

      return res.json(product);
    },

    async destroy(req, res) {
      await Product.findByIdAndRemove(req.params.id);

      return res.send(); // retorna somente se foi bem ou mal sucedido
    }
  };
  ```

### **12.4.2 Routes**

Veja que tudo que precisamos é do id do registro, então assim como antes a nossa rota irá mandar o id pelo url e isso será feito através de um método chamado `delete`

```JavaScript
routes.delete("/products/:id", ProductController.destroy) //destri coisas
```

- Arquivo `routes.js`

  ```JavaScript
  const express = require("express");
  const routes = express.Router();

  const ProductController = require("./controllers/ProductController");

  // Minhas rotas
  routes.get("/products", ProductController.index); //pegar coisas
  routes.post("/products", ProductController.store); //adicionar coisas
  routes.get("/products/:id", ProductController.show); //ver coisas
  routes.put("/products/:id", ProductController.update); //atualiza coisas
  routes.delete("/products/:id", ProductController.destroy); //destri coisas

  module.exports = routes;
  ```

### **12.4.3 Insomnia**

- Copie um id valido

- Crie uma nova request, chamarei ela de `Delete`

- Configure a url da forma que no `Show` (`base_url/products/id`) e pressione send e receba apenas uma mensagem indicando sucesso (a mensagem é o 200 OK que está evidenciado na imagem, ele indica sucesso).

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_42.png?raw=true)

- Agora indo ao mongoDB compass veremos que o registro sumiu

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_43.png?raw=true)

- Outro jeito de ver isso, é ir na request Index do insomnia e dar um send novamente, assim a listagem de itens do banco de dados não retornará o registro apagado

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_44.png?raw=true)

# **13. CORS**

O cors permite que a nossa aplicação seja acessada de outros lugares que não sejam a nossa maquina (localhost).

Instale o cors:

```sh
sudo npm install cors
```

Para fazer isso, vá ao arquivo `server.js` e acrescente as linhas abaixo:

```JavaScript
const cors = require("cors");
app.use(cors());
```

E pronto, agora a nossa api pode ser acessada publicamente, o aquivo todo está abaixo:

- Arquivo `server.js`

  ```JavaScript
  const express = require("express");
  const mongoose = require("mongoose");
  const mongoUrl = require("./credentials.json");
  const routes = require("./src/routes");
  const cors = require("cors");

  // Iniciando o APP
  const app = express();

  // app.use(express.json());

  // Iniciando o DB
  mongoose.connect(mongoUrl.mongoUrl, {
    useNewUrlParser: true
  });

  // Criação
  app.use(express.json());

  // cors
  app.use(cors());

  // Rotas
  app.use("/api", routes);

  app.listen(3001);
  ```

> OBS.: É meio que obvio que não vai acontecer nada agora, porque você não tem nenhum servidor para colocar ela para rodar. Mas ela está pronta para isso.

# **14. RESUMO**

- Instale o node:

  ```sh
  curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -

  sudo apt-get install -y nodejs
  ```

- De o comando

  ```sh
  npm init -y
  ```

- Instale as dependências

  ```sh
  sudo npm install express

  sudo npm install -D nodemon

  sudo npm install mongoose

  sudo npm install require-dir

  sudo npm install cors
  ```

- Ajuste o arquivo package.json para ficar da seguinte forma:

  ```JavaScript
  {
    "name": "node-api",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
      "test": "echo \"Error: no test specified\" && exit 1",
      "dev": "nodemon server.js"
    },
    "keywords": [],
    "author": "",
    "license": "ISC",
    "dependencies": {
      "express": "^4.17.1",
      "require-dir": "^1.2.0"
    },
    "devDependencies": {
      "nodemon": "^1.19.1"
    }
  }
  ```

- Rode o comando no terminal

  ```sh
  npm run dev
  ```

- Crie arquivos e diretórios para que a estrutura de arquivos fique igual a minha:

  ```sh
  ├── credentials.json
  ├── .gitignore
  ├── node_modules
  ├── package.json
  ├── package-lock.json
  ├── server.js
  └── src
      ├── controllers
      │   └── ProductController.js
      ├── models
      │   └── Product.js
      └── routes.js
  ```

- Arquivo `.gitignore`

  ```JavaScript
  # credentials
  credentials.json
  ```

- Arquivo `credentials.json`

  ```JavaScript
  {
    "mongoUrl": "mongodb+srv://SEU_USUARIO:SUA_SENNHA@UM_LINK_QUE_O_MONGO_VAI_TE_DAR"
  }
  ```

- Arquivo `server.js`

  ```JavaScript
  const express = require("express");
  const mongoose = require("mongoose");
  const mongoUrl = require("./credentials.json");
  const routes = require("./src/routes");
  const cors = require("cors");

  // Iniciando o APP
  const app = express();

  // app.use(express.json());

  // Iniciando o DB
  mongoose.connect(mongoUrl.mongoUrl, {
    useNewUrlParser: true
  });

  // Criação
  app.use(express.json());

  // cors
  app.use(cors());

  // Rotas
  app.use("/api", routes);

  app.listen(3001);
  ```

- Arquivo `ProductController.js`

  ```JavaScript
  const Product = require("../models/Product");

  module.exports = {
    async index(req, res) {
      const products = await Product.find();

      return res.json(products);
    },

    async store(req, res) {
      const product = await Product.create(req.body);
      return res.json(product);
    },

    async show(req, res) {
      const product = await Product.findById(req.params.id);

      return res.json(product);
    },

    async update(req, res) {
      const product = await Product.findByIdAndUpdate(req.params.id, req.body, {
        new: true
      });

      return res.json(product);
    },

    async destroy(req, res) {
      await Product.findByIdAndRemove(req.params.id);

      return res.send(); // retorna somente se foi bem ou mal sucedido
    }
  };
  ```

- Arquivo `routes.js`

  ```JavaScript
  const express = require("express");
  const routes = express.Router();

  const ProductController = require("./controllers/ProductController");

  // Minhas rotas
  routes.get("/products", ProductController.index); //pegar coisas
  routes.post("/products", ProductController.store); //adicionar coisas
  routes.get("/products/:id", ProductController.show); //ver coisas
  routes.put("/products/:id", ProductController.update); //atualiza coisas
  routes.delete("/products/:id", ProductController.destroy); //destri coisas

  module.exports = routes;
  ```

- Arquivo `Product.js`

  ```JavaScript
  const { Schema, model } = require("mongoose");

  const ProductSchema = new Schema(
    {
      title: {
        type: String,
        required: true
      },
      description: {
        type: String,
        required: true
      },
      url: {
        type: String,
        required: true
      }
    },
    {
      timestamps: true
    }
  );

  module.exports = model("Product", ProductSchema);
  ```
