# Apostila de React-Native

Autor: Lucas Felipe Dutra

**ANTES DE QUALQUER COISA, VEJA ESSE VIDEO [AQUI](https://www.youtube.com/watch?v=9w3o9NHXqu0&list=PLMdYygf53DP5Sc6yFYs6ZmjsuuA2fu0TK) PARA APRENDER MAIS SOBRE CLEAN CODE**

# Dicas

- [Curso da Rocketseat](https://skylab.rocketseat.com.br/node/curso-react-native/lesson/scroll-infinito-com-flat-list)
- [Material de JavaScript](https://github.com/LucasFDutra/Minhas-apostilas/tree/master/JavaScript)
- [Material de React](https://github.com/LucasFDutra/Minhas-apostilas/tree/master/React)
- [Material de Node](https://github.com/LucasFDutra/Minhas-apostilas/tree/master/NodeJS)
- [Documentação](https://facebook.github.io/react-native/docs/getting-started)

# Sumário

- [**1. INTRODUÇÃO**](#1-introdução)
  - [1.1 INICIANDO UM PROJETO](#11-iniciando-um-projeto)
- [**2. TAGS JSX**](#2-tags-jsx)
- [**3. ROTAS**](#3-rotas)
- [**4. ESTILIZAÇÃO**](#4-estilização)
- [**5. EXEMPLO**](#5-exemplo)
- [**6. API**](#6-api)
- [**7. EXIBINDO LISTA DE DADOS**](#7-exibindo-lista-de-dados)
  - [7.1 ESTILIZAÇÃO DA LISTA](#71-estilização-da-lista)
- [**8. SCROLL ÍNFINITO**](#8-scroll-ínfinito)
- [**9. NOVA PÁGINA**](#9-nova-página)
- [**10. RESUMINDO**](#10-resumindo)

# **1. INTRODUÇÃO**

O react-native é uma biblioteca do javaScript que permite utilizarmos códigos em javaScript para programar dispositivos móveis. Sendo que o mesmo código servirá para Android e IOS.

Como você deve imaginar, existe sim uma relação entre react e react-native, tudo que fazemos no react também é válido e útilizado aqui (a grosso modo, react-native é nada mais do que o react para Mobile).

Então antes de iniciar seus estudos aqui com react-native, estude react, pois assim sua curva de aprendizado será muito menor.

- O que temos de igual?

  - O conceito de componentes;
  - Hooks;
  - Ciclos de vida;
  - jsx

- O que temos de diferente?
  - Criação de um projeto;
  - As tags jsx são diferentes do html convencional;
  - Não utilizamos CSS;
  - Como criar as rodas.

Para o que é igual ao react deverá ser estudado pelo material de react, disponível [aqui](https://github.com/LucasFDutra/Minhas-apostilas/tree/master/React).

Já o que for diferente irei abordar aqui, seguindo um exemplo (O qual é exatamente igual ao exemplo criado no material de react). Uma boa observação sobre o exemplo que utilizarei, é que vou dar preferencia por programar com ciclos de vida, não tem nenhum motivo específico, é só porque quero seguir mais a risca o tutorial da rocketseat.

## 1.1 INICIANDO UM PROJETO

Para iniciar um projeto em react-native siga os passos que estão descritos nesse repositório [aqui](https://github.com/LucasFDutra/Ambiente-React-E-React-native-Com-ESlint-Airbnb). Nele você vai ver como se instala todas as ferramentas necessárias, como se configura o ambiente de desenvolvimento, como iniciar uma aplicação e como utilizar o seu celular como sendo o hardware em que seu programa estará rodando.

# **2. TAGS JSX**

Como o react-native estará rodando em um dispositivo móvel e trabalhando com componentes nativos do sistema, é bem plausivel de pensar que ele não iria aceitar tags HTML normais. Mas para manter essa sintaxe (jsx) o react-native possui suas próprias tags (consulte a documentação para ver todas), sendo que duas das principais são as tags `View` e `Text`. A `View` seria o equivalente às `div`s do HTML e o `Text` representa todos os componentes de texto do programa, porém sem estilização própria, ou seja, onde antes teríamos `<p/>`, `<h1/>`, `<strong/>`, dentre outras, agora temos apenas o `Text`, que se quisermos podemos utilizá-lo.

Um detalhe importante, é que no react-native jamais poderemos colocar um texto fora da div `Text`. Por exemplo: Vamos dar um nome à um botão utilizando react, e depois react-native

- react

  ```JavaScript
  <button>press</button>
  ```

- react-native

  ```JavaScript
  <Button>
    <Text>press</Text>
  </Button>
  ```

# **3. ROTAS**

Para facilitar a navegação entre páginas vamos ter sempre um arquivo de rotas, que será responsável pela transição entre as páginas e o como essa transição acontecerá.

A transição pode acontecer clicando um botão, arrastando para o lado, através de um menu lateral, enfim, temos diversas formas de fazer isso. Para ver como fazer cada uma delas, consulte a documentação nesse ponto [aqui](https://facebook.github.io/react-native/docs/navigation).

Vamos começar criando esse gerenciamento de rotas dividindo nosso programa em páginas e criando o arquivo de rotas. Para isso crie uma pasta `src` que é onde ficarão todos os nossos códigos. Dentro dela crie os arquivos `routes.js`, `index.js`, a pasta pages com o arquivo `main.js`. E também apague o arquivo `App.js`.

- Árvore de diretórios do programa
  ```sh
  ├── android
  ├── app.json
  ├── babel.config.js
  ├── index.js
  ├── ios
  ├── metro.config.js
  ├── node_modules
  ├── package.json
  ├── src
  │   ├── index.js
  │   ├── pages
  │   │   └── main.js
  │   └── routes.js
  ├── __tests__
  │   └── App-test.js
  └── yarn.lock
  ```

Para que as rotas funcionem, precisamos adicionar uma lib ao projeto. Digite no terminal

```sh
yarn add react-navigation@2.18.3
```

Agora vamos mostrar as modificações necessárias em cada código já existente e o que colocar em cada um dos criados

- Arquivo `Index.js`

  ```JavaScript
  import { AppRegistry } from 'react-native';
  import App from './src';
  import { name as appName } from './app.json';

  AppRegistry.registerComponent(appName, () => App);
  ```

- Arquivo `/src/index.js`

  ```JavaScript
  import React from 'react';
  import Routes from './routes';

  const App = () => <Routes />;

  export default App;
  ```

- Arquivo `/src/pages/main.js`

  ```JavaScript
  import React, { Component } from 'react';
  import { View, Text } from 'react-native';

  export default class Main extends Component {
    static navigationOptions = {
      title: 'JShunt',
    };

    render() {
      return (
        <View>
          <Text>Hello World</Text>
        </View>
      );
    }
  }
  ```

- Arquivo `/src/routes.js`

  ```JavaScript
  import { createStackNavigator } from 'react-navigation';
  import Main from './pages/main';

  export default createStackNavigator(
    {
      Main,
    },
    {
      navigationOptions: {
        headerStyle: {
          backgroundColor: '#DA552F',
        },
        headerTintColor: '#FFF',
      },
    },
  );
  ```

> OBS.: Esse parte do `navigationOptions` é para estilizar o header para toda a aplicação.

Então nossa aplicação começa em `index.js`, que procura por um `App` dentro da pasta `src`, e esse `App` foi exportado de dentro de `/src/index.js`, que nos levou para as rotas em `/src/routes.js`, que agora controla a navegação entre as páginas, mas que por hora nos leva somente para a página `main` dentro de `/src/pages/main.js`.

Nesse momento nossa aplicação está apenas mostrando um `Hello world` na tela do celular.

- Saída

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React-Native/Imagens/Figura_01.png?raw=true)

# **4. ESTILIZAÇÃO**

Agora que já estamos mostrando os dados na tela precisando mostrar eles de uma forma mais agradável visualmente falando.

No react e no JavaScript nós fazemos uso do CSS, mas aqui não temos isso, mas para manter a semelhança o react-native útiliza algo bem próximo, o `StyleSheets`. Que é uma função do react-native em que escrevemos as nossas esterilizações, utilizando uma sintaxe muito semelhante ao CSS.

Sendo que todos os atributos de estilo css que eram escritos da forma `palavra1-palavra2`, agora será escrito da forma `palavra1Palavra2`. Exemplo, `background-color` agora é `backgroundColor`. Simples assim.

A Forma com a qual passamos essa estilização para um elemento é bem simples. Nós faremos da seguinte forma `<tag style={nomeDoStyleSheet.Style}>conteúdo</tag>`

Abaixo podemos ver como ficaria um código desses.

- Exemplo

  ```JavaScript
  export default class Main extends Component {
    //...
    render() {
      return (
        <View style={styles.container}>
          <Text>Hello World</Text>
        </View>
      );
    }
  }

  const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#fafafa',
    },
  });
  ```

- Saída
  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React-Native/Imagens/Figura_02.png?raw=true)

# **5. EXEMPLO**

Antes de começarmos à trabalhar no exemplo, vamos definir o que será feito nesse exemplo.

Pegando os dados de uma Api, criada durante o material de nodeJS, que está [aqui](https://github.com/LucasFDutra/Minhas-apostilas/tree/master/NodeJS/node-api). Vamos mostrá-los na tela, sendo que iremos ter duas páginas, uma principal contendo uma lista de produtos, e outra com os dados detalhadas sobre um determinado produto, que será escolhido mediante um clique em um botão.

Abaixo você pode ver qual será o resultado final da aplicação

![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React-Native/Imagens/Figura_06.gif?raw=true)

# **6. API**

Agora vamos realmente começar nosso exemplo, e vamos fazer isso com uma chamada à Api.

Mas ao em vez de pegarmos a minha versão, vou utilizar a que está sendo disponibilizada pela rocketseat, por ser mais prático.

Para pegar a resposta de uma Api não tem absolutamente nada de diferente do que é no JavaScript normal. Então não vou ficar descrevendo passo a passo, apenas mostrarei os arquivos finais.

> OBS.: Para se informar melhor sobre essa api em específico, e como trabalhar com o insomnia, veja o material de nodeJS [aqui](https://github.com/LucasFDutra/Minhas-apostilas/tree/master/NodeJS#11-insomnia). Algumas outras informações úteis podem ser retiradas do material de react nessa parte [aqui](https://github.com/LucasFDutra/Minhas-apostilas/tree/master/React#92-api).

Agora vamos começar instalando a lib `axios` que vai fazer esse serviço de transitar as informações da api para nossa aplicação.

```sh
yarn add axios
```

Crie um arquivo chamado `api.js` que ficará dentro de `src/services` (services será criado por você).

- Árvore de diretórios de `src`

  ```sh
  ├── index.js
  ├── pages
  │   └── main.js
  ├── routes.js
  └── services
      └── api.js
  ```

- Arquivo `/src/services/api.js`

  ```JavaScript
  import axios from 'axios';

  const api = axios.create({
    baseURL: 'https://rocketseat-node.herokuapp.com/api',
  });

  export default api;
  ```

No arquivo `/src/pages/main.js` faça a importação da api e coloque para carregar os dados durante a montagem do componente, ou seja, no `componentDidMount`, mas também será criada uma função chamada `loadProducts`, que irá dentro do `componentDidMount`.

- Arquivo `/src/pages/main.js`

  ```JavaScript
  //...
  import api from '../services/api';

  export default class Main extends Component {
    //...

    componentDidMount() {
      this.loadProducts();
    }

    loadProducts = async () => {
      const response = await api.get('/products');

      const { docs } = response.data;
    };

    render() {
      return (
        <View>
          <Text>Hello World</Text>
        </View>
      );
    }
  }
  ```

Com isso, nós trouxemos os dados da api para dentro dessa variável `docs`. E agora na proxima seção vamos mostrar esses dados em tela.

# **7. EXIBINDO LISTA DE DADOS**

Para exibir os componentes de uma lista podemos utilizar o comando `map`, mas o melhor a ser feito é utilizar a tag `flatLIst`, que já esta preparada para esse tipo de trabalho, e mais para frente ela vai nos ajudar com Scroll ínfinito (mas por hora, apenas utilize ela).

E como temos que guardar as informações e atualizar a tela conforme elas são atualizada, vamos ter que utilizar o conceito de estados do react. Então volte no materia de react, e releia sobre [`state`](https://github.com/LucasFDutra/Minhas-apostilas/tree/master/React#81-state) ou sobre [`hooks`](https://github.com/LucasFDutra/Minhas-apostilas/tree/master/React#7-hooks)

- Arquivo `/src/pages/main.js`

  ```JavaScript
  import React, { Component } from 'react';
  import {
  View, Text, FlatList, TouchableOpacity
  } from 'react-native';
  import api from '../services/api';

  export default class Main extends Component {
    static navigationOptions = {
      title: 'JShunt',
    };

    state = {
      docs: [],
    };

    componentDidMount() {
      this.loadProducts();
    }

    loadProducts = async () => {
      const response = await api.get('/products');

      const { docs } = response.data;

      this.setState({ docs });
    };

    renderItem = ({ item }) => (
      <View>
        <Text>{item.title}</Text>
        <Text>{item.description}</Text>
        <TouchableOpacity onPress={() => {}}>
          <Text>Acessar</Text>
        </TouchableOpacity>
      </View>
    );

    render() {
      return (
        <View>
          <FlatList
            data={this.state.docs}
            keyExtrator={(item) => item._id}
            renderItem={this.renderItem}
          />
        </View>
      );
    }
  }
  ```

- Saída

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React-Native/Imagens/Figura_03.png?raw=true)

## 7.1 ESTILIZAÇÃO DA LISTA

Vamos agora estilizar a nossa lista, para isso vamos utilizar a seguinte estilização

- Arquivo `/src/pages/main.js`

  ```JavaScript
  import React, { Component } from 'react';
  import {
  View, Text, FlatList, TouchableOpacity, StyleSheet
  } from 'react-native';
  import api from '../services/api';

  export default class Main extends Component {
    static navigationOptions = {
      title: 'JShunt',
    };

    state = {
      docs: [],
    };

    componentDidMount() {
      this.loadProducts();
    }

    loadProducts = async () => {
      const response = await api.get('/products');

      const { docs } = response.data;

      this.setState({ docs });
    };

    renderItem = ({ item }) => (
      <View style={styles.productContainer}>
        <Text style={styles.productTitle}>{item.title}</Text>
        <Text style={styles.productDescription}>{item.description}</Text>
        <TouchableOpacity style={styles.productButton} onPress={() => {}}>
          <Text style={styles.productButtonText}>Acessar</Text>
        </TouchableOpacity>
      </View>
    );

    render() {
      return (
        <View style={styles.container}>
          <FlatList
            contentContainerStyle={styles.list}
            data={this.state.docs}
            keyExtrator={(item) => item._id}
            renderItem={this.renderItem}
          />
        </View>
      );
    }
  }

  const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#fafafa',
    },

    list: {
      padding: 20,
    },

    productContainer: {
      backgroundColor: '#fff',
      borderWidth: 1,
      borderColor: '#DDD',
      borderRadius: 5,
      padding: 20,
      marginBottom: 20,
    },

    productTitle: {
      fontSize: 18,
      fontWeight: 'bold',
      color: '#333',
    },

    productDescription: {
      fontSize: 16,
      color: '#999',
      marginTop: 5,
      lineHeight: 24,
    },

    productButton: {
      height: 42,
      borderRadius: 5,
      borderWidth: 2,
      borderColor: '#DA552F',
      backgroundColor: 'transparent',
      justifyContent: 'center',
      alignItems: 'center',
      marginTop: 10,
    },

    productButtonText: {
      fontSize: 16,
      color: '#DA552F',
      fontWeight: 'bold',
    },
  });
  ```

- Saída

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React-Native/Imagens/Figura_04.png?raw=true)

# **8. SCROLL ÍNFINITO**

Como você pode ver pelo app que está criando ai, quando chegamos ao final da página o programa simplesmente para, ele não carrega mais coisas (e eu sei que tem mais), então seria legal fazermos com que ele carregasse mais conteúdo assim que estivermos nos aproximando do final da página, do mesmo jeito que o Facebook, Instagram, YouTube e todos esses apps que possuem feed.

Para isso vamos armazenar as informações da página em uma variável de estado chamada `productInfo` e outra variável de estado com a página atual a ser exibida `page`.

Dentro do `loadProducts` vamos adicionar essas informações aos nossos estados.

E dentro de `FlatList` conseguimos avisar para o celular que ele pode carregar os novos arquivos quando chegarmos uma dada porcentagem de proximidade com o final da lista da página atula. Exemplo, se colocarmos 0.2 quer dizer que se estivermos em 80% da lista exibida, então deve-se carregar mais.

- Arquivo `/src/pages/main.js`

  ```JavaScript
  //...
  export default class Main extends Component {
    //...

    loadProducts = async (page = 1) => {
      const response = await api.get(`/products?page=${page}`);

      const { docs, ...productInfo } = response.data;

      this.setState({ docs, productInfo });
    };

    //...

    loadMore = () => {};

    render() {
      return (
        <View style={styles.container}>
          <FlatList
            contentContainerStyle={styles.list}
            data={this.state.docs}
            keyExtrator={(item) => item._id}
            renderItem={this.renderItem}
            onEndReached={this.loadMore}
            onEndReachedThreshold={0.1}
          />
        </View>
      );
    }
  }
  //...
  ```

Então veja que agora precisamos carregar uma função para carregar mais dados. O código completo fica (tem modificação na `loadProducts`).

- Arquivo `/src/pages/main.js`

  ```JavaScript
  import React, { Component } from 'react';
  import {
  View, Text, FlatList, TouchableOpacity, StyleSheet
  } from 'react-native';
  import api from '../services/api';

  export default class Main extends Component {
    static navigationOptions = {
      title: 'JShunt',
    };

    state = {
      productInfo: {},
      docs: [],
      page: 1,
    };

    componentDidMount() {
      this.loadProducts();
    }

    loadProducts = async (page = 1) => {
      const response = await api.get(`/products?page=${page}`);

      const { docs, ...productInfo } = response.data;

      this.setState({ docs: [...this.state.docs, ...docs], productInfo, page });
    };

    loadMore = () => {
      const { page, productInfo } = this.state;
      if (page === productInfo.pages) return;

      const pageNumber = page + 1;

      this.loadProducts(pageNumber);
    };

    renderItem = ({ item }) => (
      <View style={styles.productContainer}>
        <Text style={styles.productTitle}>{item.title}</Text>
        <Text style={styles.productDescription}>{item.description}</Text>
        <TouchableOpacity style={styles.productButton} onPress={() => {}}>
          <Text style={styles.productButtonText}>Acessar</Text>
        </TouchableOpacity>
      </View>
    );

    render() {
      return (
        <View style={styles.container}>
          <FlatList
            contentContainerStyle={styles.list}
            data={this.state.docs}
            keyExtrator={(item) => item._id}
            renderItem={this.renderItem}
            onEndReached={this.loadMore}
            onEndReachedThreshold={0.1}
          />
        </View>
      );
    }
  }

  const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#fafafa',
    },

    list: {
      padding: 20,
    },

    productContainer: {
      backgroundColor: '#fff',
      borderWidth: 1,
      borderColor: '#DDD',
      borderRadius: 5,
      padding: 20,
      marginBottom: 20,
    },

    productTitle: {
      fontSize: 18,
      fontWeight: 'bold',
      color: '#333',
    },

    productDescription: {
      fontSize: 16,
      color: '#999',
      marginTop: 5,
      lineHeight: 24,
    },

    productButton: {
      height: 42,
      borderRadius: 5,
      borderWidth: 2,
      borderColor: '#DA552F',
      backgroundColor: 'transparent',
      justifyContent: 'center',
      alignItems: 'center',
      marginTop: 10,
    },

    productButtonText: {
      fontSize: 16,
      color: '#DA552F',
      fontWeight: 'bold',
    },
  });
  ```

- Saída

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React-Native/Imagens/Figura_05.gif?raw=true)

# **9. NOVA PÁGINA**

Agora vamos exibir uma página com as informações do conteúdo que colocarmos no botão.

Para isso crie dentro da pasta `pages` o arquivo `product.js` (pode ser qualquer nome, mas eu vou usar esse). Adicione essa página às rotas.

- Árvore de diretórios de `src`

  ```sh
  ├── index.js
  ├── pages
  │   ├── main.js
  │   └── product.js
  ├── routes.js
  └── services
      └── api.js
  ```

A ideia aqui é criar uma outra página que seja na realidade uma webView.

Então para exibir essa webView vamos primeiro adicionar a lib correta.

```sh
yarn add react-native-webview
```

Agora que você deve rodar o comando `react-native run-android` novamente.

- Arquivo `/src/pages/products.js`

  ```JavaScript
  import React from 'react';
  import { WebView } from 'react-native-webview';

  const Product = ({ navigation }) => (
    <WebView source={{ uri: navigation.state.params.product.url }} />
  );

  Product.navigationOptions = ({ navigation }) => ({
    title: navigation.state.params.product.title,
  });

  export default Product;
  ```

- Arquivo `/src/routes.js`

  ```JavaScript
  import { createStackNavigator } from 'react-navigation';
  import Main from './pages/main';
  import Product from './pages/product';

  export default createStackNavigator(
    {
      Main,
      Product,
    },
    {
      navigationOptions: {
        headerStyle: {
          backgroundColor: '#DA552F',
        },
        headerTintColor: '#FFF',
      },
    },
  );
  ```

O bom do react-navigation é que ele já possui uma propriedade que nos permite transitar entre as páginas, chamada `navigate`. E como queremos que a transição entre páginas ocorra quando clicarmos em um botão, essa propriedade vai para dentro do botão `Acessar`, mais especificamente dentro de `onPress`, e receberá a página para qual deve ir e o item daquele produto, pois assim conseguiremos mostar o produto correspondente à aquele botão.

- Arquivo `/src/pages/main.js`

  ```JavaScript
  import React, { Component } from 'react';
  import {
  View, Text, FlatList, TouchableOpacity, StyleSheet
  } from 'react-native';
  import api from '../services/api';

  export default class Main extends Component {
    static navigationOptions = {
      title: 'JShunt',
    };

    state = {
      productInfo: {},
      docs: [],
      page: 1,
    };

    componentDidMount() {
      this.loadProducts();
    }

    loadProducts = async (page = 1) => {
      const response = await api.get(`/products?page=${page}`);

      const { docs, ...productInfo } = response.data;

      this.setState({ docs: [...this.state.docs, ...docs], productInfo, page });
    };

    loadMore = () => {
      const { page, productInfo } = this.state;
      if (page === productInfo.pages) return;

      const pageNumber = page + 1;

      this.loadProducts(pageNumber);
    };

    renderItem = ({ item }) => (
      <View style={styles.productContainer}>
        <Text style={styles.productTitle}>{item.title}</Text>
        <Text style={styles.productDescription}>{item.description}</Text>
        <TouchableOpacity
          style={styles.productButton}
          onPress={() => {
            this.props.navigation.navigate('Product', { product: item });
          }}
        >
          <Text style={styles.productButtonText}>Acessar</Text>
        </TouchableOpacity>
      </View>
    );

    render() {
      return (
        <View style={styles.container}>
          <FlatList
            contentContainerStyle={styles.list}
            data={this.state.docs}
            keyExtrator={(item) => item._id}
            renderItem={this.renderItem}
            onEndReached={this.loadMore}
            onEndReachedThreshold={0.1}
          />
        </View>
      );
    }
  }

  const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#fafafa',
    },

    list: {
      padding: 20,
    },

    productContainer: {
      backgroundColor: '#fff',
      borderWidth: 1,
      borderColor: '#DDD',
      borderRadius: 5,
      padding: 20,
      marginBottom: 20,
    },

    productTitle: {
      fontSize: 18,
      fontWeight: 'bold',
      color: '#333',
    },

    productDescription: {
      fontSize: 16,
      color: '#999',
      marginTop: 5,
      lineHeight: 24,
    },

    productButton: {
      height: 42,
      borderRadius: 5,
      borderWidth: 2,
      borderColor: '#DA552F',
      backgroundColor: 'transparent',
      justifyContent: 'center',
      alignItems: 'center',
      marginTop: 10,
    },

    productButtonText: {
      fontSize: 16,
      color: '#DA552F',
      fontWeight: 'bold',
    },
  });
  ```

- Saída:

  ![](https://github.com/LucasFDutra/Minhas-apostilas/blob/master/React-Native/Imagens/Figura_06.gif?raw=true)

# **10. RESUMINDO**

- Árvore de diretórios do programa

  ```sh
  ├── android
  ├── app.json
  ├── babel.config.js
  ├── index.js
  ├── ios
  ├── metro.config.js
  ├── node_modules
  ├── package.json
  ├── src
  │   ├── index.js
  │   ├── pages
  │   │   ├── main.js
  │   │   └── product.js
  │   ├── routes.js
  │   └── services
  │       └── api.js
  ├── __tests__
  │   └── App-test.js
  └── yarn.lock
  ```

- Arquivo `Index.js`

  ```JavaScript
  import { AppRegistry } from 'react-native';
  import App from './src';
  import { name as appName } from './app.json';

  AppRegistry.registerComponent(appName, () => App);
  ```

- Arquivo `/src/index.js`

  ```JavaScript
  import React from 'react';
  import Routes from './routes';

  const App = () => <Routes />;

  export default App;
  ```

- Arquivo `/src/routes.js`

  ```JavaScript
  import { createStackNavigator } from 'react-navigation';
  import Main from './pages/main';
  import Product from './pages/product';

  export default createStackNavigator(
    {
      Main,
      Product,
    },
    {
      navigationOptions: {
        headerStyle: {
          backgroundColor: '#DA552F',
        },
        headerTintColor: '#FFF',
      },
    },
  );
  ```

- Arquivo `/src/services/api.js`

  ```JavaScript
  import axios from 'axios';

  const api = axios.create({
    baseURL: 'https://rocketseat-node.herokuapp.com/api',
  });

  export default api;
  ```

- Arquivo `/src/pages/main.js`

  ```JavaScript
  import React, { Component } from 'react';
  import {
  View, Text, FlatList, TouchableOpacity, StyleSheet
  } from 'react-native';
  import api from '../services/api';

  export default class Main extends Component {
    static navigationOptions = {
      title: 'JShunt',
    };

    state = {
      productInfo: {},
      docs: [],
      page: 1,
    };

    componentDidMount() {
      this.loadProducts();
    }

    loadProducts = async (page = 1) => {
      const response = await api.get(`/products?page=${page}`);

      const { docs, ...productInfo } = response.data;

      this.setState({ docs: [...this.state.docs, ...docs], productInfo, page });
    };

    loadMore = () => {
      const { page, productInfo } = this.state;
      if (page === productInfo.pages) return;

      const pageNumber = page + 1;

      this.loadProducts(pageNumber);
    };

    renderItem = ({ item }) => (
      <View style={styles.productContainer}>
        <Text style={styles.productTitle}>{item.title}</Text>
        <Text style={styles.productDescription}>{item.description}</Text>
        <TouchableOpacity
          style={styles.productButton}
          onPress={() => {
            this.props.navigation.navigate('Product', { product: item });
          }}
        >
          <Text style={styles.productButtonText}>Acessar</Text>
        </TouchableOpacity>
      </View>
    );

    render() {
      return (
        <View style={styles.container}>
          <FlatList
            contentContainerStyle={styles.list}
            data={this.state.docs}
            keyExtrator={(item) => item._id}
            renderItem={this.renderItem}
            onEndReached={this.loadMore}
            onEndReachedThreshold={0.1}
          />
        </View>
      );
    }
  }

  const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#fafafa',
    },

    list: {
      padding: 20,
    },

    productContainer: {
      backgroundColor: '#fff',
      borderWidth: 1,
      borderColor: '#DDD',
      borderRadius: 5,
      padding: 20,
      marginBottom: 20,
    },

    productTitle: {
      fontSize: 18,
      fontWeight: 'bold',
      color: '#333',
    },

    productDescription: {
      fontSize: 16,
      color: '#999',
      marginTop: 5,
      lineHeight: 24,
    },

    productButton: {
      height: 42,
      borderRadius: 5,
      borderWidth: 2,
      borderColor: '#DA552F',
      backgroundColor: 'transparent',
      justifyContent: 'center',
      alignItems: 'center',
      marginTop: 10,
    },

    productButtonText: {
      fontSize: 16,
      color: '#DA552F',
      fontWeight: 'bold',
    },
  });
  ```

- Arquivo `/src/pages/products.js`

  ```JavaScript
  import React from 'react';
  import { WebView } from 'react-native-webview';

  const Product = ({ navigation }) => (
    <WebView source={{ uri: navigation.state.params.product.url }} />
  );

  Product.navigationOptions = ({ navigation }) => ({
    title: navigation.state.params.product.title,
  });

  export default Product;
  ```
