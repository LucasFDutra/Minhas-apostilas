# Apostila de NodeJS

Autor: Lucas Felipe Dutra

**ANTES DE QUALQUER COISA, VEJA ESSE VIDEO [AQUI](https://www.youtube.com/watch?v=9w3o9NHXqu0&list=PLMdYygf53DP5Sc6yFYs6ZmjsuuA2fu0TK) PARA APRENDER MAIS SOBRE CLEAN CODE**

# Dicas

- [Curso da rocketseat](https://skylab.rocketseat.com.br)
- [Material de JavaScript](https://github.com/LucasFDutra/Minhas-apostilas/tree/master/JavaScript)

Todo o material que aqui estará será feito durante a execução do exemplo que se encontra na pasta `node-api` aqui dentro desse repositório.

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

Esse comando criou um arquivo chamado `package.json`. Esse arquivo por enquanto está apenas com as informações do projeto, como por exemplo nome, versão, descrição, e outras coisas. Mas será nele que iremos colocar quais serão as nossas dependências e suas versões (as bibliotecas utilizadas).

No meu caso, criei uma aplicação de exemplo chamada `node-api`

- A árvore de diretórios nesse momento fica:
  ```sh
  └── package.json
  ```

> Se gostou dessa representação de árvores de diretórios, abra seu terminal e instale o `tree` com `sudo apt install tree` depois vá para o diretório em que quer exibir a árvore e execute o comando `tree` e veja o resultado. No caso eu copiei e colei ele aqui entre o bloco gerado por ``` que a liguagem markdown me fornece.

## 3.1 INSTALANDO DEPENDÊNCIAS

As dependências são basicamente bibliotecas. E para instalá-las na sua aplicação, abra o terminal na pasta da aplciação e digite.

```sh
sudo npm install nome_da_dependencia
```

> OBS.: No linux precisa do comando sudo.

# **4. EXPRESS**

O `express` é um micro framwork que vai nos auxiliar a trabalhar com rotas (endereços que podem ser acessados na api) e views (formas de visualização).

> OBS.: As views não são utilizadas quando se trabalha com API rest (API rest é quando o backend e o frontend são completamente separados).

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

Note que se a bibliotecas em questão estiver dentro de `node_modules` então a importação acontece igual ao que fizemos para o `express`, porém se a biblioteca for um arquivo criado pelo usuário e que esteja em outro diretório, então deve-se especificar o caminho do arquivo. Exemplo:

```JavaScript
const variavel = require("./libs/biblioteca.js")
```

Agora que temos o express na aplicação, vamos atribuir uma variável a ele, para podermos trabalhar com ela (pra quem manja de poo, esse negocio que vou fazer agora parece muito com a criação de um objeto, e pode usar essa analogia ai que vai dar certo - eu mesmo estou usando isso pra poder entender melhor)

```JavaScript
const express = require("express");

const app = express();

app.listen(3001);
```

O comando listen, faz com que a aplicação fique ouvindo a porta 3001 do nosso pc, então caso rodemos uma aplicação frontend no nosso browser nessa porta ela estará conectada ao nosso backend.

Agora rode esse código digitando no teminal `node server.js` ele ficará esperando algo acontecer, dai abra seu browser e digite o endereço `http://localhost:3001/`, mas é claro que não vai ter nada lá alem de um `Cannot GET /` pois a aplicação ainda não possui nenhuma tratativa de rotas.

# **5. ROTAS**

Para trabalhar com as rotas, precisamos utilizar o comando

```JavaScript
app.get("local", (req, res) => {/*função*/});
```

- `local`: é para onde a nossa aplicação irá, no caso se eu quiser que ela vá para a raiz, eu coloco '/', mas poderia ir para por exemplo `http://localhost:3001/teste`, assim eu colocaria `/teste`

- req: contém todos os detalhes e informações de uma requisição feita ao servidor.

  - Por exemplo:
    - Parâmetros;
    - Corpo da requisição;
    - Cabeçalho;
    - Usuário;
    - Autenticação;
    - etc.

- res: contém a resposta que vamos dar de acordo com a requisição

Tanto o req quanto o res possuem métodos, e eles serão explorados dentro da nossa função. Por exemplo, podemos utilizar o método `send` para retornar algo como resposta.

```JavaScript
app.get("local", (req, res) => {
    res.send("Hello World");
});
```

Fazendo esse modificação no nosso arquivo server.js, ele ficará da seguinte forma:

```JavaScript
const express = require("express");

const app = express();

app.get("/", (req, res) => {
  res.send("Hello World");
});

app.listen(3001);
```

E reesecutando o comando `node server.js` e abrindo o browser na porta 3001 bem na home ('/') teremos a mensagem 'Hello World' aparecendo.

> Sugestão.: Mude de `/` para `/teste` e coloque no browser `http://localhost:3001/teste` para ver o resultado, será bom para entender como funcionam esses comandos de rota.

Se você seguiu a sugestão deve ter entendido que basicamente vamos usar o `get` para executar alguma coisa de acordo com a pagina que o usuário estiver acessando.

# **6. NODEMON**

Como já deve ter notado, não é legal ficar tendo que reiniciar o servidor a cada modificação feita, então é muito interessante que exista uma ferramenta para fazer automaticamente para gente, assim a aplicação ficaria no modo live reload. E para isso mesmo que existe o nodemon.

Instale o mesmo dando comando abaixo dentro da pasta do projeto:

```sh
sudo npm install -D nodemon
```

> OBS.: O -D é para instalar como desenvolvedor, isso faz com que ela fique separada das outras dependências, afinal ela é apenas para o ambiente de desenvolvimento, afinal live reload não é necessário para a aplicação além do momento de em que ela está sendo desenvolvida.

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

Clique em `try free` e crie uma conta

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_01.png?raw=true)

Você vai cair nessa tela aqui

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_02.png?raw=true)

Role tudo para baixo e clique em create cluster (note que temos 512mb gratuitos para utilizarmos)

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_03.png?raw=true)

