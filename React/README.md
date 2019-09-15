# Apostila de React

Autor: Lucas Felipe Dutra

**ANTES DE QUALQUER COISA, VEJA ESSE VIDEO [AQUI](https://www.youtube.com/watch?v=ln6t3uyTveQ&list=PLVc5bWuiFQ8GgKm5m0cZE6E02amJho94o&index=9)**

# Dicas

- [Documentação pt-br](https://pt-br.reactjs.org/)
- [Configure seu ambiente de desenvolvimento](https://github.com/LucasFDutra/Ambiente-React-E-React-native-Com-ESlint-Airbnb)
- [Material de JavaScript](https://github.com/LucasFDutra/Minhas-apostilas/tree/master/JavaScript)
- [Curso gratuito Rocketseat](https://skylab.rocketseat.com.br/node/curso-react-js)

De uma olhada nesse site aqui [codebox](https://codesandbox.io/), isso é uma aplicação web que vai permitir que você crie aplicações react sem precisar instalar nada no seu pc, já vai estar tudo pronto, é otimo para um primeiro contato. Porém eu não farei nada com ela durante esse material, farei tudo no meu pc mesmo, porém se quiser utilizar essa ferramenta, fique a vontade.

# Sumário

- [**1. INTRODUÇÃO**](#1-introdução)
  - [1.1 INSTALAÇÃO E CONFIGURAÇÕES](#11-instalação-e-configurações)
  - [1.2 O QUE É REACT?](#12-o-que-é-react)
    - [**1.2.1 React e react-native**](#121-react-e-react-native)
- [**2. INICIANDO ESTUDOS**](#2-iniciando-estudos)
- [**3. CONHECENDO ESTRUTURA DA APLICAÇÃO**](#3-conhecendo-estrutura-da-aplicação)
- [**4. ARRUMANDO OS ARQUIVOS**](#4-arrumando-os-arquivos)
- [**5. ELEMENTO REACT**](#5-elemento-react)
- [**6. COMPONENTE**](#6-componente)
- [**7. HOOKS**](#7-hooks)
  - [7.1 EXEMPLO](#71-exemplo)
    - [**7.1.1 useState**](#711-usestate)
    - [**7.1.2 useEfect**](#712-useefect)
- [**8. CICLOS DE VIDA**](#8-ciclos-de-vida)
  - [8.1 STATE](#81-state)
    - [**8.1.1 Exemplo**](#811-exemplo)
  - [8.2 COMPONENT DID MOUNT](#82-component-did-mount)
    - [**8.2.1 Equivalente com hooks**](#821-equivalente-com-hooks)
    - [**8.2.2 Exemplo**](#822-exemplo)
      - [8.2.2.1 Utilizando ciclos de vida](#8221-utilizando-ciclos-de-vida)
      - [8.2.2.2 Utilizando hooks](#8222-utilizando-hooks)
  - [8.3 COMPONENT DID UPDATE](#83-component-did-update)
    - [**8.3.1 Equivalente com hooks**](#831-equivalente-com-hooks)
    - [**8.3.2 Exemplo**](#832-exemplo)
      - [8.3.2.1 Utilizando ciclos de vida](#8321-utilizando-ciclos-de-vida)
      - [8.3.2.2 Utilizando hooks](#8322-utilizando-hooks)
  - [8.4 COMPONENT DID UNMOUNT](#84-component-did-unmount)
    - [**8.4.1 Equivalente com hooks**](#841-equivalente-com-hooks)
    - [**8.4.2 Exemplo**](#842-exemplo)
      - [8.4.2.1 Utilizando ciclos de vida](#8421-utilizando-ciclos-de-vida)
      - [8.4.2.2 Utilizando hooks](#8422-utilizando-hooks)
- [**9. HUNTWEB**](#9-huntweb)
  - [9.1 HEADER](#91-header)
  - [9.2 API](#92-api)
    - [**9.2.1 Axios**](#921-axios)
  - [9.3 PAGES](#93-pages)
    - [**9.3.1 Ciclos de vida**](#931-ciclos-de-vida)
      - [9.3.1.1 Main](#9311-main)
      - [9.3.1.2 Página anterior/proxima](#9312-página-anteriorproxima)
      - [9.3.1.3 Navegação](#9313-navegação)
      - [9.3.1.4 Product](#9314-product)
    - [**9.3.2 Hooks**](#932-hooks)

# **1. INTRODUÇÃO**

## 1.1 INSTALAÇÃO E CONFIGURAÇÕES

Para iniciar seus estudos com react, veja o material de configuração do ambiente de desenvolvimento que está [aqui](https://github.com/LucasFDutra/Ambiente-React-E-React-native-Com-ESlint-Airbnb), pois nesse material eu ensino desde a instalação do node, até como iniciar uma aplicação com react. No caso desse material aqui, o interessante são as seções 1, 2, 3 e 6. O restante é para react-native, que fica em outro material.

> OBS.: To falando sério, vê lá, se não vai ficar perdido aqui, as coisas não vão funcionar, lá eu ensino a instalar tudo que precisa.

## 1.2 O QUE É REACT?

Bom, o react é uma biblioteca para javaScript, criada e mantida pelo facebook (com apoio da comunidade).

O react serve para trabalharmos no frontend de uma aplicação web.

### **1.2.1 React e react-native**

E se em algum momento você ouviu falar de react-native, e ficou em duvida do que é isso, se é igual ao react. Bom, eu vou explicar aqui rapidinho: Não são a mesma coisa, o react e o react-native possuem semelhanças gigantescas, o que é otimo, pois de passar um código react para um react-native ou vice versa, se torna muito fácil, porém, elas possuem finalidades diferentes, o react serve para criar aplicações web, e o react-native serve para criar aplicações mobile (android e ios de uma vez só).

# **2. INICIANDO ESTUDOS**

Para irmos estudando react, eu vou criar um exemplo, e vou ir trabalhando em cima dele. Nesse caso, irei criar um exemplo chamado `huntweb`, que estará dentro desse repositório.

Crie o projeto, escolhendo a pasta que ele deve estar, e de o comando no terminal

```sh
create-react-app huntweb
```

> OBS.: Lembrando que se você não configurou o ambiente de desenvolvimente, esse comando vai dar errado, afinal de contas você não instalou o `create-react-app`... Eu falei que era pra ver o material de configuração.

# **3. CONHECENDO ESTRUTURA DA APLICAÇÃO**

- A árvore de diretórios logo após a construção da aplicação é a seguinte:

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

Vamos passar cada um dos diretórios e alguns arquivos mais importantes:

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

- A árvore de diretórios nesse instante é:

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

- A árvore deve ficar da seguinte forma:

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

- Arquivo `src/index.js`

  ```JavaScript
  import React from 'react';
  import ReactDOM from 'react-dom';
  import App from './App';
  import * as serviceWorker from './serviceWorker';

  ReactDOM.render(<App />, document.getElementById('root'));

  serviceWorker.unregister();
  ```

E o arquivo `App.js` deve ficar da seguinte forma:

- Arquivo `src/App.js`

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

- Arquivo `src/App.js`

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

- Arquivo `src/App.js`

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

- Saída:

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_03.png?raw=true)

Veja que agora a aplicação é sempre atualizada, e o valor de i no console bate com o da aplicação (o do console fica atrasado de uma unidade mesmo).

> OBS.: Em `onClick` é importante utilizar uma arrow function, pois se utilizar direto o `click(i)` ele será executado constantemente, e isso vai gerar um erro.

### **7.1.2 useEfect**

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

Seguindo o mesmo exemplo de um botão que incrementa valores, nós iremos fazer o seguinte:

- Arquivo `src/App.js`

  ```JavaScript
  import React, { useState, useEffect } from "react";

  function App() {
    const [i, setI] = useState(0);

    useEffect(()=>{
      window.alert('O valor de i foi alterado');
    }, [i]);

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

- Saída:

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_04.png?raw=true)

> OBS.: podemos passar quantos parâmetros quisermos dentro do array do `useEffect`.

# **8. CICLOS DE VIDA**

> Recomendo a leitura desse artigo [aqui](https://medium.com/creditas-tech/m%C3%A9todos-do-ciclo-de-vida-de-componentes-reactjs-um-mergulho-profundo-332ed7b3b782)

A outra forma de fazer esse esquema de controlar estados de um componente, é utilizando ciclos de vida de um componente, porém esse é o jeito antigo, e tudo fica mais fácil com hooks.

> OBS.: É importante frisar que os hooks e os ciclos de vida são coisas diferentes, não é que os hooks sejam iguais aos ciclos de vida, eles apenas cumpre os mesmos serviços, porém de formas diferentes. Então é um pouco errado dizer que "coisa x em hooks é igual a coisa y em ciclos de vida". O correto seria dizer que "coisa x em hooks se faz assim, em ciclos de vida fazemos o mesmo do jeito y". É a mesma coisa que comparar um lápis e uma lapiseira, ambos escrevem, mas cada um faz isso a sua maneira e funcionam de formas totalmetne diferentes, mas no final cumprem a mesma função.

Então porque mostrar essa ideia de ciclos de vida?

O motivo de fazer isso é bem simples. Muitos materiais na internet, incluindo a documentação do react, ainda mostra como fazer as coisas desse jeito, então é bom que eu também faça isso para facilitar as suas pesquisas.

Porém, Meu objetivo nessa seção é mais de mostrar como converter um códico com essa implementação para um código utilizando hooks, do que ensinar ciclos de vida propriamente dito.

Para utilizar esse tipo de implementação, o nosso código deve possuir uma estrutura básica:

```JavaScript
import React, { Component } from 'react';

export default class Main extends Component {
  render() {
    return (
      <h1>Hello World</h1>
    );
  }
}
```

Ou seja, nós importamos um componente e extendemos ele, e todos os métodos de ciclo de vida que utilizaremos serão métodos desse componente.

E dentro da classe do componente, iremos sempre chamar o método `render` e dentro dele teremos o retorno do nosso código `jsx`, seguindo aquela mesma regra de retornar um único componente apenas.

Agora vem um detalhe muito importante, quando for criar funções dentro de uma classe, faça elas no modelo de arrow functions. Caso contrário vai dar problema. O motivo pode ser visto nesse video [aqui](https://www.youtube.com/watch?v=AgOwGKB8D2M).

Então caso precise criar uma função dentro da classe, siga o modelo abaixo:

```JavaScript
import React, { Component } from 'react';

export default class Main extends Component {

  myFunction = () => {
    // código...
  }

  render() {
    return (
      <h1>Hello World</h1>
    );
  }
}
```

> OBS.: Os métodos que são do componente não precisam estar como arrow function.

## 8.1 STATE

Como vimos em hooks, é meio complicado modificar o valor de uma variável com o react e isso ser mostrado na tela, e como você deve imaginar, aqui nós não temos um `useState` para fazer esse serviço para nós. Aqui temos um objeto chamado `state` que conterá todas as variáveis que necessitem desse controle de estados.

Veja abaixo como devemos criar esse objeto.

```JavaScript
import React, { Component } from 'react';

export default class Main extends Component {
  state = {
    nomeDaVariavel_1: valorDeInicioDaVariavel_1,
    nomeDaVariavel_2: valorDeInicioDaVariavel_2,
    nomeDaVariavel_n: valorDeInicioDaVariavel_n,
  };

  render() {
    return (
      <h1>Hello World</h1>
    );
  }
}
```

Como você viu acima até que não é tão diferente de um hook, então se eu quiser posso inicializar a variável com um array, com um outro objeto, enfim, da forma que eu quiser.

```JavaScript
state = {
  data: [],
  contador: 0,
};
```

Porém na hora de ver essas variáveis devemos lembrar que elas são elementos da classe, logo elas devem ser referenciadas com o `this` ([estude poo para entender essa parte](https://github.com/LucasFDutra/Minhas-apostilas/tree/master/POO)). E é justamente esse `this` o motivo pelo qual utilizamos arrow functions (sério, vê aquele vídeo para entender melhor o mótivo de utilizar arrow functions).

Um pequeno exemplo seria:

```JavaScript
state = {
  contador: 0,
};

render(){
  return (
    <h1>mostrar contador: {this.state.contador}</h1>
  );
}
```

Claro que esse mini exemplo não faz absolutamente nada, mas ele ta ai somente para você ver a sintaxe.

Agora se quisermos adicionar valor a essas variáveis. Nós não faremos simplesmente `this.state.contador = 20`, nós iremos utilizar o método `setState` (e daqui você já deve ter imaginado de onde vem aquele negocio dos hooks de colocar [var, setVar]).

O jeito de utilizar isso é da seguinte forma:

```JavaScript
this.setState({ nomeDaVariavel_1: valor });
```

> OBS.: No caso do state, fica bem obvio que o respectivo à ele com hooks seria o `useState`.

### **8.1.1 Exemplo**
Vamos replicar o exemplo de adicionar uma unidade ao valor de i quando precionamos um botão:

- Exemplo:

  ```JavaScript
  import React, { Component } from 'react';

  export default class Main extends Component {
    state = {
      i: 0
    };

    render() {
      return (
        <div>
          <p>O valor de i é: {this.state.i}</p>
          <button
            onClick={() => {
              this.setState({ i: this.state.i + 1 });
            }}
          >
            Adicionar
          </button>
        </div>
      );
    }
  }
  ```

- Saída:

    ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_20.gif?raw=true)

## 8.2 COMPONENT DID MOUNT

É o método que executa assim que o componente for mostrado em tela. Ou seja, se precisarmos fazer alguma coisa assim que o componente for mostrado em tela, iremos utilizar esse método.

A implementação desse método é feita da seguinte forma:

```JavaScript
import React, { Component } from 'react';

export default class Main extends Component {
  componentDidMount() {
    // Código..
  }

  render() {
    return <h1>Hello World</h1>;
  }
}
```

O código que ficar entre dentro do ComponentDidMount irá executar assim que o nosso componente for carregado na tela.

### **8.2.1 Equivalente com hooks**

```JavaScript
import React, { useEffect } from 'react';

const Main = () => {
  useEffect(() => {
    // código...
  }, []);

  return <div>Hello World</div>;
};

export default Main;
```

### **8.2.2 Exemplo**
Emitindo um alerta quando inicia o componete.

#### 8.2.2.1 Utilizando ciclos de vida

- Exemplo:

  ```JavaScript
  import React, { Component } from 'react';

  export default class Main extends Component {
    componentDidMount() {
      window.alert('Iniciando componente');
    }

    render() {
      return <div>Hello World</div>;
    }
  }
  ```

- Saída:

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_22.png?raw=true)

#### 8.2.2.2 Utilizando hooks

- Exemplo:

  ```JavaScript
  import React, { useEffect } from 'react';

  const MainHooks = () => {
    useEffect(() => {
      window.alert('Iniciando componente');
    }, []);

    return <div>Hello World</div>;
  };

  export default MainHooks;
  ```

- Saída:

    ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_21.png?raw=true)

OBS.: Veja que dos dois jeitos tivemos o mesmo resultado, ou nem tanto, pois utilizando `componentDidMount` o componente apareceu somente depois de clicar em `OK` na caixa de alerta, já com hooks ele apareceu junto.

## 8.3 COMPONENT DID UPDATE

Sempre que o componente sofrer alguma alteração será chamado o método `componentDidUpdate`, para ele é possivel passar três parâmetros (já são passados automaticamente pelo método `render`):
- `prevProps`: As propriedades do componente antes dele ser modificado
- `prevState`: O valor das variáveis de estado antes da modificação do componente
- `snapshot`: Esse parametro recebe o retorno da função `getSnapshotBeforeUpdate`, que também é chamada pelo método render.

  ```JavaScript
  //..
  getSnapshotBeforeUpdate(prevProps, prevState){
    // Código...
    return //alguma coisa
  }
  //...
  componentDidUpdate(prevProps, prevState, snapshot) {
    // Código...
  }
  //...
  render(){
    //...
  }
  ```

Um exemplo rápido com o snapshot seria:

```JavaScript
getSnapshotBeforeUpdate(prevProps, prevState){
  return 'Hello World';
}
//...
componentDidUpdate(prevProps, prevState, snapshot) {
  console.log(snapshot)
}
//...
render(){
  //...
}
```

Esse código iria mostrar um `Hello World` no console assim que algo no componente fosse modificado.

### **8.3.1 Equivalente com hooks**
Com hooks nós temos uma boa diferença, aqui não iremos vigiar o componente todo, somente partes específicas dele. E para isso iremos utilizar o `useEffect`.

```JavaScript
import React, { useEffect } from 'react';

const Main = () => {
  useEffect(() => {
    // Código...
  }, [/* o que estamos vigiando */]);

  return <div>Hello World</div>;
};

export default Main;
```

Isso vai fazer com que o código que está dentro da função execute assim que o que estivermos vigiando seja modificado.

### **8.3.2 Exemplo**
Vamos mostrar um alerta assim que o valor de i for modificado.

#### 8.3.2.1 Utilizando ciclos de vida

- Exemplo:

  ```JavaScript
  import React, { Component } from 'react';

  export default class Main extends Component {
    state = {
      i: 0,
    };

    componentDidUpdate(prevProps, prevState, snapshot) {
      window.alert('O valor de i foi alterado');
    }

    render() {
      return (
        <div>
          <p>O valor de i é: {this.state.i}</p>
          <button
            onClick={() => {
              this.setState({ i: this.state.i + 1 });
            }}
          >
            Adicionar
          </button>
        </div>
      );
    }
  }
  ```

- Saida:

    ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_23.gif?raw=true)

#### 8.3.2.2 Utilizando hooks

- Exemplo: 

  ```JavaScript
  import React, { useState, useEffect } from 'react';

  const Main = () => {
    const [i, setI] = useState(0);

    useEffect(() => {
      window.alert('O valor de i foi alterado');
    }, [i]);

    return (
      <div>
        <p>O Valor de i é: {i}</p>
        <button
          onClick={() => {
            setI(i + 1);
          }}
        >
          Alterar
        </button>
      </div>
    );
  };

  export default Main;
  ```

- Saída:

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_24.gif?raw=true)

## 8.4 COMPONENT DID UNMOUNT
Executa assim que o componente é desmontado.

```JavaScript
//...
componentWillUnmount() {
  // Código...
}
//...
render() {
  //...
}
```

### **8.4.1 Equivalente com hooks**
O equivalente seria deixar um `return` dentro do `useEffect`

```JavaScript
useEffect(() => {
  return () => {
    window.alert("componente desmontado");
  };
}, [i]);
```


### **8.4.2 Exemplo**

Vamos fazer com que uma mensagem seja exibida assim que o componente for desmontado, para isso vamos fazer uma modificação no arquivo `App.js`, em que ele vai desmontar o componente após 5 segundos (vou utilizar hooks para fazer a mudança de estado da variável `visible`).

- Arquivo `App.js`

  ```JavaScript
  import React, { useState } from 'react';
  import Main from './Main.js';
  import MainHooks from './MainHooks.js';

  function App() {
    const [visible, setVisible] = useState(true);

    setTimeout(() => {
      setVisible(false);
    }, 5000);

    return (
      <div className='App'>
        {visible && <Main />}
      </div>
    );
  }

  export default App;
  ```

#### 8.4.2.1 Utilizando ciclos de vida

- Exemplo:

  ```JavaScript
  import React, { Component } from 'react';

  export default class Main extends Component {
    state = {
      i: 0,
    };

    componentWillUnmount() {
      window.alert('componente sendo desmontado');
    }

    render() {
      return (
        <div>
          <p>
            O valor de i é:
            {this.state.i}
          </p>
          <button
            onClick={() => {
              this.setState({ i: this.state.i + 1 });
            }}
          >
            Adicionar
          </button>
        </div>
      );
    }
  }
  ```

- Saída:

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_25.gif?raw=true)

#### 8.4.2.2 Utilizando hooks

- Exemplo:

  ```JavaScript
  import React, { useState, useEffect } from "react";

  const Main = () => {
    const [i, setI] = useState(0);

    useEffect(() => {
      return () => {
        window.alert("componente desmontado");
      };
    }, [i]);

    return (
      <div>
        <p>
          O Valor de i é:
          {i}
        </p>
        <button
          onClick={() => {
            setI(i + 1);
          }}
        >
          Alterar
        </button>
      </div>
    );
  };

  export default Main;
  ```

- Saída: 

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_26.gif?raw=true)

**Agora que já entendeu esses conceitos de componentes, hooks e ciclos de vida, vamos dar seguimento ao exemplo principal desse material (huntweb), e vamos aprender alguns conceitos no caminho.**

# **9. HUNTWEB**

Para dar seguimento ao nosso exemplo, tenha os seus arquivos configurados da seguinte forma:

- Arquivo `src/App.js`

  ```JavaScript
  import React from 'react';

  function App() {
    return <div className='App'>Hello World</div>;
  }

  export default App;
  ```

- Arquivo `src/index.js`

  ```JavaScript
  import React from 'react';
  import ReactDOM from 'react-dom';
  import App from './App';
  import * as serviceWorker from './serviceWorker';

  ReactDOM.render(<App />, document.getElementById('root'));

  serviceWorker.unregister();
  ```

Agora como você já deve ter pensado, nós não vamos ficar utilizando o arquivo `App.js` para montar todos os nossos componentes. Nós vamos modularizar esse código.

Então agora crie uma pasta dentro de `src` chamada `components` e dentro dessa pasta você pode criar os arquivos `.js` de cada componente, ou então fazer como eu, e criar uma pasta com o nome do componente, e um arquivo `index.js` dentro dela, e posteriormente um arquivo `styles.css` para esse componente. Fazendo a gente tem dentro de cada pasta um código `js` e um `css`, deixando tudo mais organizado.

## 9.1 HEADER

Primeiro componente que criarei será um componente chamado `Header`.

- A árvore de diretórios de `src`

  ```sh
  ├── App.js
  ├── components
  │   └── Header
  │       └── index.js
  ├── index.js
  └── serviceWorker.js
  ```

Agora vamos trabalhar dentro do nosso arquivo `index.js`

De início a estrutura fica assim;

```JavaScript
import React from 'react';

const Header = () => {
  return (
    //código
  )
}

export default Header;
```

Os arquivos ficam da seguinte forma:

- Arquivo `src/components/Header/index.js`

  ```JavaScript
  import React from 'react';

  const Header = () => <header id='main-header'>JSHuntWeb</header>;

  export default Header;
  ```

- Arquivo `src/App.js`

  ```JavaScript
  import React from 'react';
  import Header from './components/Header';

  function App() {
    return (
      <div className='App'>
        <Header />
      </div>
    );
  }

  export default App;
  ```

- Saída:

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_05.png?raw=true)

Agora vamos para a estilização.

Crie dentro da pasta `components/Header` o arquivo `styles.css`, que ficará da seguinte forma:

- Arquivo `Header/styles.css`
  ```CSS
    header#main-header {
    width: 100%;
    height: 60px;
    background: #da552f;
    font-size: 18px;
    font-weight: bold;
    color: #ffffff;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  ```

O arquivo `index.js` precisa importar o `styles.css`, e isso é feito com uma linha apenas: `improt './styles.css'`

- Arquivo `src/components/Header/index.js`

  ```JavaScript
  import React from 'react';

  import './styles.css';

  const Header = () => <header id='main-header'>JSHuntWeb</header>;

  export default Header;
  ```

O resultado disso na nossa aplicação é o seguinte:

- Saída:

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_06.png?raw=true)

Mas ai você deve ter notado que ele não está exatamente do jeito que eu queria, isso é porque o html já possui algumas estilizações, e para acabar com elas, crie um arquivo `styles.css` dentro da pasta `src` e o importe para dentro de `App.js`.

- A árvore de diretórios de `src`

  ```sh
  ├── App.js
  ├── components
  │   └── Header
  │       ├── index.js
  │       └── styles.css
  ├── index.js
  ├── serviceWorker.js
  └── styles.css
  ```

- Arquivo `src/styles.css`

  ```CSS
  * {
    margin: 0;
    padding: 0;
    outline: 0;
    box-sizing: border-box;
  }

  body {
    font-family: Arial, Helvetica, sans-serif;
    background: #fafafa;
    color: #333;
  }
  ```

- Saída:

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_07.png?raw=true)

## 9.2 API

Iremos integrar nossa aplicação com uma api, e a api em questão é uma que criei durante o material de nodeJS, você consegue encontrar tal material [aqui](https://github.com/LucasFDutra/Minhas-apostilas/tree/master/NodeJS).

Mas eu vou utilizar a api montada pelo pessoal da rocketseat, pois eles possuem um dominio para ela, assim facilita minha vida (sem falar que a minha corre mais risco de dar bug do que a deles kkkkk), e também caso você não tenha feito todo o material de node será mais fácil para você pegar essa aqui, e começar a trabalhar em cima dela. O enderaço dessa api é: `https://rocketseat-node.herokuapp.com/api`

Coloque isso como `base_url` do seu insomnia e vamos começar dai.

> OBS.: Caso não saiba o que é o insomnia, vá no material de node e veja por lá. Pois é muito importante daqui para frente. A parte especifica em que falo dele está [aqui](https://github.com/LucasFDutra/Minhas-apostilas/tree/master/NodeJS#11-insomnia).

### **9.2.1 Axios**

Se você viu meu material de javaScript você viu sobre esse biblioteca, e como utilizá-la. Mas se não viu, corre lá, o link está [aqui](https://github.com/LucasFDutra/Minhas-apostilas/tree/master/JavaScript#124-axios)

Mas aqui nós vamos colocar ele na nossa aplicação de um jeito diferente, nós vamos adicionar o pacote do axios com o yarn.

```sh
yarn add axios
```

Agora crie uma pasta chamada `services` dentro da pasta `src` e dentro dessa pasta crie o arquivo `api.js`

- A árvore de diretórios de `src`

  ```sh
  ├── App.js
  ├── components
  │   └── Header
  │       ├── index.js
  │       └── styles.css
  ├── index.js
  ├── services
  │   └── api.js
  ├── serviceWorker.js
  └── styles.css
  ```

O motivo de colocar isso dentro da pasta `services` é pq assim podemos padronizar uma pasta que ficará responsável por tudo aquilo que for referente a conexões com servidor.

por hora, esse arquivo ficará da seguinte forma:

- Arquivo `src/services/api.js`

  ```JavaScript
  import axios from 'axios';

  const api = axios.create({
    baseURL: 'https://rocketseat-node.herokuapp.com/api',
  });

  export default api;
  ```

## 9.3 PAGES

E agora vamos criar nossas páginas. Então dentro de `src` crie uma pasta chamada `pages`. 

Agora vamos definir dois caminhos a serem tomados, um criando toda a aplicação utilizando o conceito de ciclos de vida e outro o de hooks. Eu irei implementar das duas formas. Sendo que primeiro irei fazer com ciclos de vida.

E como não pretendo perder muito tempo explicando todo o passo a passo de criação e lógicas das páginas, eu vou explicar tudo certinho durante a implementação com ciclos de vida, e depois vou fazer algo mais direto na implementação com hooks. Logo eu recomendo que você veja ambas, pois uma ficará com a explicação melhor (ciclos de vida) e a outra é um jeito mais fácil de fazer (hooks).

### **9.3.1 Ciclos de vida**

#### 9.3.1.1 Main

Dentro da pasta `pages` crie uma chamada `main` e dentro dela crie um arquivo chamado `index.js`. Basicamente estaremos criando a página principal da nossa aplicação.

- A árvore de diretórios de `src`

  ```sh
  ├── App.js
  ├── components
  │   └── Header
  │       ├── index.js
  │       └── styles.css
  ├── index.js
  ├── pages
  │   └── main
  │       └── index.js
  ├── services
  │   └── api.js
  ├── serviceWorker.js
  └── styles.css
  ```

Efetue a importação da página `main` para dentro do seu arquivo `App.js` e mande mostrá-la.

- Arquivo `src/App.js`

  ```JavaScript
  import React from 'react';
  import Header from './components/Header';
  import Main from './pages/main';
  import './styles.css';

  function App() {
    return (
      <div className='App'>
        <Header />
        <Main />
      </div>
    );
  }

  export default App;
  ```

#### **Vamos começar puxando as informações da nossa api.**

E como queremos puxar as informações assim que página for carregada, iremos então utilizar o `componenteDidMount` para pegar esses dados para nós.

- Arquivo `src/pages/main/index.js`

  ```JavaScript
  import React, { Component } from 'react';
  import api from '../../services/api';

  export default class Main extends Component {
    componentDidMount() {
      this.loadProducts();
    }

    loadProducts = async () => {
      const response = await api.get('/products');

      console.log(response);
    };

    render() {
      return <h1>Hello World</h1>;
    }
  }
  ```

- Saída:

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_08.png?raw=true)

Veja que o retorno do nosso log indica que os dados retornam dentro de `response.data.docs`, então faça faça a seguinte troca:

```JavaScript
console.log(response);
```

Irá virar:

```JavaScript
console.log(response.data.docs);
```

#### **Agora vamos salvar essas informações em uma variável de estado**

Como visto na seção 8 precisamos utilizar um objeto state e o método setState para podermos armazenar os dados dentro dessa variável, e como o retorno será um array, então vamos criar essa variável como sendo um array vazio.

Vamos também carregar ela dentro do componentDidMount e exibir essa informação no render.

- Arquivo `src/pages/main/index.js`

  ```JavaScript
  import React, { Component } from 'react';
  import api from '../../services/api';

  export default class Main extends Component {
    state = {
      products: [],
    };

    componentDidMount() {
      this.loadProducts();
    }

    loadProducts = async () => {
      const response = await api.get('/products');

      this.setState({ products: response.data.docs });
    };

    render() {
      return <h1>Contagem de produtos: {this.state.products.length}</h1>
    }
  }
  ```

- Saída:

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_09.png?raw=true)

#### **Agora vamos mostrar os dados retornados no formato de lista**

Vamos utilizar o método `map` para poder percorrer o nosso array de produtos, e mostraremos eles no formato de titulo (h2).

> OBS.: Caso não saiba como funciona o comando map, indico que veja [aqui](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Array/map).

- Arquivo `src/pages/main/index.js`

  ```JavaScript
  import React, { Component } from 'react';
  import api from '../../services/api';

  export default class Main extends Component {
    state = {
      products: [],
    };

    componentDidMount() {
      this.loadProducts();
    }

    loadProducts = async () => {
      const response = await api.get('/products');

      this.setState({ products: response.data.docs });
    };

    render() {
      return (
        <div className="product-list">
          {this.state.products.map(product => {
            return (
              <h2 key={product._id}>{product.title}</h2>
            );
          })}
        </div>
      );
    }
  }
  ```

> OBS.: O atributo `key` em `h2` está ali pois o `react` pede que o elemento seguinte ao `map` receba uma `key` única para cada interação do `map`. E nesse caso nós retiramos a `key` do id do nosso produto (quando demos o `console.log` esse `_id` estava lá).
>
> > OBS.: O elemento que precisa da `key` é somente o proximo elemento afrente do map, se esse elemento possuir sub-elementos, os sub-elementos não precisam de uma `key`.

- Saída:

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_10.png?raw=true)

Mas você viu que assim nós mostramos somente os titulos, e quero mostrar tudo. Então vamos dar uma melhorada nisso aqui.

Para isso vamos colocar tudo em formato de `artigo` (nenhum motivo especial, é só porque eu quis) e vamos deixar um botão `Acessar`, que futuramente nos levará à uma outra página (mas no momento ele não fará nada).

- Arquivo `src/pages/main/index.js`

  ```JavaScript
  import React, { Component } from 'react';
  import api from '../../services/api';

  export default class Main extends Component {
    state = {
      products: [],
    };

    componentDidMount() {
      this.loadProducts();
    }

    loadProducts = async () => {
      const response = await api.get('/products');

      this.setState({ products: response.data.docs });
    };

    render() {
      return (
        <div className='product-list'>
          {this.state.products.map((product) => (
            <article key={product._id}>
              <strong>{product.title}</strong>
              <p>{product.description}</p>
              <a href=''>Acessar</a>
            </article>
          ))}
        </div>
      );
    }
  }
  ```

- Saída:

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_11.png?raw=true)

O código funciona bem, mas vamos deixar ele um pouco menos verboso (sem muita coisa escrita) e vamos diminuir isso aqui: `this.state.products.map`. Até para facilitar em futuras chamadas. Vamos fazer o seguinte: Declare uma constante chamada `products` que receberá o `this.state`, assim podemos utilizar somento o `products` deixando método `render` da seguinte forma:

- método `render`

  ```JavaScript
  render() {
    const { products } = this.state;

    return (
      <div className='product-list'>
        {products.map((product) => (
          <article key={product._id}>
            <strong>{product.title}</strong>
            <p>{product.description}</p>
            <a href=''>Acessar</a>
          </article>
        ))}
      </div>
    );
  }
  ```

#### **Agora vamos estilizar a nossa página**

Como você deve ter visto, a nossa `div` pertence a uma classe, isso é porque eu quero dar uma estilização para ela, e farei isso com o arquivo `styles.css` que ficará na mesma pasta que o arquivo `index.js`

- A árvore de diretórios de `src`

  ```sh
  ├── App.js
  ├── components
  │   └── Header
  │       ├── index.js
  │       └── styles.css
  ├── index.js
  ├── pages
  │   └── main
  │       ├── index.js
  │       └── styles.css
  ├── services
  │   └── api.js
  ├── serviceWorker.js
  └── styles.css
  ```

Lembresse de importar os estilos para dentro do `index.js` com o comando `import './styles.css';`

- Arquivo `src/pages/main/styles.css`

  ```CSS
  .product-list {
    max-width: 700px;
    margin: 20px auto 0;
    padding: 0 20px;
  }

  .product-list article {
    background: #ffffff;
    border: 1px solid #dddddd;
    border-radius: 5px;
    padding: 20px;
    margin-bottom: 20px;
  }

  .product-list article p {
    font-size: 16px;
    color: #999999;
    margin-top: 5px;
    line-height: 24px;
  }

  .product-list article a {
    height: 42px;
    border-radius: 5px;
    border: 2px solid #da552f;
    background: none;
    margin-top: 10px;
    color: #da552f;
    font-weight: bold;
    font-size: 16px;
    text-decoration: none; /*retira o traço embaixo da palavra */
    display: flex;
    justify-content: center;
    align-items: center;
    transition: all 0.2s; /*tudo que acontecer no botão terá um efeito de transição de 0.2s*/
  }

  /* hover: quando o usuário passar o mouse sobre o botão */

  .product-list article a:hover {
    background: #da552f;
    color: #ffffff;
  }
  ```

Depois de aplicar todos esses estilos, nós temos o seguinte resultado:

- Saída:

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_12.png?raw=true)

#### 9.3.1.2 Página anterior/proxima

Se você notou bem quando puxamos os dados no nosso console, tinha marcado lá que tinhamos duas páginas, isso porque na implementação do servidor foi feito esse esquema de dividir os conteúdos em páginas com no máximo 10 itens em cada.

O resultado disso é que nossa aplicação não fica carregando toda a base de dados de uma só vez, então precisamos mandar ela ficar trocando de página. Basicamente é esse esquema ai da imagem que temos nas pesquisas do google.

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_13.png?raw=true)

#### **Agora vamos inserir os botões**

Para fazermos isso vamos criar dois botões, um de anterior e um de próximo. O código para isso é extremamente simples. Vamos adicionar uma div logo após o final da página, contendo dois botões.

- Inserir botões:

  ```JavaScript
  <div className='actions'>
    <button>Anterior</button>
    <button>Próximo</button>
  </div>
  ```

O problema aqui é que o return não pode retornar duas `div`, então precisamos colocar tudo dentro de uma única `div`. No final das contas o código final fica assim:

- Arquivo `src/pages/main/index.js`

  ```JavaScript
  render() {
    const { products } = this.state;

    return (
      <div className='product-list'>
        {products.map((product) => (
          <article key={product._id}>
            <strong>{product.title}</strong>
            <p>{product.description}</p>
            <a href=''>Acessar</a>
          </article>
        ))}
        <div className='actions'>
          <button>Anterior</button>
          <button>Próximo</button>
        </div>
      </div>
    );
  }
  ```

  > OBS.: Eu preferi mostrar apenas o render, para não ficar colocando códigos muito extensos aqui.

- Saída:

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_14.png?raw=true)

#### **Agora vamos partir para o css e fazer esse negocio ficar bonitão.**

> OBS.: Como o arquivo css já está grande, eu vou colocar abaixo somente a parte nova. Mas o arquivo como um todo ficará com tudo o que tinha antes, mais esse trecho.

- Arquivo `src/pages/main/styles.css`

  ```CSS
  .product-list .actions {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
  }

  .product-list .actions button {
    padding: 10px;
    border-radius: 5px;
    border: 0;
    background: #da552f;
    color: #ffffff;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
  }

  .product-list .actions button:hover {
    opacity: 0.7;
  }
  ```

O resultado disso é:

- Saída:

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_15.png?raw=true)

#### **Agora vamos fazer esses botões funcionarem**

Vamos primeiro indicar para nossos botões o que eles devem fazer ao serem clicados: Que no caso é ir para as funções `prevPage` e `nextPage`.

> OBS.: Como criaremos essas duas funções dentro da classe, temos que referênciá-las com o `this`

- onClick

  ```JavaScript
  <div className='actions'>
    <button onClick={this.prevPage}>Anterior</button>
    <button onClick={this.nextPage}>Próximo</button>
  </div>
  ```

Agora eu poderia já sair criando as funções, mas não iria adiantar de nada, pois nós não temos salvo a informação de qual página estamos. Então primeiro precisamos fazer com que essa informação chegue até nós.

Para isso vamos criar uma nova varável dentro do objeto state, que terá essa função. Chamarei ela de `productInfo` que será um objeto vazio, que receberá não somente as informações de página, mas também doas as informações extras que vem da nossa api (com extras eu quero dizer o que não são dados).

- Informações a serem salvas

  ```JavaScript
  {
    "total": 13,
    "limit": 10,
    "page": 1,
    "pages": 2
  }
  ```

Então vamos lá. Se o `response.data` retorna tudo isso mais o `docs`, então nós precisamos fazer com que `productInfo` receba os dados vindos de `response.data` exceto o `data.docs`.

Primeiro vamos adicionar essa variável ao state.

- State

  ```JavaScript
  state = {
    products: [],
    productInfo: {},
  };
  ```

E precisamos agora fazer uma modificação no `loadProducts` adicionando a linha

```JavaScript
const { docs, ...productInfo } = response.data;
```

Essa sintaxe estranha está igualando o objeto criado na esquerda com o objeto da direita, sendo que o objeto da esquerda possui dois campos: `docs`, e `productInfo`. Mas do jeito que está ali está acontecendo o seguinte: Pega tudo que vier de `response.data` o que for `docs` ficará dentro de `docs`, e o restante ficará dentro de `productInfo`.

E modificar a linha de `setState`

```JavaScript
this.setState({ products: response.data.docs, productInfo: productInfo });
```

Apesar dessa sintaxe estar correta, ela é um tanto quanto feia, e podemos reduzir ela da seguinte forma (coisas do javaScript):

Se `const { docs, ...productInfo } = response.data;` então `response.data.docs = docs`, logo podemos fazer `products: docs`.

Se `productInfo` escreve igual a `productInfo` e nós estamos atribuindo `productInfo` à `productInfo`, então faz sentido utilizarmos apenas `productInfo`.

E o nome disso é `Destructuring assignment`. E essa essa explicação toda estranha foi proposital, pois esse negocio é esquesito de mais, mas no final das contas é bem simples: Se algo for atribuido a algo com mesmo nome, então podemos abreviar tudo utilizando somente o nome desse algo. Em resumo, para o nosso caso `productInfo: productInfo` é equivalente a `productInfo`.

Mas para aprender mais sobre `Destructuring assignment` clique [aqui](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/Atribuicao_via_desestruturacao).

E agora também preciso modificar a linha

```JavaScript
loadProducts = async () => {
  const response = await api.get('/products');
  //...
```

para:

```JavaScript
loadProducts = async (page = 1) => {
  const response = await api.get(`/products?page=${page}`);
  //...
```

Esse endereço é valido apenas para essa nossa api, e isso acontece por conta do modo como ela foi construida para navegar entre páginas. Então se quiser entender melhor como isso funciona, você precisará ver o material de nodeJS.

Mas basicamente o método `loadProducts` está recebendo qual página ele deve carregar, sendo que por default ele vai para a página 1.

- Assim nosso `loadProducts` ficará da seguinte forma:

  ```JavaScript
  loadProducts = async (page = 1) => {
    const response = await api.get(`/products?page=${page}`);

    const { docs, ...productInfo } = response.data;

    this.setState({ products: docs, productInfo });
  };
  ```

Agora sim, agora iremos criar as duas funções de referentes as mudanças de páginas:

- nextPage

  ```JavaScript
  nextPage = () => {
    const page = parseInt(this.state.productInfo.page);

    if (page === this.state.productInfo.pages) return;

    const pageNumber = page + 1;

    this.loadProducts(pageNumber);
  };
  ```

Uma explicação desse método é que ele avalia em que página estamos, e se ela é igual a ultima página, e se for igual, ele retorna nada e para por aqui mesmo. Mas se não for, ele vai passar para o método `loadProducts` a página atual mais 1.

> OBS.: O valor da página em `productInfo` é retornado com uma string, por isso eu precisei converter para inteiro, para que pudesse fazer a comparação com `pages` (que é um inteiro) e para somar 1 ao valor da página.

Ai agora, como você já deve imaginar, o código para página anterior será muito parecido, basta verificarmos se estamos na primeira página, e caso não estejamos, vamos mandar para o load products a página atual menos 1.

- prevPage

  ```JavaScript
  prevPage = () => {
    const page = parseInt(this.state.productInfo.page);

    if (page === 1) return;

    const pageNumber = page - 1;

    this.loadProducts(pageNumber);
  };
  ```

Fazendo o teste aqui o resultado foi esse:

- Saída:

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_16.gif?raw=true)

Uma coisa que podemos fazer é desabilitar os botões de anterior e próximo quando estivermos respectivamente na primeira e última página. Para isso vamos adicionar a propriedade `disabled` nos nossos botões, com essas condições dentro.

#### 9.3.1.3 Navegação

Agora estamos encaminhando para criarmos a página que irá exibir os detalhes do produto (botão `Acessar`). Mas primeiro vamos configurar a navegação.

Primeiro instale a biblioteca que fará esse esquema de navegação para nós:

```sh
yarn add react-router-dom
```

Agora vamos criar dentro da pasta `src` um arquivo chamado `routes.js`

- A árvore de diretórios de `src`
  ```sh
  ├── App.js
  ├── components
  │   └── Header
  │       ├── index.js
  │       └── styles.css
  ├── index.js
  ├── pages
  │   └── main
  │       ├── index.js
  │       └── styles.css
  ├── routes.js
  ├── services
  │   └── api.js
  ├── serviceWorker.js
  └── styles.css
  ```

O arquivo de rotas serve para trabalharmos as rotas da barra de url do nosso navegador, ou seja. É aqui que iremos definir aqueles urls tipo: /home, /products, entre outros. E esse arquivo fica da seguinte forma:

- Arquivo `src/routes.js`

  ```JavaScript
  import React from 'react';
  import { BrowserRouter, Switch, Route } from 'react-router-dom';
  import Main from './pages/main';

  const Routes = () => (
    <BrowserRouter>
      <Switch>
        <Route path='/' component={Main} />
      </Switch>
    </BrowserRouter>
  );

  export default Routes;
  ```

- `BrowserRouter`: Utilizaremos as rotas através de um browser.
- `Switch`: Vai permitir que apenas uma única rota seja chamada ao mesmo tempo. Ou seja, com o react-router-dom nós podemos fazer com que duas páginas sejam acessadas ao mesmo tempo, mas o Switch evita isso.
- `Route`: Define uma rota.

No caso, o que estamos fazendo aqui é dizer que quando nosso navegador estiver no endereço `http://localhost:3000/` vamos executar o componente `Main`.

Então se tivermos mais rotas, que levam a outros componentes, vamos ter que adicioná-las aqui.

Mas para fazer a nossa aplicação reconhecer esse arquivo como o "gestor de rotas", precisamos adicioná-lo ao nosso `App.js`, sendo assim:

- Arquivo `src/App.js`

  ```JavaScript
  import React from 'react';
  import Header from './components/Header';
  import './styles.css';
  import Routes from './routes';

  function App() {
    return (
      <div className='App'>
        <Header />
        <Routes />
      </div>
    );
  }

  export default App;
  ```

Veja que ao em vez de exibir o `Main` dentro da div, eu mandei exibir `Routes`. Agora pronto, sempre que adicionarmos uma página ela deve ser indicada dentro do arquivo `routes.js` com o respectivo caminho para ela.

#### 9.3.1.4 Product

Agora vamos criar a página product, que conterá as informações do produto, e será exibida assim que clicarmos no botão `Acessar` na página main.

Para começar, vamos criar dentro de `src` a pasta da página, ou seja, uma pasta chamada `product` contendo os arquivos `index.js` e `styles.js`.

E por hora vamos trabalhar com o `index.js`, e depois com o `styles.js`, mas já pode criá-lo ai.

- A árvore de diretórios de `src`

  ```sh
  ├── App.js
  ├── components
  │   └── Header
  │       ├── index.js
  │       └── styles.css
  ├── index.js
  ├── pages
  │   ├── main
  │   │   ├── index.js
  │   │   └── styles.css
  │   └── product
  │       ├── index.js
  │       └── styles.css
  ├── routes.js
  ├── services
  │   └── api.js
  ├── serviceWorker.js
  └── styles.css
  ```

#### Arquivo pages/product/index.js

Para fazer um teste inicial se está tudo funcionando, vamos colocar o seguinte código em `product/index.js`

- Arquivo `src/pages/product/index.js`

  ```JavaScript
  import React, { Component } from 'react';

  export default class Product extends Component {
    render() {
      return (
        <div>Hello World</div>
      );
    }
  }
  ```

> OBS.: Vamos voltar nesse arquivo posteriormente, por hora ele ficará com essa cara somente para fazermos o teste das rotas.

#### Arquivo src/routes.js

E vamos adicionar essa rota ao arquivo `routes.js`, sendo que essa rota será `http://localhost:3000/product`

- Arquivo `src/routes.js`

  ```JavaScript
  import React from 'react';
  import { BrowserRouter, Switch, Route } from 'react-router-dom';
  import Main from './pages/main';
  import Product from './pages/product';

  const Routes = () => (
    <BrowserRouter>
      <Switch>
        <Route exact path='/' component={Main} />
        <Route path='/products/:id' component={Product} />
      </Switch>
    </BrowserRouter>
  );

  export default Routes;
  ```

> OBS.: Esse arquivo de rotas não vai mudar

Deixa eu explicar o que está acontecendo em:

- `/products/:id`: A rota precisa receber um parâmetro chamado id, pois eu preciso mostrar apenas as informações do produto que eu cliquei para saber mais. Logo eu preciso identificar esse produto. E essa identificação será passada pela rota, assim eu posso mostrar a página com as informações daquele produto em específico.
- `exact`: O `react-router-dom` faz um comparativo entre a url que está no browser e a url que está dentro do `path`, e caso ela seja correspondente ele para de olhar as proximas rotas e mostra a primeira que encontrou. De forma exemplificada: Suponha que temos dois nomes: João e João Antonio. Se mandarmos o `react-router-dom` procurar por `João Antonio` ele vai primeiro olhar para `João` (já que é o primeiro item da lista) e vai falar "uhm.. não é que parece, deve ser isso... nem vou procurar mais". Ou seja, ele não vai mostrar `João Antonio`, vai mostar `João`. Se colocarmos o comando `exect` antes de `João` ele vai entender que se for pra ser `João`, o temo de pesquisa tem que ser exatametente `João`, e como não é ele vai para o proximo.

> OBS.: Como o segundo item (`'/products/:id'`) é o ultimo, não faz sentido ele receber o `exact`, pois o `react-router-dom` vai parar a pesquisa nele de um jeito ou de outro.

Uma dica aqui seria jogar no seu navegador o endereço `http://localhost:3000/products/3` (pode ser qualquer número de id) com e sem o `exact`, você vai ver que com ele aparecerá a mensagem `Hello world`, e sem ele vamos cair na página `main`.

#### Arquivo pages/main/routes.js

Continuando com as nossas modificações de arquivos, vamos agora para dentro do arquivo da página `main`, e lá devemos configurar o botão `Acessar` para nos levar para a rota `/products/:id`.

Para isso vamos primeiramente importar um componente chamado `Link` que vem do `react-router-dom`, onde estamos utilizando a tag `<a>` vamos trocar pelo `<Link>` e trocaremos o `href` por `to`, e o link de redirecionamento será "/products/id". Sendo que esse id é o id referente ao produto em que esse elemento será criado.

Para melhorar o entendimento sobre isso, vou mostar essa parte do código antes e como ela deve ficar:

- Antes:

  ```JavaScript
  render() {
    //Codigos...
    <a href="">Acessar</a>
  }
  ```
- Depois:

  ```JavaScript
  import { Link } from 'react-router-dom';
  //Codigos...
  render(){
    //Codigos...
    <Link to={`/products/${products._id}`}>Acessar</Link>
  }
  ```

O arquivo `index.js` da página `main` fica da seguinte forma

- Arquivo `src/pages/main/index.js`

  ```JavaScript
  import React, { Component } from 'react';
  import { Link } from 'react-router-dom';
  import api from '../../services/api';
  import './styles.css';

  export default class Main extends Component {
    state = {
      products: [],
      productInfo: {},
    };

    componentDidMount() {
      this.loadProducts();
    }

    loadProducts = async (page = 1) => {
      const response = await api.get(`/products?page=${page}`);

      const { docs, ...productInfo } = response.data;

      this.setState({ products: docs, productInfo });
    };

    prevPage = () => {
      const page = parseInt(this.state.productInfo.page);

      if (page === 1) return;

      const pageNumber = page - 1;

      this.loadProducts(pageNumber);
    };

    nextPage = () => {
      const page = parseInt(this.state.productInfo.page);

      if (page === this.state.productInfo.pages) return;

      const pageNumber = page + 1;

      this.loadProducts(pageNumber);
    };

    render() {
      const { products } = this.state;

      return (
        <div className='product-list'>
          {products.map((product) => (
            <article key={product._id}>
              <strong>{product.title}</strong>
              <p>{product.description}</p>
              <Link to={`/products/${product._id}`}>Acessar</Link>
            </article>
          ))}
          <div className='actions'>
            <button onClick={this.prevPage}>Anterior</button>
            <button onClick={this.nextPage}>Próximo</button>
          </div>
        </div>
      );
    }
  }
  ```

> OBS.: Esse arquivo não sofrerá mais nenhuma alteração.

Agora se você clicar em qual um dos botões de acesso você irá cair na página de produtos, que atualmente irá exibir sempre a mensagem `Hello World`.

Veja na imagem abaixo que quando clicamos no botão a url muda de acordo com o id daquele produto, e isso já indica que está tudo funcionando.

- Saída:

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_17.gif?raw=true)

#### Arquivo pages/product/index.js

Agora vamos voltar a página dos produtos, e vamos colocar as informações que queremos mostrar dentro dela.

A lógica aqui não é muito diferente do que já fizemos na página main. Vamos carregar um componente assim que ele inicializar (componentDidMount) e vamos colocar isso dentro de uma variável objeto (state). E iremos mostrar isso na tela.

A diferença é que não criarei uma função `loadProducts` (poderia, mas não vou) e carregarei tudo direto no `componentDidMount`, porém como utilizarei o método `get` dentro dele, e o `get` é assincrono, eu preciso indicar isso para o `componentDidMount`, logo eu preciso escrever `async componentDidMount() {...}`.

- Arquivo `src/pages/products/index.js`

  ```JavaScript
  import React, { Component } from 'react';
  import api from '../../services/api';
  import './styles.css';

  export default class Product extends Component {
    state = {
      product: {}
    };

    async componentDidMount() {
      const { id } = this.props.match.params;

      const response = await api.get(`/products/${id}`);

      this.setState({ product: response.data });
    }

    render() {
      const { product } = this.state;

      return (
        <div className="product-info">
          <h1>{product.title}</h1>
          <p>{product.description}</p>
          <p>
            URL: <a href={product.url}>{product.url}</a>
          </p>
        </div>
      );
    }
  }
  ```

> OBS.: `this.props.match.params` retorna um objeto (faça um console.log nisso ai que você vai ver), e dentre os itens desse objeto o id.

- Saída:

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_18.png?raw=true)

Agora aplicando a estilização com o arquivo `styles.css` teremos:

- Arquivo `src/pages/products/styles.css`
  ```CSS
  .product-info {
    max-width: 700px;
    margin: 20px auto 0;
    background: #ffffff;
    border-radius: 5px;
    border: 1px solid #dddddd;
    padding: 20px;
  }

  .product-info h1 {
    font-size: 32px;
  }

  .product-info p {
    color: #666666;
    line-height: 24px;
    margin-top: 5px;
  }

  .product-info p a {
    color: #069;
  }
  ```

- Saída:

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React/Imagens/Figura_19.png?raw=true)

### **9.3.2 Hooks**

- Árvore de diretórios

  ```sh
  ├── src
  │   ├── App.js
  │   ├── components
  │   │   └── Header
  │   │       ├── index.js
  │   │       └── styles.css
  │   ├── index.js
  │   ├── pages
  │   │   ├── main
  │   │   │   ├── index.js
  │   │   │   └── styles.css
  │   │   └── product
  │   │       ├── index.js
  │   │       └── styles.css
  │   ├── routes.js
  │   ├── services
  │   │   └── api.js
  │   ├── serviceWorker.js
  │   └── styles.css
  ├── yarn-error.log
  └── yarn.lock
  ```

- Arquivo `/src/App.js`

  ```JavaScript
  import React from 'react';
  import Header from './components/Header';
  import './styles.css';
  import Routes from './routes';

  function App() {
    return (
      <div className='App'>
        <Header />
        <Routes />
      </div>
    );
  }

  export default App;
  ```

- Arquivo `/src/index.js`

  ```JavaScript
  import React from 'react';
  import ReactDOM from 'react-dom';
  import App from './App';
  import * as serviceWorker from './serviceWorker';

  ReactDOM.render(<App />, document.getElementById('root'));

  serviceWorker.unregister();
  ```

- Arquivo `/src/routes.js`

  ```JavaScript
  import React from 'react';
  import { BrowserRouter, Switch, Route } from 'react-router-dom';
  import Main from './pages/main';
  import Product from './pages/product';

  const Routes = () => (
    <BrowserRouter>
      <Switch>
        <Route exact path='/' component={Main} />
        <Route path='/products/:id' component={Product} />
      </Switch>
    </BrowserRouter>
  );

  export default Routes;
  ```

- Arquivo `/src/components/Header/index.js`

  ```JavaScript
  import React from 'react';

  import './styles.css';

  const Header = () => <header id='main-header'>JSHuntWeb</header>;

  export default Header;
  ```

- Arquivo `/src/components/Header/styles.css`

  ```CSS
  header#main-header {
    width: 100%;
    height: 60px;
    background: #da552f;
    font-size: 18px;
    font-weight: bold;
    color: #ffffff;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  ```

- Arquivo `/src/pages/main/index.js`

  ```JavaScript
  import React, { useState, useEffect } from 'react';
  import { Link } from 'react-router-dom';
  import api from '../../services/api';
  import './styles.css';

  const Main = () => {
    const [products, setProducts] = useState([]);
    const [productInfo, setProductInfo] = useState({});

    useEffect(() => {
      loadProducts();
    }, []);

    const loadProducts = async (page = 1) => {
      const response = await api.get(`/products?page=${page}`);

      const { docs, ...productInfo } = response.data;
      setProducts(docs);
      setProductInfo(productInfo);
    };

    const prevPage = () => {
      const page = parseInt(productInfo.page);

      if (page === 1) return;

      const pageNumber = page - 1;

      loadProducts(pageNumber);
    };

    const nextPage = () => {
      const page = parseInt(productInfo.page);
      if (page === productInfo.pages) {
        return;
      }

      const pageNumber = page + 1;
      loadProducts(pageNumber);
    };

    return (
      <div className='product-list'>
        {products.map((product) => (
          <article key={product._id}>
            <strong>{product.title}</strong>
            <p>{product.description}</p>
            <Link to={`/products/${product._id}`}>Acessar</Link>
          </article>
        ))}
        <div className='actions'>
          <button onClick={prevPage}>Anterior</button>
          <button onClick={nextPage}>Próximo</button>
        </div>
      </div>
    );
  };

  export default Main;
  ```

- Arquivo `/src/pages/main/styles.css`

  ```CSS
  .product-list {
    max-width: 700px;
    margin: 20px auto 0;
    padding: 0 20px;
  }

  .product-list article {
    background: #ffffff;
    border: 1px solid #dddddd;
    border-radius: 5px;
    padding: 20px;
    margin-bottom: 20px;
  }

  .product-list article p {
    font-size: 16px;
    color: #999999;
    margin-top: 5px;
    line-height: 24px;
  }

  .product-list article a {
    height: 42px;
    border-radius: 5px;
    border: 2px solid #da552f;
    background: none;
    margin-top: 10px;
    color: #da552f;
    font-weight: bold;
    font-size: 16px;
    text-decoration: none; /*retira o traço embaixo da palavra */
    display: flex;
    justify-content: center;
    align-items: center;
    transition: all 0.2s; /*tudo que acontecer no botão terá um efeito de transição de 0.2s*/
  }

  /* hover: quando o usuário passar o mouse sobre o botão */

  .product-list article a:hover {
    background: #da552f;
    color: #ffffff;
  }

  .product-list .actions {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
  }

  .product-list .actions button {
    padding: 10px;
    border-radius: 5px;
    border: 0;
    background: #da552f;
    color: #ffffff;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
  }

  .product-list .actions button:hover {
    opacity: 0.7;
  }
  ```

- Arquivo `/src/pages/product/index.js`

  ```JavaScript
  import React, { useState, useEffect } from "react";
  import api from "../../services/api";
  import "./styles.css";

  const Product = props => {
    const [product, setProduct] = useState({});

    useEffect(() => {
      const loadProduct = async () => {
        const { id } = props.match.params;

        const response = await api.get(`/products/${id}`);

        setProduct(response.data);
      };
      loadProduct();
    }, []);

    return (
      <div className="product-info">
        <h1>{product.title}</h1>
        <p>{product.description}</p>
        <p>
          URL: <a href={product.url}>{product.url}</a>
        </p>
      </div>
    );
  };

  export default Product;
  ```

- Arquivo `/src/pages/product/styles.css`

  ```CSS
  .product-info {
    max-width: 700px;
    margin: 20px auto 0;
    background: #ffffff;
    border-radius: 5px;
    border: 1px solid #dddddd;
    padding: 20px;
  }

  .product-info h1 {
    font-size: 32px;
  }

  .product-info p {
    color: #666666;
    line-height: 24px;
    margin-top: 5px;
  }

  .product-info p a {
    color: #069;
  }
  ```

- Arquivo `/src/services/api.js`

  ```JavaScript
  import axios from 'axios';

  const api = axios.create({
    baseURL: 'https://rocketseat-node.herokuapp.com/api',
  });

  export default api;
  ```