# Apostila de React

Autor: Lucas Felipe Dutra

**ANTES DE QUALQUER COISA, VEJA ESSE VIDEO [AQUI](https://www.youtube.com/watch?v=ln6t3uyTveQ&list=PLVc5bWuiFQ8GgKm5m0cZE6E02amJho94o&index=9)**

- Vamos a algumas recomendações:
  - Sempre irei colocar algumas recomendações, como vídeos, posts e afins no inicio de algumas partes. Então se tiver dúvidas ao ver o que escrevi recomendo que veja esses links.
  - Todos os exemplos serão escritos em pedaços picados, para diminuir e enfatizar as partes importantes aqui. Porém depois de citar tudo que preciso irei colocar o link para o código completo.

Veja como configurar o seu ambiente de desenvolvimento react [aqui](https://github.com/LucasFDutra/Ambiente-React-Com-ESlint-Airbnb)

# **1. INTRODUÇÃO**

- [Video recomendado](https://www.youtube.com/watch?v=cokAqzJMrZ8)

Tudo que será feito abaixo (até a seção 5) foi feito com a aplicação online chamada [codebox](https://codesandbox.io/), que permite a criação de códigos online, sem preciar instalar nada

O react é uma biblioteca do JavaScript, logo para poder aprender react tem que saber JavaScript.

E para importar a mesma precisamos inserir as seguintes linhas de código.

```JavaScript
import React from "react"
import ReactDOM from "react-dom"
```

# **2. ELEMENTO REACT**

Um elemento em react pode ser declarado de duas formas, a forma de JSX e a forma convencional do proprio react. Porém a forma convencional é muito ruim, se torma muito extensa e não é muito viável de ser utilizada.

O que esse tal de JSX? Bem o formato jsx é basicamente escrever o elemento em html (bem parecido com isso). Veja o exemplo abaixo:

```JavaScript
const elemento = <div><h2>Olá mundo</h2></div>
```

Assim quando utilizarmos o `elemento` no nosso código já sabemos que ele se refere à aquela linha html. Porém note que essa linha não foi declarada como uma string, e isso fica meio confuso para quem é um programador sem conhecimento nesses frameworks (que admito serem bem doidos), mas mesmo assim o react entende isso. Bom, isso acontece por conta que ele está preparado para trabalhar dessa forma, ou seja, o react entende esse formato jsx.

# **3. COMPONENTE**

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

Depois de criar o componente, precisamos mandar o react mostrar ele na tela, para isso faremos o seguinte comando:

```JavaScript
const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
```

- Saída:
  ![](https://github.com/LucasFDutra/Estudos/blob/master/Apostila%20de%20Web/Imagens%20React/Figura_001.png?raw=true)

Veja o código completo [aqui](https://github.com/LucasFDutra/Estudos/tree/master/Apostila%20de%20Web/React/ex001)

# **4. HOOKS**

- [Recomendado](https://reactjs.org/docs/hooks-intro.html)

Antes de inicar, saiba que hooks só podem ser utilizados em componentes funcionais, ou seja, componentes criados mediante a utilização de funções (sim, existe outro jeito de criar componentes, mediante classes ES6, mas não vem ao caso agora).

Vamos supor que queremos dar dinamismo à nossa aplicação, ou seja, passar parametros para o nosso componente e atualizá-lo conforme queremos.

Vejamos como poderiamos implementar a primeira parte dessa ideia, ou seja, como faremos para passar parâmetros.

Primeiramente isso é bem simples, afinal nosso componente é uma função JS. Sendo assim fica da seguinte forma:

```JavaScript
function App(props) {
  return (
    <div className="App">
      <h1>Hello CodeSandbox</h1>
      <h2>Start editing to see some magic happen!</h2>
      {elemento}
      <p>Meu nome é {props.name}</p>
    </div>
  );
}

const rootElement = document.getElementById("root");
ReactDOM.render(<App name="Lucas" />, rootElement);
```

Veja que o que fizemos foi colocar um parâmetro `props` na nossa function e passar ele lá em baixo no ReactDOM logo apos a chamada do componente App, passando a string "Lucas" como sendo uma variável name.

```JavaScript
function App(props)

<p>Meu nome é {props.name}</p>

ReactDOM.render(<App name="Lucas" />, rootElement);
```

Veja que props não recebe `Lucas`, mas sim um objeto. Por isso precisamos colocar `props.name` quando queremos mostrar o conteúdo de name.

Agora vamos para a segunda parte, a parte interativa. Digamos que quero criar um botão que aumente um dado valor ao ser apertado e o atualiza na tela a cada incremento. Tal ideia deve ficar como mostrado abaixo:

![](https://github.com/LucasFDutra/Estudos/blob/master/Apostila%20de%20Web/Imagens%20React/Figura_002.gif?raw=true)

Para isso podemos pensar em fazer o seguinte:

```JavaScript
function click(i) {
  return (i += 1);
}

function App() {
  var i = 0;
  return (
    <div className="App">
      <h1>O valor de i é: {i}</h1>
      <button onClick={click(i)}>Incrementar</button>
    </div>
  );
}
```

Sendo que quando temos `onClick={click(i)}` estamos dizendo que quando clicarmos no botão ele irá chamar a função click e passar o valor de i para ela.

Mas, isso não funciona.

O porque não funciona? Bem, é simples. Quando criamos o componente ele não fica sendo chamado repetidas vezes, então quando clicamos no botão não existe função sendo chamada, pois simplesmete reenderizamos o componente na tela e depois ele não é reenderizado novamente.

E veja que a variável i não é salva na memoria em momento algum, pois ela está dentro de um função, e assim que retornamos o seu valor ele é apagado. E isso é um problema, pois queremos que ele continue atualizando, mas como atualizar se ele sempre está valendo a mesma coisa?

Então veja que mesmo que fizermos a função (componente) ser rodada varias e várias vezes o valor de i sempre será o mesmo.

Mas como resolvemos isso? Utilizando hooks. Hooks são ancoras para os nossos valores, ancoras que fazem com que eles tenham seus valores salvos como se fossem variáveis globais.

E o código?

Primeiro precisamos pegar algumas coisas específicas na biblioteca do react. Que nesse caso são.

```JavaScript
import React, {useState} from "react";
import ReactDOM from "react-dom";
```

Agora vamos criar a nossa variável `i` de acordo com os padrões do hook.

```JavaScript
function App() {
  const [i, setI] = useState(0)
  return (
```

O useState é um hook, que guadará o estado da nossa variáve. nesse caso ficaremos com a seguinte construção:

```JavaScript
const [variável, função_de_controle_da_variável] = useState(valor_inicial_da_variável)
```

Ou seja, a nossa variável i, é controlada pela função setI e de inicio vale 0. Uma observação valida aqui, é que não é obrigatório preencher o campo de valor inicial da variável.

> **OBS.: Os hooks que forem adicionados devem sempre serem adicionados no inicio do componente.**

Proximo passo é que a nossa função de modificação deve estar dentro do componente. E assim termos o código abaixo:

```JavaScript
// componente
function App() {
  const [i, setI] = useState(0);

  function click() {
    setI(i + 1);
  }

  return (
    <div className="App">
      <h1>O valor de i é: {i}</h1>
      <button onClick={click}>Incrementar</button>
    </div>
  );
}
```

> OBS.: a função click poderia ter sido feito utilizando arrow function, seria melhor (veja mais sobre isso na apostila de JavaScript), mas por hora irei utilizar a function normal.

Veja o código completo [aqui](https://github.com/LucasFDutra/Estudos/tree/master/Apostila%20de%20Web/React/ex002)

## 4.1 EXEMPLO

O exemplo será composto por um jogo, em que o computador tentará adivinhar um número. Para que ele consiga adivinhar o número iremos colocar 3 botões na tela e falaremos para ele se o valor é maior ou menos ou se acertou.

Veja abaixo o gif mostrando o jogo, e se quiser pode ver o código completo [aqui](https://github.com/LucasFDutra/Estudos/tree/master/Apostila%20de%20Web/React/ex003)

![](https://github.com/LucasFDutra/Estudos/blob/master/Apostila%20de%20Web/Imagens%20React/Figura_003.gif?raw=true)

# **5. PROXIMOS PASSOS**

Veja projetos mais recentes utilizando hooks e tente reproduzir o que está sendo feito. Eu mesmo tenho um [aqui](https://github.com/LucasFDutra/Minhas-Series) que foi desenvolvido com base no projeto que está [aqui](https://github.com/LucasFDutra/Estudos/tree/master/Apostila%20de%20Web/React/ex004/minhas-series) que foi desenvolvido juntamento com o canal devPleno durante o Hands-on de 2019. Porém, de preferência para projetos que alguém vai ensinando junto (youtube). Mas já deixo a dica de que pelo menos a parte visual é bom ir olhando o [bootstrap](https://getbootstrap.com/) e no [reactstrap](https://reactstrap.github.io/), pois é mais tranquilo utilizar eles para fazer as interfaces.