Depois vai cair nessa tela abaixo e isso pode demorar um tempo

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_04.png?raw=true)

Depois de criado vá em Database Access para criar um usuário e senha

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_05.png?raw=true)

Vá em add new user

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_06.png?raw=true)

Crie o usuário, e deixe marcada a opção Read and write to any database e adicione o usuário

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_07.png?raw=true)

Vá em network access

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_08.png?raw=true)

Crie um novo acesso em add ip address e depois permita que esse banco de dados seja acessado de qualquer lugar clicando em Allow access from anywhere

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_09.png?raw=true)

Vá em clusters e clique em connect

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_10.png?raw=true)

Selecione a opção connect to your application

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_11.png?raw=true)

Agora deixe a tela seguinte com a configuração mostrada abaixo e clique em copy

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_12.png?raw=true)

Agora dentro da pasta backend adicione o mongoose com o comando

```sh
sudo npm i mongoose
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

A url de conexão é aquela que pegamos do mongoDB ao clicar em copy. Assim nosso código ficará da seguinte forma:

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

Uma observação é que provavelmente você terá recebido esse url com `<username>` e `<password>` é só trocar pelo username e o password que você definiu no passo de criação da base de dados (lembre de retirar o sinal de <> também, veja meu exemplo).

> OBS.: O parametro `test` que está nessa url é o nome do banco de dados, porém se trocar esse nome e colocar qualquer outra coisa ele simplesmente criará esse novo banco de dados para você. Mas pode deixar teste mesmo (em algum lugar lá no começo provavelmente tinha um lugar para definir o nome do banco e eu não vi).

> OBS.: O comando `useNewUrlParser` é para identificar para o mongoose que estaremos utilizando o novo formato de url (evita um warning).

Pronto, nossa conexão com o banco de dados está feita

## 7.1 SEGURANÇA

Esse banco de dados será deletado, por isso deixei senha à mostra aqui, porém você não quer que o seu fique dessa forma, sendo assim o melhor jeito é colocar esse link de acesso em um arquivo `.json` (no caso criei um arquivo chamado `credentials.json`), e puxar a informação dele, e colocar esse arquivo dentro do `.gitignore` para assim a url de acesso não ficar à mostra para o mundo.

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

Se quiser verificar o que está acontecendo no seu banco de dados, de uma forma mais fácil do que ficar acessando o site do mongoDB, utilize o mongoDB compass, que é uma interface que irá trazer as informações do seu banco. Para baixar o mongodb compass community clique [aqui](https://www.mongodb.com/products/compass). Agora é só clicar em `try now`

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_13.png?raw=true)

Clique em tools escolha a melhor versão para você e clique em download

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_14.png?raw=true)

Agora abra o mongoDB compass community e depois vá no mongoDB Atlas (onde configurou seu banco de dados) e vá em cluster e clic em connect novamente e depois escolha a opção connect with mongoDB compass

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_15.png?raw=true)

Ai você clica em copy

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_16.png?raw=true)

Volte para o mongoDB compass e ele automaticamente identificará que existe uma url copiada e perguntará se quer importar ela para dentro da aplicação. Clique em sim

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_17.png?raw=true)

Coloque o username e o password conforme havia configurado antes, e em `Autentication Database` coloque `admin`. E clique em connect

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_18.png?raw=true)

Veja que a base de dados de teste está presente

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/NodeJS/Imagens/Figura_19.png?raw=true)

# **8. MODEL**

O model representa uma tabela no banco de dados.

Crie dentro da pasta do projeto uma pasta chamada `src` e dentro da mesma crie uma pasta chamada `models`.

> OBS: Claro que os nomes são opcionais, mas eles fazem sentido no mundo da programação, então meio que por convenção coloque esses nomes.

Agora, vamos criar dentro dessa pasta um arquivo .js que será nosso arquivo model. Coloque o nome dele de acordo com a url que você quer usar para chegar nele. Se a aplicação fosse para utilizar cadastros de desenvolvedore, você poderia utilizar `Dev.js`, mas se fosse uma loja e quisessemos que esse url levasse aos produtos, iriamos colocar `Product.js`

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

> OBS: Para seguir com o exemplo que estou estudando irei criar um arquivo chamado `Product.js`. Mas para utilizar de exemplo aqui eu sempre chamarei de `NomeDoModel`

Dentro de `Product.js` deve-se importar duas coisas do mongoose, o `Schema` e o `model`, para isso digite a seguinte linha:

```JavaScript
const { Schema, model } = require('mongoose')
```

Agora vamos criar a estrutura do nosso banco de dados, ou seja o esquema dele. Que é trazido da seguite forma:

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

O `timestamps` serve para gerar automaticamente duas colunas para nós, uma chamada createdAt e outra chamada updatedAt em cada registro da base de dados.

- createdAt: Armazena a data de criação de cada registro
- updatedAt: Armazena a data da ultima alteração do registro

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

> OBS: ainda não tente abrir nada no seu navegador, pois sem ajustar o arquivo `server.js` e sem criar o arquivos de rotas não vai acontecer nada.

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

> OBS: O insomnia não discarta a necessidade de você manter o servidor rodando em algum terminal (npm run dev).