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

# Introdução

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

Já o que for diferente irei abordar aqui, seguindo um exemplo (O qual é exatamente igual ao exemplo criado no material de react).

## Iniciando um projeto

Para iniciar um projeto em react-native siga os passos que estão descritos nesse repositório [aqui](https://github.com/LucasFDutra/Ambiente-React-E-React-native-Com-ESlint-Airbnb). Nele você vai ver como se instala todas as ferramentas necessárias, como se configura o ambiente de desenvolvimento, como iniciar uma aplicação e como utilizar o seu celular como sendo o hardware em que seu programa estará rodando.

# Tags jsx

Como o react-native estará rodando em um dispositivo móvel e trabalhando com componentes nativos do sistema, é bem plausivel de pensar que ele não iria aceitar tags HTML normais. Mas para manter essa sintaxe (jsx) o react-native possui suas próprias tags (consulte a documentação para ver todas), sendo que duas das principais são as tags `View` e `Text`. A `View` seria o equivalente às `div`s do HTML e o `Text` representa todos os componentes de texto do programa, porém sem estilização própria, ou seja, onde antes teríamos `<p/>`, `<h1/>`, `<strong/>`, dentre outras, agora temos apenas o `Text`, que se quisermos podemos utilizá-lo.

Um detalhe importante, é que no react-native jamais poderemos colocar um texto fora da div `Text`. Por exemplo: Vamos dar um nome à um botão utilizando react, e depois react-native

- react

      	```JavaScript
      	<button>press</button>
      	```

- react-native

      	```JavaScript
      	<button>
      		<Text>press</Text>
      	</button>
      	```

# Rotas

Para facilitar a navegação entre páginas vamos ter sempre um arquivo de rotas, que será responsável pela transição entre as páginas e o como essa transição acontecerá.

A transição pode acontecer clicando um botão, arrastando para o lado, através de um menu lateral, enfim, temos diversas formas de fazer isso. Para ver como fazer cada uma delas, consulte a documentação nesse ponto [aqui](https://facebook.github.io/react-native/docs/navigation).

Vamos começar criando esse gerenciamento de rotas dividindo nosso programa em páginas e criando o arquivo de rotas. Para isso crie uma pasta `src` que é onde ficarão todos os nossos códigos. Dentro dela crie oaosrquivos `routes.js`, `index.js`, a pasta pages com o arquivo `main.js`. E também pague o arquivo `App.js`.

- Árvore de diretórios do programa

      	```sh
      	// arvore
      	```

Agora vamos mostrar as modificações necessárias em cada código já existente e o que colocar em cada um dos criados

- Arquivo `App.js`

      	```JavaScript
      	// código js
      	```

Aqui nós mandamos o código iniciar por `App` que está dentro de `src`. Agora vamos criar esse `App`.

- Arquivo `Index.js`

      	```JavaScript
      	// código js
      	```

- Arquivo `/src/index.js`

      	```JavaScript
      	// código js
      	```

- Arquivo `/src/pages/main.js`

      	```JavaScript
      	// código js
      	```

- Arquivo `/src/routes.js`

      	```JavaScript
      	// código js
      	```

Então nossa aplicação começa em `index.js`, que procura por um `App` dentro da pasta `src`, e esse `App` foi exportado de dentro de `/src/index.js`, que nos levou para as rotas em `/src/routes.js`, que agora controla a navegação entre as páginas, mas que por hora nos leva somente para a página `main` dentro de `/src/pages/main.js`.

Nesse momento nossa aplicação está apenas mostrando um `Hello world` na tela do celular.

- Saída

      	![]()

# Estilização

Agora que já estamos mostrando os dados na tela precisando mostrar eles de uma forma mais agradável visualmente falando.

No react e no JavaScript nós fazemos uso do CSS, mas aqui não temos isso, mas para manter a semelhança o react-native útiliza algo bem próximo, o `StyleSheets`. Que é uma função do react-native em que escrevemos as nossas esterilizações, utilizando uma sintaxe muito semelhante ao CSS.

Sendo que todos os atributos de estilo css que eram escritos da forma `palavra1-palavra2`, agora será escrito da forma `palavra1Palavra2`. Exemplo, `background-color` agora é `backgroundColor`. Simples assim.

A Forma com a qual passamos essa estilização para um elemento é bem simples. Nós faremos da seguinte forma `<tag style={nomeDoStyleSheet.Style}>conteúdo</tag>`

Abaixo podemos ver como ficaria um código desses.

- Exemplo

      	```JavaScript
      	// código js
      	```

- Saída

      	![]()

# Exemplo

Antes de começarmos à trabalhar no exemplo, vamos definir o que será feito nesse exemplo.

Pegando os dados de uma Api, criada durante o material de nodeJS, que está [aqui](https://github.com/LucasFDutra/Minhas-apostilas/tree/master/NodeJS/node-api). Vamos mostrá-los na tela, sendo que iremos ter duas páginas, uma principal contendo uma lista de produtos, e outra com os dados detalhadas sobre um determinado produto, que será escolhido mediante um clique em um botão.

Abaixo você pode ver qual será o resultado final da aplicação

    ![]()

# Api

Agora vamos realmente começar nosso exemplo, e vamos fazer isso com uma chamada à Api.

Mas ao em vez de pegarmos a minha versão, vou utilizar a que está sendo disponibilizada pela rocketseat, por ser mais prático.

Para pegar a resposta de uma Api não tem absolutamente nada de diferente do que é no JavaScript normal. Então não vou ficar descrevendo passo a passo, apenas mostrarei os arquivos finais.

> OBS.: Para se informar melhor sobre essa api em específico, e como trabalhar com o insomnia, veja o material de nodeJS [aqui](https://github.com/LucasFDutra/Minhas-apostilas/tree/master/NodeJS#11-insomnia). Algumas outras informações úteis podem ser retiradas do material de react nessa parte [aqui](https://github.com/LucasFDutra/Minhas-apostilas/tree/master/React#92-api).

- Arquivo `/src/services/api.js`

      	```JavaScript
      	// código
      	```

- Saída

      	![]()

# Exibindo lista de dados

Para exibir os componentes de uma lista podemos utilizar o comando `map`, mas o melhor a ser feito é utilizar a tag `flatLIst`, que já esta preparada para esse tipo de trabalho, e mais para frente ela vai nos ajudar com Scroll ínfinito (mas por hora, apenas utilize ela).

- Arquivo `/src/pages/main.js`

      	```JavaScript
      	// código js
      	```

- Saída

      	![]()

## Estilização da lista

Vamos agora estilizar a nossa lista, para isso vamos utilizar a seguinte estilização

```JavaScript
// código
```

Isso fará com que o arquivo fique da seguinte forma

- Arquivo `/src/pages/main.js`

      	```JavaScript
      	// código js
      	```

- Saída

      	![]()

# Scroll ínfinito

Como você pode ver pelo gif, quando chegamos ao final da página o programa simplesmente para, ele não carrega mais coisas (e eu sei que tem mais), então seria legal fazermos com que ele carregasse mais conteúdo assim que estivermos nos aproximando do final da página, do mesmo jeito que o Facebook, Instagram, YouTube e todos esses apps que possuem feed.

- Arquivo `/src/pages/main.js`

      	```JavaScript
      	// código js
      	```

- Saída

      	![]()

# Nova página

Agora vamos exibir uma página com as informações do conteúdo que colocarmos no botão.

Para isso crie dentro da pasta `pages` o arquivo `product.js` (pode ser qualquer nome, mas eu vou usar esse). Adicione essa página às rotas.

- Árvore de diretórios de `src`

      	```sh
      	// arvore
      	```

- Arquivo `/src/pages/products.js`

      	```JavaScript
      	// código js
      	```

- Arquivo `/src/routes.js`

      	```JavaScript
      	// código js
      	```

- Arquivo `/src/pages/main.js`

      	```JavaScript
      	// código js
      	```

## Estilização da nova página

A nova página contará com a seguinte estilização

- Arquivo `/src/pages/products.js`

      	```JavaScript
      	// código js
      	```

# Resumindo

- Árvore de diretórios do programa

      	```sh
      	// arvore
      	```

- Arquivo `Index.js`

      	```JavaScript
      	// código js
      	```

- Arquivo `/src/index.js`

      	```JavaScript
      	// código js
      	```

- Arquivo `/src/routes.js`

      	```JavaScript
      	// código js
      	```

- Arquivo `/src/services/api.js`

      	```JavaScript
      	// código js
      	```

- Arquivo `/src/pages/main.js`

      	```JavaScript
      	// código js
      	```

- Arquivo `/src/pages/products.js`

      	```JavaScript
      	// código js
      	```
