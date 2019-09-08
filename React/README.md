# Apostila de React

Autor: Lucas Felipe Dutra

**ANTES DE QUALQUER COISA, VEJA ESSE VIDEO [AQUI](https://www.youtube.com/watch?v=ln6t3uyTveQ&list=PLVc5bWuiFQ8GgKm5m0cZE6E02amJho94o&index=9)**

# Dicas

- [Documentação pt-br](https://pt-br.reactjs.org/)
- [Configure seu ambiente de desenvolvimento](https://github.com/LucasFDutra/Ambiente-React-E-React-native-Com-ESlint-Airbnb)
- [Material de JavaScript](https://github.com/LucasFDutra/Minhas-apostilas/tree/master/JavaScript)
- [Curso gratuito Rocketseat](https://skylab.rocketseat.com.br/node/curso-react-js)

De uma olhada nesse site aqui [codebox](https://codesandbox.io/), isso é uma aplicação web que vai permitir que você crie aplicações react sem precisar instalar nada no seu pc, já vai estar tudo pronto, é otimo para um primeiro contato. Porém eu não farei nada com ela durante esse material, farei tudo no meu pc mesmo, porém se quiser utilizar essa ferramenta, fique a vontade.

# **1. INTRODUÇÃO**

## 1.1 INSTALAÇÃO E CONFIGURAÇÕES

Para iniciar seus estudos com react, veja o material de configuração do ambiente de desenvolvimento que está [aqui](https://github.com/LucasFDutra/Ambiente-React-E-React-native-Com-ESlint-Airbnb), pois nesse material eu ensino desde a instalação do node, até como iniciar uma aplicação com react. No caso desse material aqui, o interessante são as seções 1, 2, 3 e 6. O restante é para react-native, que fica em outro material.

> OBS.: To falando sério, vê lá, se não vai ficar perdido aqui, as coisas não vão funcionar, lá eu ensino a instalar tudo que precisa.

## 1.2 O QUE É REACT?

Bom, o react é uma biblioteca para javaScript, criada e mantida pelo facebook (com apoio da comunidade).

O react serve para trabalharmos no frontend de uma aplicação web.

### 1.2.1 React e react-native

E se em algum momento você ouviu falar de react-native, e ficou em duvida do que é isso, se é igual ao react. Bom, eu vou explicar aqui rapidinho: Não são a mesma coisa, o react e o react-native possuem semelhanças gigantescas, o que é otimo, pois de passar um código react para um react-native ou vice versa, se torna muito fácil, porém, elas possuem finalidades diferentes, o react serve para criar aplicações web, e o react-native serve para criar aplicações mobile (android e ios de uma vez só).

# **2. INICIANDO ESTUDOS**

Para irmos estudando react, eu vou criar um exemplo, e vou ir trabalhando em cima dele. Nesse caso, irei criar um exemplo chamado `huntweb`, que estará dentro desse repositório.

Crie o projeto, escolhendo a pasta que ele deve estar, e de o comando no terminal

```sh
create-react-app huntweb
```

> OBS.: Lembrando que se você não configurou o ambiente de desenvolvimente, esse comando vai dar errado, afinal de contas você não instalou o `create-react-app`... Eu falei que era pra ver o material de configuração.

# **3. CONHECENDO ESTRUTURA DA APLICAÇÃO**

A árvore de diretórios logo após a construção da aplicação é a seguitne:

```sh
├── node_modules
├── package.json
├── public
│   ├── favicon.ico
│   ├── index.html
│   ├── logo192.png
│   ├── logo512.png
│   ├── manifest.json
│   └── robots.txt
├── README.md
├── src
│   ├── App.css
│   ├── App.js
│   ├── App.test.js
│   ├── index.css
│   ├── index.js
│   ├── logo.svg
│   └── serviceWorker.js
└── yarn.lock
```

Vamos passar cada um dos diretorios e alguns arquivos mais importantes:

- `node_modules`: Estão todas as dependencias (eu fiz elas não aparecerem aqui, pq são muitas, ia ficar muito ruim de ver na árvore).

- `public`: Estão todos os arquivos que serão acessiveis pelo usuário final da aplicação

- `src`: É onde ficarão os nossos códigos. No caso ele já vem com alguns arquivos padrões, que gerarão uma aplicação, a qual você vai ver daqui a pouco.

- `package.json` É onde estarão listadas as dependencias do nosso projeto.

- `README.md`: É o readme da documentação do `create-react-app` que pode ser deletado.

- `yarn.lock`: É o cache das nossas dependências.

Agora que você já conhece as pastas, pegue seu terminal, e com ele apontando para dentro da pasta `huntweb` rode o comando:

```sh
yarn start
```

Isso vai abrir uma aba no seu navegador, que é a aplicação padrão que vem com o `create-react-app`

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_01.png?raw=true)

# **4. ARRUMANDO OS ARQUIVOS**

Quando iniciar uma palicação, nem tudos os arquivos que o `create-react-app` gera são necessários, então vamos apagar alguns deles.

A árvore de diretórios nesse instante é:

```sh
├── node_modules
├── package.json
├── public
│   ├── favicon.ico
│   ├── index.html
│   ├── logo192.png
│   ├── logo512.png
│   ├── manifest.json
│   └── robots.txt
├── README.md
├── src
│   ├── App.css
│   ├── App.js
│   ├── App.test.js
│   ├── index.css
│   ├── index.js
│   ├── logo.svg
│   └── serviceWorker.js
└── yarn.lock
```

Ela deve ficar da seguinte forma:

```sh
├── node_modules
├── package.json
├── public
│   ├── favicon.ico
│   ├── index.html
│   ├── logo192.png
│   ├── logo512.png
│   ├── manifest.json
│   └── robots.txt
├── README.md
├── src
│   ├── App.js
│   ├── index.js
│   └── serviceWorker.js
└── yarn.lock
```

Dentro do arquivo `index.js` você pode remover algumas linhas (que estavam fazendo importações dos arquivos que apagamos), fazendo ele ficar da seguinte forma:

```JavaScript
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import * as serviceWorker from './serviceWorker';

ReactDOM.render(<App />, document.getElementById('root'));

serviceWorker.unregister();
```

E o arquivo `App.js` deve ficar da seguinte forma:

```JavaScript
import React from "react";

function App() {
  return (
    <div className="App">
      <h1>Olá mundo!</h1>
    </div>
  );
}

export default App;
```

> OBS.: Você já deve ter imaginado que esse `<h1>Olá mundo<h1>` não é obrigatório, e ele vai sair dai depois.

Agora digite em um terminal

```sh
yarn start
```

E aparecerá em seu navegador a menságem `Olá mundo!`

# **5. ELEMENTO REACT**

Um elemento em react pode ser declarado em forma de JSX.

E o que esse tal de JSX? Bem o formato jsx é basicamente escrever o elemento em html (bem parecido com isso). Veja o exemplo abaixo:

```JavaScript
const elemento = <div><h2>Olá mundo</h2></div>
```

Assim quando utilizarmos o `elemento` no nosso código já sabemos que ele se refere à aquela linha html.

E como o jsx é entendido somente pelo react, em todo lugar que você utilizar essa sintax é necessário importar o react

```JavaScript
import React from 'react';
```

# **6. COMPONENTE**

Um componente em react não é nada mais do que a união de vários elementos. E esse componente é dado dentro do retorno de uma função.

```JavaScript
// componente
function App() {
  return (
    <div className="App">
      <h1>Hello CodeSandbox</h1>
      <h2>Start editing to see some magic happen!</h2>
    </div>
  );
}
```

Mas uma coisa deve ser respeitada, uma função pode retornar apenas um componente, logo podemos colocar quantos elementos quisermos, desde que eles estejam contidos dentro de uma tag que sirva como "borda" da caixa do componente. No exemplo acima, utilizamos uma `div` como sendo esse conteiner, assim tudo que está dentro da `div` componhe um unico componente, e podemos retornar a `div` como um todo.

Veja que esse componente possui elementos dentro dele, o h1 e h2, mas se quisermos, também podemos colocar o elemento que foi criado separadamente dentro do componente. Veja abaixo

```JavaScript
// componente
function App() {
  return (
    <div className="App">
      <h1>Hello CodeSandbox</h1>
      <h2>Start editing to see some magic happen!</h2>
      {elemento}
    </div>
  );
}
```

# **7. HOOKS**

Hooks são coisas bem novas no react, e eles facilitam a nossa vida para trabalhar com estados. Ou seja, ele facilita para sabermos qual é o valor de uma dada variável em um dado instante, ou então se algo mudou na nossa variável (o valor dela, se um objeto recebeu um novo incremento).

Antes dos hooks era um pouco mais chato de fazer isso. Mas como agora temos eles, eu vou seguir tratando tudo com hooks.

- [Recomendado](https://reactjs.org/docs/hooks-intro.html)

Antes de inicar, saiba que hooks só podem ser utilizados em componentes funcionais, ou seja, componentes criados mediante a utilização de funções (sim, existe outro jeito de criar componentes, mediante classes ES6, mas não vem ao caso agora).

## 7.1 EXEMPLO

Vamos criar uma pequena aplicação para entendermos melhor esse conceito de hooks.

Nossa aplicação terá a seguinte tarefa:

- Mostrar um número
- Acrescentar uma unidade nesse número ao clicar em um botão.

Para começarmos isso vamos primeiro criar a interface.

Como nosso index tem por função apenas retornar o que está dentro do nosso App, então tudo tem que ser criado dentro de `App.js`

E como jsx é bem parecido com html, mudando apenas alguns nomes de atributos, como por exemplo, `class` em jsx fica sendo `className`, isso porque `class` é uma palavra reservada no javaScript (Então fique atento à esses detalhes), então a criação dessa interface vai ser bem simples considerando que você sabe html.

Como eu falei, o arquivo `index.js` não deve ser modificado. Então vou mostar o como fica o arquivo `App.js`.

- Arquivo `App.js`

  ```JavaScript
  import React from "react";

  function App() {
    let i = 0;

    function click(i) {
      console.log(i);
      return (i += 1);
    }

    return (
      <div className="App">
        <button onClick={() => (i = click(i))}>Incremento</button>
        <p>O valor de i é: {i}</p>
      </div>
    );
  }

  export default App;
  ```

- Saída:
  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_02.png?raw=true)

Veja que o valor de `i` mostrado no console indica que ele sofre alterações, porém o valor exibido na aplicação é sempre 0.

Isso aconte pois o componente é reenderizado apenas uma vez. Ou seja, ele é sempre mostrado do jeito que foi construido no momento inicial.

E é para resolver esse tipo de problema que os hooks servem. Eles fazem esse papel de entender que algo mudou e precisa ser reenderizado na tela.

Agora vamos reformular o código utilizando hooks.

Mas primeiro vamos importar um hook.

Existem alguns hooks para podermos importar, mas os mais relevantes são:

- `useState`: Para controlar o valor de uma variável;
- `useEfect`: Monitora mudanças em alguma coisa.

Para importar esses dois faremos:

```JavaScript
import React, {useState, useEffect} from "react";
```

### **7.1.1 useState**

Vamos efetuar o exemplo utilizando apenas o `useState`.

A declaração para o `useState` é a seguinte:

```JavaScript
const [nomeDaVariavel, setNomeDaVariavel] = useState(valorInicialDaVariavel);
```

> Claro que não é obrigatório utilizar `setNomeDaVariavel`, pode ser qualquer coisa, mas assim é mais intuitivo.

- Explicando essa sintax:

  - `nomeDaVariavel`: é a variável que vamos trabalhar, no caso do exemplo `i`;
  - `setNomeDaVariavel`: nome da função que vai colocar um valor na variável `nomeDaVariavel`;
  - `valorInicialDaVariavel`: bem intuitivo, esse é o valor inicial da variável, pode ser desde um número, até um array vazio.

- Arquivo `App.js`

  ```JavaScript
  import React, { useState } from "react";

  function App() {
    const [i, setI] = useState(0);

    function click(i) {
      setI(i + 1);
      console.log(i);
    }

    return (
      <div className="App">
        <button onClick={() => click(i)}>Incremento</button>
        <p>O valor de i é: {i}</p>
      </div>
    );
  }

  export default App;
  ```

- Saída

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_03.png?raw=true)

Veja que agora a aplicação é sempre atualizada, e o valor de i no console bate com o da aplicação (o do console fica atrasado de uma unidade mesmo).

> OBS.: Em `onClick` é importante utilizar uma arrow function, pois se utilizar direto o `click(i)` ele será executado constantemente, e isso vai gerar um erro.

### 7.1.2 useEfect

Vamos efetuar o exemplo utilizando o `useEffect`. Porém, irei também utilizar o `useState` para auxiliar.

O exemplo que irei construir será o mesmo de antes, mas eu farei o seguinte, toda vez que o valor de i for modificado, uma mensagem irá aparecer na tela.

A declaração para o `useEffect` é a seguinte:

```JavaScript
useState( () => {}, [])
```

- Explicando essa sintax:

  - `() => {}`: uma função, no formato de arrow function, em que estará o código do que deve ser feito quando o `useEffect` for disparado.
  - `[]`: É um array com as dependências do `useEffect`. Ou seja, tudo aquilo que ele ficará olhando se possui ou não modificação, e caso ocorra ele será ativado.
    - Se deixarmos o array do `useEffect` vazio (`[]`), ele irá executar apenas uma vez.
    - Se eu colocar uma variável, a função irá executar sempre que essa variável for modificada.

Seguindo o mesmo exemplo de um botão que incrementa valores, nos iremos fazer o seguinte:

- Arquivo `App.js`

  ```JavaScript
  import React, { useState, useEffect } from "react";

  function App() {
    const [i, setI] = useState(0);

    useEffect(()=>{
      window.alert('O valor de i foi alterado');
    }, [i])

    function click(i) {
      setI(i + 1);
      console.log(i);
    }

    return (
      <div className="App">
        <button onClick={() => click(i)}>Incremento</button>
        <p>O valor de i é: {i}</p>
      </div>
    );
  }

  export default App;
  ```

* Saída

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_04.png?raw=true)

> OBS.: podemos passar quantos parâmetros quisermos dentro do array do `useEffect`.

**Agora que já entendeu esses conceitos de componentes e hooks, vamos dar seguimento ao exemplo principal desse material (huntweb), e vamos aprender alguns conceitos no caminho.**
