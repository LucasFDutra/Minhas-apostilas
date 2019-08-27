# Apostila de JavaScript

Autor: Lucas Felipe Dutra

**ANTES DE QUALQUER COISA, VEJA ESSE VIDEO [AQUI](https://www.youtube.com/watch?v=9w3o9NHXqu0&list=PLMdYygf53DP5Sc6yFYs6ZmjsuuA2fu0TK) PARA APRENDER MAIS SOBRE CLEAN CODE**

# DICAS

Segue abaixo alguns links que posso indicar para auxiliarem em seus estudos. Mas já adianto que o que mais recomendo é o curso gratuito da Rocketseat (primeiro link).

- [Rocketseat](https://skylab.rocketseat.com.br/)
- [Mozilla](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [W3schools](https://www.w3schools.com/js/default.asp)
- [Curso em Video](https://www.youtube.com/playlist?list=PLHz_AreHm4dlsK3Nr9GVvXCbpQyHQl1o1)
- [DevMedia](https://www.devmedia.com.br/primeiros-passos-no-html5-javascript-e-css3/25647)
- [DevMedia](https://www.devmedia.com.br/javascript-tutorial/37257)

Em mihas anotações referentes ao curso em video tem no material uma parte de manipulação de dom, e outra de poo (não aborda no curso em video, mas eu estudei por fora). Porém, não escolhi não trazer esses temas para cá, isso se deve ao fato de que POO não é muito utilizada em JavaScript (não diretamente) e a manipulação de dom eu acho mais interessante utilizar algum framework ou então o react. Recomendo muito o react.

- [Minhas notas do curso em video](https://github.com/LucasFDutra/Minhas-apostilas/tree/master/JavaScript/Curso%20em%20Video);
- [Meu material sobre react]().

Então quando acabar esse material, você pode seguir seus estudos em duas direções, ou o frontend (recomendo o react na web e react-native no mobile) ou então o backend (recomendo o nodeJS).

# Instalação

Para trabalhar com o JavaScript no seu computador instale o nodejs primeiramente.

## Windows

Vá no [site](https://nodejs.org/en/) do node e baixe o instalador e saia dando next

## Linux (ubuntu e derivados)

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

## Linux (Todos os sistemas)

Veja maiores informações sobre o node para linux [aqui](https://github.com/nodesource/distributions/blob/master/README.md). Você encontra como instalar o node no seu pc (esse link veio a partir do site oficial do node na aba downloads)

## Configurando [VScode](https://code.visualstudio.com/)

Recomendo utilizar o Visual studio code para programar, porém sinta-se a vontade para utilizar o que preferir, mas caso escolha trabalhar com o vscode, então baixe as extensões

- `ESLint` para deixar o código mais bonito e corrigir erros
- `Node Exec` para executar os códigos js precionando F8.

Caso queira dar uma olhada nesse link [aqui](https://blog.rocketseat.com.br/ambiente-desenvolvimento-javascript/). É do pessoal da rocketseat mostrando algumas configurações que eles sugerem para fazer no vscode para programar em JS.

Lembrando que assim iremos executar os códigos js na forma de node e não de frontend (browser).

## Como criar um código JS

Você pode utilizar ele no meio do código html, como será indicado no tópico 1, ou então crie um novo arquivo no seu pc com a extensão `.js` e pronto, começe a programar nesse arquivo e mande ele rodar com o node, pode fazer isso via terminal ou caso tenha instalado a extensão `Node Exec` no vscode é só prescionar F8.

# SUMÁRIO

- [**1. ESTRUTURANDO**](#1-estruturando)
- [**2. VARIÁVEIS**](#2-variáveis)
  - [2.1 CONVERSÃO DE VARIÁVEIS](#21-conversão-de-variáveis)
  - [2.2 FORMATANDO STRINGS](#22-formatando-strings)
  - [2.3 FORMATANDO NÚMEROS](#23-formatando-números)
- [**3. CONDICIONAIS**](#3-condicionais)
  - [3.1 OPERADORES](#31-operadores)
  - [3.2 IF](#32-if)
  - [3.2 SWITCH](#32-switch)
  - [3.3 OPERADORES TERNÁRIOS](#33-operadores-ternários)
- [**4. ESTRUTURAS DE REPETIÇÕES**](#4-estruturas-de-repetições)
  - [4.1 FOR](#41-for)
  - [4.2 WHILE](#42-while)
  - [4.3 DO WHILE](#43-do-while)
  - [4.4 BREAK](#44-break)
- [**5. MÉTODOS/FUNÇÕES**](#5-métodosfunções)
- [**6. INTERVALO E TIMEOUT**](#6-intervalo-e-timeout)
- [**7. Arrays**](#7-arrays)
  - [7.1 DECLARAÇÃO](#71-declaração)
  - [7.2 INSERINDO NOVOS TERMOS](#72-inserindo-novos-termos)
  - [7.3 ACESSAR UM TERMO](#73-acessar-um-termo)
  - [7.4 MUDANDO UM TERMO](#74-mudando-um-termo)
  - [7.5 REMOVE E RETORNAR O ULTIMO TERMO](#75-remove-e-retornar-o-ultimo-termo)
  - [7.6 REMOVE E RETORNA O PRIMEIRO TERMO](#76-remove-e-retorna-o-primeiro-termo)
  - [7.7 ADICIONA ELEMENTO AO INICIO](#77-adiciona-elemento-ao-inicio)
  - [7.8 DELETANDO ELEMENTO](#78-deletando-elemento)
  - [7.9 INSERIR ELEMENTOS](#79-inserir-elementos)
  - [7.10 CONCATENANDO ARRAYS](#710-concatenando-arrays)
  - [7.11 ORDENANDO ARRAY](#711-ordenando-array)
  - [7.12 INVERTENDO ARRAY](#712-invertendo-array)
  - [7.13 MAIOR TERMO DO ARRAY](#713-maior-termo-do-array)
  - [7.14 MENOR TERMO DO ARRAY](#714-menor-termo-do-array)
  - [7.15 LIMPANDO ARRAY](#715-limpando-array)
  - [7.16 OBTER ÍNDICE DE UM ELEMENTO](#716-obter-índice-de-um-elemento)
  - [7.17 COPIANDO UM ARRAY](#717-copiando-um-array)
  - [7.18 RETORNAR O TAMANHO DE UM ARRAY](#718-retornar-o-tamanho-de-um-array)
  - [7.19 ARRAY COM FOR](#719-array-com-for)
  - [7.20 FOREACH](#720-foreach)
- [**8. JSON**](#8-json)
- [**9. JAVASCRIPT ASSINCRONO**](#9-javascript-assincrono)
  - [9.1 AJAX](#91-ajax)
  - [9.2 PROMISES](#92-promises)
  - [9.3 ASYNC/AWAIT](#93-asyncawait)
  - [9.4 AXIOS](#94-axios)
    - [**9.4.1 Axios com promises**](#941-axios-com-promises)
    - [**9.4.2 Axios com async/await**](#942-axios-com-asyncawait)

# **1. ESTRUTURANDO**

É possível colocar o código js em meio ao arquivo HTML. Basta adicioná-lo entre a tag `<script>`. Como mostrado abaixo.

- Exemplo:

  ```HTML
  <!DOCTYPE html>
  <html lang="pt-br">
  <head>
  </head>
  <body>
      <script>
          <!-- Código JS -->
      </script>
  </body>
  </html>
  ```

Porém, em um primeiro momento vamos rodar os nossos códigos JS utilizando o node, ou seja, vamos rodar ele fora do navegador, utilizando a nossa máquina.

Porém tudos os códigos que eu fizer aqui você pode apenas colocá-los entre a tag `script` de uma arquivo html e abrir o mesmo no seu browser, e abrir a janela de inspeção (no google chrome aperte F12) e se dirigir ao console da mesma.

Uma outra opção é colocar o arquivo js separado do arquivo html. Bastando indicar qual o arquivo js será utilizado pelo arquivo html em questão. E então abra o arquivo html no seu browser e vá para o console da pagina. Para fazer isso crie um arquivo html com a seguinte estrutura:

```HTML
<!DOCTYPE html>
<html lang="pt-br">
<head>
</head>
<body>
    <script src="arquivo.js"></script>
</body>
</html>
```

Claro que estou supondo que você deixará o arquivo.js e o arquivo .html na mesma pasta, caso contrário você terá que indicar o endereço e o nome do arquivo dentro da tag `script`.

# **2. VARIÁVEIS**

O JS não possui variáveis estáticas, ou seja, elas não possuem tipos fixos (int, float, string). Uma variável é apenas uma variável que pode assumir um tipo conforme necessário. Ou seja, elas possuem tipo dinâmico (você entenderá isso melhor no exemplo).

Podemos criar variáveis de três maneiras.

```JavaScript
nome_da_variavel = valor;
var nome_da_variavel = valor;
let nome_da_variavel = valor;
const nome_da_variavel = valor;
```

A diferença entre esses quatro tipos de declaração pode ser encontrada [aqui](https://www.alura.com.br/artigos/entenda-diferenca-entre-var-let-e-const-no-javascript), mas também irei explicá-las de forma mais resumida, e mais abaixo terá um exemplo:

- sem nada antes: A variável é vista como sendo global. Ou seja, todo o código à vê.
- `var`: A variável existe apenas dentro do seu escopo local. Ou seja, se tivermos uma função e essa variável for declarada dentro dela toda a função verá a variável.
- `let`: A variável é de escopo de bloco. Ou seja, se ela for declarada dentro de um `for` que está dentro de uma função, somente o `for` verá essa variável, não a função toda.
- `const`: Diferentemente do `let` e `var`, aqui a variável obrigatoriamente precisa ser inicializada, e não pode ter seu valor alterado, afinal é uma constante.

Agora vamos ver dois exemplos, o primeiro é um que utilizaremos a variável x para receber uma string, um inteiro, um float e um boolean, mostrando que o tipo dela pode ser trocado de acordo com o que precisamos. E o segundo é um que utilizaremos os conceitos de `var`, `let` e `const`

> OBS.: O comando `console.log` mostrará no console o valor que for passado à ele, em resumo ele é igual ao comando `print` de outras linguagens como o python.

- Exemplo:

  ```JavaScript
  // declarando a variável
  var x;
  //string
  x = 'nome';
  console.log(x);
  //numeros
  x = 1;
  console.log(x);
  //float
  x = 3.14;
  console.log(x);
  //boolean
  x = true;
  console.log(x);
  x = false;
  console.log(x);
  ```

- Saída:
  ```JavaScript
  nome
  1
  3.14
  true
  false
  ```

Antes do exemplo queria te dizer que caso não saiba o que é uma função e nem um `for`, não se preocupe, pense da que ambos formam uma caixa, e nesse caso o função é uma caixa grade, e o `for` é uma menor que está dentro dessa caixa grande.

- Exemplo `var`:

  ```JavaScript
  function testeVar() {
    console.log(i);
    for (var i = 0; i < 3; i++) {
      console.log(i);
    }
    console.log(i);
  }

  testeVar();
  ```

- Saída:

  ```JavaScript
  undefined // antes do loop
  0
  1
  2
  3 // depois do loop
  ```

Veja que a variável aceitou normalmente o `undefined`, e foi reconhecida mesmo antes de ter sido declarada no `for`, isso porque ela é do tipo `var` e todo o escopo à verá.

Colocando para quem não entende funções e loops, vamos voltar as caixas: O que aconteceu aqui é que se a variável for um `var`, a caixa externa consegue ver dentro da caixa interna e por conseguencia vizualizar o valor da variável.

- Exemplo `let`:

  ```JavaScript
  function testeLet() {
    console.log(i);
    for (let i = 0; i < 3; i++) {
      console.log(i);
    }
    console.log(i);
  }

  testeLet();
  ```

Desta forma o resultado é um **erro**, isso porque o `let` não é visivel para fora do bloco, no caso o for. Sendo assim o primeiro e terceiro `console.log` que temos nessa função não são possíveis de serem executados.

Assim, essa função precisa ser reescrita da seguinte forma:

- Exemplo `let`:

  ```JavaScript
  function testeLet() {
    for (let i = 0; i < 3; i++) {
      console.log(i);
    }
  }

  testeLet();
  ```

- Saída:

  ```JavaScript
  0
  1
  2
  ```

Agora vamos para o exemplo utilizando o `const`:

- Exemplo `const`:

  ```JavaScript
  function testeConst() {
    console.log(x);
    for (let i = 0; i < 2; i++) {
      const x = 3;
    }
    console.log(x);
  }

  testeConst();
  ```

Veja que nesse caso eu declaro a constante `x` dentro do for, mas não a utilizo como contador, isso é porque ela é uma constante, logo não serve para contar, afinal não muda de valor. Porém o objetivo nesse momento é ver que o `const` também é visto apenas pelo bloco, afinal o que retorna dessa função é um **erro**.

O modo de fazer isso funcionar seria o seguinte:

- Exemplo `const`:

  ```JavaScript
  function testeConst() {
    for (let i = 0; i < 2; i++) {
      const x = 3;
      console.log(x);
    }
  }

  testeConst();
  ```

- Saída:

  ```JavaScript
  3
  3
  ```

> OBS.: O JS não exige que coloquemos `;` no final de cada comando, mas acho que todo mundo acostumou com isso, e em certos lugares ele acaba sendo necessário, então é sempre bom colocar para não perder o costume.

## 2.1 CONVERSÃO DE VARIÁVEIS

Sempre acabamos caindo no caso de que recebemos uma variável em um tipo, mas queremos trabalhar com ela em outro. Um exemplo disso é quando recebemos algo de um input html que vem em formato string, mas precisamos fazer uma soma com ele. Logo precisamos pegar esse valor e passar para float ou int.

- String -> Outros

  ```JavaScript
  variavel = Number.parseTIPO(variavel)
  //Exemplos
  variavel = Number.parseInt(variavel)
  variavel = Number.parseFloat(variavel)
  ```

- Outros -> String
  ```JavaScript
  variavel = variavel.toString()
  variavel = String(variavel)
  ```

## 2.2 FORMATANDO STRINGS

```JavaScript
var s = 'JavaScript'
s.length // tamanho da string
s.toUpperCase() // todo para maiúscula
s.toLowerCase() // tudo para minúscula
```

## 2.3 FORMATANDO NÚMEROS

```JavaScript
var numero = 3.14
numero.toFixed(2) // define duas casas decimais para numero
numero.toFixed(2).replace('.',',') // substitui o ponto por virgula: 3.14 -> 3,14

// mostra o numero com o cifrão da moeda respectiva
numero.toLocaleString('pt-br', {style: 'currency', currency: 'BRL'}) // R$ 3,14
numero.toLocaleString('pt-br', {style: 'currency', currency: 'USD'}) // US$ 3,14
```

# **3. CONDICIONAIS**

Condicionais basicamente irão controlar o fluxo do nosso programa, impondo condições para que o nosso código tome determinadas atitudes. Exemplo:

Se `a` for maior do que `b` então faça `x`, se não faça `y`.

## 3.1 OPERADORES

Agora teremos 3 modos de fazer condicionais, mas em todos eles vamos utilizar os nossos operadores.

- **&&:** Condição 'a' e condição 'b' devem ser atendidas.

- **||:** Condição 'a' ou condição 'b' devem ser atendidas.

- **maior:** >

- **maior ou igual:** >=

- **menor:** <

- **menor ou igual:** <=

- **diferente:** !=

- **igual:** ==

- **identicos:** ===

- **não identicos:** !==

- **Verdadeiro:** true

- **Falso:** false

É importante comentar que temos aqui os operadores `==`, `===`, `!=` e `!==`. Que possuem diferenças entre eles.

- Os operadores `==` e `!=` olham apenas o valor a ser comparado sem olhar o tipo.
- Os operadores `===` e `!==` olham o valor e o tipo.

- Exemplo:

  ```JavaScript
  5 == '5'; // true
  5 === '5'; // false
  5 === 5;  // true

  5 != '5' // false
  5 !== '5' // true
  5 !== 5 // false
  ```

## 3.2 IF

A condicional `if` pode ser dividida em 3 estágios:

- `if`: em que verificamos uma dada condição e caso ela seja atendida fazemos algo
- `else if`: em que caso o `if` antecessor não atenda aos requisitos impostos, iremos verificar novas condições
- `else`: em que caso o `if` antecessor e eventuais `else if` anteriores também não atendam seus requisitos então entraremos nesse bloco.

Veja como podemos trabalhar com cada um desses estágios do `if`

- if
  ```JavaScript
  if (condição){
    // Código...
  }
  ```
- else if
  ```JavaScript
  else if (condição){
    // Código...
  }
  ```
- else
  ```JavaScript
  else{
    // Código...
  }
  ```

Veja o exemplo a seguir:

- Exemplo:

  ```JavaScript
  var a = 1;
  var b = 1;

  if (a == b) {
    console.log("'a' é igual à 'b'"); // console.log seria o printf do JS
  } else if (a > b) {
    console.log("'a' é maior do que 'b'");
  } else {
    console.log("'a' é diferente de 'b'");
  }
  ```

- Saída:
  ```JavaScript
  'a' é igual à 'b'
  ```

É importante frizar que a condicional `else if` somente é verificada caso a condicinal do `if` seja falsa, isso evita gasto de processamento. Ou seja, um `else if` seguido de um `if` tem diferença perante dois `if` seguidos.

Se colocarmos por exemplo:

- Exemplo:

  ```JavaScript
  var a = 1;
  var b = 1;

  if (a == b) {
    console.log("'a' é igual à 'b'"); // console.log seria o printf do JS
  }
  if (a > b) {
    console.log("'a' é maior do que 'b'");
  } else {
    console.log("'a' é diferente de 'b'");
  }
  ```

A saída será a mesma, porém no primeiro caso o teste (a > b) não foi rodado, pois o `if` antecessor já retornou `true`. Porém nesse segundo exemplo o teste é sim rodado, pois estamos usando outro `if`.

## 3.2 SWITCH

O switch serve para quando acabamos verificando valores pontuais de uma variável, por exemplo:

- Se a = 1: faça..
- Se a = 2: faça..
- Se a = n: faça..

fazer isso com o uso do `if` não é muito produtivo (porém possível). Para esses casos podemos utilizar o switch que possui a seguinte sintax:

```JavaScript
switch (variavel) {
  case valor_possivel_1:
    //código
    break;
  case valor_possivel_2:
    //código
    break;
  case valor_possivel_3:
    //código
    break;
}
```

A leitura desse código fica mais ou menos da seguinte forma: caso a `variavel` seja igual ao `valor_possivel_1` então execute algo e saia do `switch`, mas se não for então veja se ela é igual ao `valor_possivel_2` e caso seja, execute algo e saia do `switch`. E assim por diante.

Veja o exemplo abaixo:

- Exemplo:

  ```JavaScript
  var a = 3;

  switch (a) {
    case 1:
      console.log("a = 3");
      break;
    case 2:
      console.log("a = 2");
      break;
    case 3:
      console.log("a = 3");
      break;
  }
  ```

- Saída:
  ```JavaScript
  a = 3
  ```

## 3.3 OPERADORES TERNÁRIOS

O operador ternário é um jeito mais rápido de fazer uma condicional, a declaração do mesmo é a seguinte:

```JavaScript
condição ? expressão_1 : expressão_2
```

Sendo que a `expressão_1` é executada caso a condição seja verdadeira, e a `expressão_2` é executada caso seja falsa.

A grosso modo, podemos ler esse comando da seguinte forma: "a nossa condição é verdadeira?.. Se sim então execute a expressão_1, se não execute a expressão_2".

Veja o exemplo:

- Exemplo

  ```JavaScript
  a = 3;

  a > 2
    ? console.log("a é maior que dois")
    : console.log("a não é maior do que dois");
  ```

- Saída:
  ```JavaScript
  a é maior que dois
  ```

# **4. ESTRUTURAS DE REPETIÇÕES**

Quando precisamos interar nosso código diversas vezes, então escolhemos as nossas estrutuas de repetição. São elas:

- For: Para operações com inicio e fim bem definidos;
- While: Para operações com o final incerto;
- do While: Uma alternativa ao While, mas que garante ao menos uma execução.

## 4.1 FOR

A sintax do for é dada da seguinte forma:

```JavaScript
for(inicialização; condição; incremento){
    // Código...
}
```

- Exemplo:
  ```JavaScript
  for (i = 0; i < 10; i++) {
    console.log(i);
  }
  console.log(`o valor de i após o for: ${i}`);
  ```
- Saída:
  ```JavaScript
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9
  o valor de i após o for: 10
  ```

## 4.2 WHILE

```JavaScript
while(condição){
  // Código...
}
```

- Exemplo:

  ```JavaScript
  i = 0;
  while (i < 10) {
    console.log(i);
    i++;
  }
  console.log(`o valor de i após o while: ${i}`);
  ```

- Saída:
  ```JavaScript
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
  O valor de i após o while: 10
  ```

## 4.3 DO WHILE

A diferença entre o `do while` e `while` é que no `do while` o código é executado primeiro e depois que a condição é verificada.

```JavaScript
do{
  // Código...
}while(condição)
```

- Exemplo:

  ```JavaScript
  i = 0;
  do {
    console.log(i);
    i++;
  } while (i < 10);
  console.log(`o valor de i após o while: ${i}`);
  ```

- Saída:
  ```JavaScript
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
  O valor de i após o do While: 10
  ```

## 4.4 BREAK

O comando `break` serve para interromper um loop caso alguma condição especial ocorra.

- Exemplo:

  ```JavaScript
  for (i = 0; i < 10; i++) {
    console.log(i);
    if (i == 5) {
      break;
    }
  }
  ```

- Saída:
  ```JavaScript
  0, 1, 2, 3, 4, 5,
  ```

# **5. MÉTODOS/FUNÇÕES**

- **Recomendados**
  - [Link 1](https://www.youtube.com/watch?v=zNimSYkrs6w): Funções em JavaScript `(Video)`
  - [Link 2](https://www.youtube.com/watch?v=AgOwGKB8D2M): Arrow Functions `(Video)`

---

Uma função nada mais é do que um bloco de código que escrevemos separadamente e o chamamos quando precisamos, evitando duplicações de código e maior modularização do código.

Vamos ver agora quatro modos de declara funções:

- Convencional
  ```JavaScript
  function nome_da_função(parâmetros){
    // Código...
  }
  ```
- Função anônima
  ```JavaScript
  const variavel = function(parametros){
    // código
  }
  ```
- Arrow function
  ```JavaScript
  const nome_da_função = (parametros)=>{
    // Código
  }
  ```
- IIFE: Immediately Invoked Function Expression
  ```JavaScript
  (function(parametro){/*código*/})(passar_parametro)
  ```

Vejamos um pouco mais sobre cada uma dessas formas

- Convencional

  - Aqui teremos a declaração normal de uma função para todas as linguagens mais tradicionais.

- Funcões anônimas

  - No JS podemos escrever funções anônimas que seriam funções atribuidas a variáveis.

- Arrow functions

  - Arrow functions são um jeito diferente e mais fácil de fazer funções anônimas. Temos dois métodos de fazer isso,
    - Primeiro é quando temos um corpo para a função, ou seja, ela possui códigos dentro dela.
    - Segundo é quando a função tem apenas o return, sendo assim podemos declará-la de forma mais direta.

- IIFE

  - Uma função que será invocada assim que criada.

- Exemplo:

  ```JavaScript
  function soma_convencional(a, b) {
    var s = a + b;
    return s;
  }

  const soma_anônima = function(a, b) {
    var s = a + b;
    return s;
  };

  const soma_arrow = (a, b) => {
    var s = a + b;
    return s;
  };

  const soma_arrow_direta = (a, b) => a + b;

  (function(a, b) {
    console.log(a + b);
  })(1, 2);

  console.log(soma_convencional(1, 2));
  console.log(soma_anônima(1, 2));
  console.log(soma_arrow(1, 2));
  console.log(soma_arrow_direta(1, 2));
  ```

- Saída:
  ```JavaScript
  3
  3
  3
  3
  3
  ```

# **6. INTERVALO E TIMEOUT**

- `setTimeout`: Executa a ação apenas uma vez, mas demora um dado tempo até executá-la.
- `setInterval`: Executa uma dada função seguidamente, mas em intervalos de tempo. Exemplo:

- Exemplo:

  ```JavaScript
  function escreverTimeout() {
    console.log("dentro do setTimeout");
  }

  setTimeout(escreverTimeout, 1000);

  function escreverInterval() {
    console.log("dentro do setInterval");
  }

  setInterval(escreverInterval, 1000);

  ```

- Saída:

```JavaScript
// depois de 1 seg
dentro do setTimeout
// depois de 1 seg
dentro do setInterval
// depois de 1 seg
dentro do setInterval
// depois de 1 seg
dentro do setInterval
// continua indefinidamente
```

# **7. Arrays**

## 7.1 DECLARAÇÃO

```JavaScript
nome = []
nome = [valores]
```

- Exemplo:

  ```JavaScript
  array_1 = []
  array_2 = [1,2,3]

  console.log(array_1)
  console.log(array_2)
  ```

- Saída:
  ```JavaScript
  []
  [ 1, 2, 3 ]
  ```

## 7.2 INSERINDO NOVOS TERMOS

```JavaScript
array[posição] = valor // insere onde quiser
// ou
array.push(valor) // insere no final
```

- Exemplo 1:

  ```JavaScript
  array = []

  for (i=0; i<3; i++){
      array[i] = i
  }

  console.log(array)
  ```

- Saída 1:

  ```JavaScript
  [ 0, 1, 2 ]
  ```

- Exemplo 2:

  ```JavaScript
  array = []

  for (i=0; i<3; i++){
      array.push(i)
  }

  console.log(array)
  ```

- Saída 2:
  ```JavaScript
  [ 0, 1, 2 ]
  ```

## 7.3 ACESSAR UM TERMO

```JavaScript
array[posição]
```

- Exemplo:

  ```JavaScript
  array = [45, 15, 'teste', 7.34]
  console.log(array[3])
  ```

- Saída:
  ```JavaScript
  7.34
  ```

## 7.4 MUDANDO UM TERMO

```JavaScript
array[posição] = valor
```

- Exemplo:

  ```JavaScript
  array = [45, 15, 'teste', 7.34]
  array[3] = 4
  console.log(array)
  ```

- Saída:
  ```JavaScript
  [ 45, 15, 'teste', 4 ]
  ```

## 7.5 REMOVE E RETORNAR O ULTIMO TERMO

```JavaScript
array.pop()
```

- Exemplo:

  ```JavaScript
  array = [45, 15, 'teste', 7.34]
  x = array.pop()
  console.log(array)
  console.log(x)
  ```

- Saída:
  ```JavaScript
  [ 45, 15, 'teste' ]
  7.34
  ```

## 7.6 REMOVE E RETORNA O PRIMEIRO TERMO

```JavaScript
array.shift()
```

- Exemplo:

  ```JavaScript
  array = [45, 15, 'teste', 7.34]
  x = array.shift()
  console.log(array)
  console.log(x)
  ```

- Saída:
  ```JavaScript
  [ 15, 'teste', 7.34 ]
  45
  ```

## 7.7 ADICIONA ELEMENTO AO INICIO

```JavaScript
array.unshift(valor)
```

- Exemplo:

  ```JavaScript
  array = [45, 15, 'teste', 7.34]
  array.unshift(100)
  console.log(array)
  ```

- Saída:
  ```JavaScript
  [ 100, 45, 15, 'teste', 7.34 ]
  ```

## 7.8 DELETANDO ELEMENTO

```JavaScript
delete a[posição] // deixa o espaço indefinido
//ou
a.splice(posição, 1)
```

- Exemplo 1:

  ```JavaScript
  array = [45, 15, 'teste', 7.34]
  delete array[2]
  console.log(array)
  ```

- Saída 1:

  ```JavaScript
  [ 45, 15, <1 empty item>, 7.34 ]
  ```

- Exemplo 2:

  ```JavaScript
  array = [45, 15, 'teste', 7.34]
  array.splice(2, 1)
  console.log(array)
  ```

- Saída 2:
  ```JavaScript
  [ 45, 15, 7.34 ]
  ```

## 7.9 INSERIR ELEMENTOS

```JavaScript
array.splice(posição, numero_de_elementos_a_serem_retirados, novos_elementos)
```

Sem retirar termos do array

- Exemplo:
  ```JavaScript
  array = [1,2,3,4]
  array.splice(2,0,15,18)
  console.log(array)
  ```
- Saída
  ```JavaScript
  //retorna []
  [1, 2, 15, 18, 3, 4]
  ```

Retirando termos do array

- Exemplo:
  ```JavaScript
  array = [1,2,3,4]
  array.splice(2,2,15,18)
  console.log(array)
  ```
- Saída
  ```JavaScript
  //retorna [3, 4]
  [1, 2, 15, 18]
  ```

## 7.10 CONCATENANDO ARRAYS

```JavaScript
array_3 = array_1.concat(array_2, array_n)
```

- Exemplo:

  ```JavaScript
  array_1 = [1,2,3]
  array_2 = [4,5,6]
  array_3 = [7,8,9]
  array_4 = array_1.concat(array_2)
  array_5 = array_1.concat(array_2, array_3)
  console.log(array_1)
  console.log(array_2)
  console.log(array_3)
  console.log(array_4)
  console.log(array_5)
  ```

- Saída:
  ```JavaScript
  [ 1, 2, 3 ]
  [ 4, 5, 6 ]
  [ 7, 8, 9 ]
  [ 1, 2, 3, 4, 5, 6 ]
  [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
  ```

## 7.11 ORDENANDO ARRAY

```JavaScript
array.sort(function(a, b){return a-b})
```

- Exemplo:

  ```JavaScript
  array = [42, 7, 54, 9]
  array.sort(function(a, b){return a-b})
  console.log(array) //o original é modificado
  ```

- Saída:
  ```JavaScript
  [ 7, 9, 42, 54 ]
  ```

## 7.12 INVERTENDO ARRAY

```JavaScript
array.reverse()
```

- Exemplo:

  ```JavaScript
  array = [42, 7, 54, 9]
  array.reverse()
  console.log(array) //o original é modificado
  ```

- Saída:
  ```JavaScript
  [ 9, 54, 7, 42 ]
  ```

## 7.13 MAIOR TERMO DO ARRAY

```JavaScript
Math.max.apply(null, array)
```

- Exemplo:

  ```JavaScript
  array = [42, 7, 54, 9]
  x = Math.max.apply(null, array)
  console.log(x)
  ```

- Saída:
  ```JavaScript
  54
  ```

## 7.14 MENOR TERMO DO ARRAY

```JavaScript
Math.min.apply(null, array)
```

- Exemplo:

  ```JavaScript
  array = [42, 7, 54, 9]
  x = Math.min.apply(null, array)
  console.log(x)
  ```

- Saída:
  ```JavaScript
  7
  ```

## 7.15 LIMPANDO ARRAY

```JavaScript
array = []
```

## 7.16 OBTER ÍNDICE DE UM ELEMENTO

```JavaScript
array.indexOf(termo);
```

- Exemplo:

  ```JavaScript
  array = [42, 7, 54, 9]
  x = array.indexOf(54)
  console.log(x)
  ```

- Saída:
  ```JavaScript
  2
  ```

## 7.17 COPIANDO UM ARRAY

```JavaScript
novo_array = array.slice() //meio na gambiarra
novo_array = array.concat() //meio na gambiarra
```

- Exemplo 1:

  ```JavaScript
  array_1 = [42, 7, 54, 9]
  array_2 = array_1.slice()
  console.log(array_1)
  console.log(array_2)
  ```

- Saída 1:

  ```JavaScript
  [ 42, 7, 54, 9 ]
  [ 42, 7, 54, 9 ]
  ```

- Exemplo 2:

  ```JavaScript
  array_1 = [42, 7, 54, 9]
  array_2 = array_1.concat()
  console.log(array_1)
  console.log(array_2)
  ```

- Saída 2:
  ```JavaScript
  [ 42, 7, 54, 9 ]
  [ 42, 7, 54, 9 ]
  ```

> OBS.: Não utilize `array_2 = array_1` pois isso copia por referência, assim sempre que modificar algo em `array_1` também será modificado em `array_2` e vice e versa.

## 7.18 RETORNAR O TAMANHO DE UM ARRAY

```JavaScript
array.length;
```

- Exemplo:

  ```JavaScript
  array = [42, 7, 54, 9]
  console.log(array.length)
  ```

- Saída:
  ```JavaScript
  4
  ```

## 7.19 ARRAY COM FOR

```JavaScript
array = [valores]
for (i in array){
  // código com i pegando o indice do array
}
```

```JavaScript
array = [valores]
for (i of array){
  // código com i pegando o valor do array
}
```

- Exemplo 1:

  ```JavaScript
  array = [42, 7, 54, 9]

  for (i in array){
      console.log(array[i])
  }
  ```

- Saída 1:

  ```JavaScript
  42
  7
  54
  9
  ```

- Exemplo 2:

  ```JavaScript
  array = [42, 7, 54, 9]

  for (i of array){
      console.log(i)
  }
  ```

- Saída 2:
  ```JavaScript
  42
  7
  54
  9
  ```

## 7.20 FOREACH

O `forEach` irá passar por cada elemento de um array executando uma determinada função. Sendo que essa função pode conter até três parâmetros:

- Valor (obrigatório)
- Índice (opcional)
- Array (opicional)

- Exemplo:

  ```JavaScript
  a = [5,4,6]
  a.forEach(fun)

  function fun(item, index, array){
      console.log(item)
      console.log(index)
      console.log(array)
  }
  ```

- Saída:
  ```JavaScript
  5
  0
  [ 5, 4, 6 ]
  4
  1
  [ 5, 4, 6 ]
  6
  2
  [ 5, 4, 6 ]
  ```

> OBS.: Veja que ele executa a função `fun` três vezes, pois o array possui três elementos, sendo assim ele executa a função uma vez para cada elemento.

# **8. JSON**

- **Recomendados**
  - [Link 1](https://www.youtube.com/watch?v=P81dE-tkaaA): JSON// Dicionário do programador `(Video)`
  - [Link 2](https://www.devmedia.com.br/json-tutorial/25275): JSON Tutorial `(Texto)`
  - [Link 3](https://www.devmedia.com.br/o-que-e-json/23166): O que é JSON `(Texto)`
  - [Link 4](https://www.youtube.com/watch?v=t4Y7jd4h-T8): Aprendendo Javascript/JSON do básico - Aula 1 `(Video)`
  - [Link 5](https://www.youtube.com/watch?v=8deUBCncNaA): Como criar e modificar um Json com Javascript `(Video)`

---

Um json é um objeto js que basicamente é utilizado para comportar informações.

Veja um exemplo de JSON

```JavaScript
base = {'nome':'Lucas',
        'idade': 24
        }
```

Sim, isso é um JSON

E para acessá-lo é bem simples. Basta fazer `base.nome` ou `base.idade`.

- Exemplo:

  ```JavaScript
  base = {'nome':'Lucas',
          'idade': 24
          }

  console.log(base.nome)
  ```

- Saída:
  ```JavaScript
  Lucas
  ```

Porém, é claro que ele pode ser bem mais elaborado. Vejamos como.

```JavaScript
base = [
        {"nome": "Lucas", "idade": 24},
        {"nome": "João", "idade": 25}
       ]
```

Veja que agora cada `{}` é um membro de um array, sendo assim podemos acessar os elementos com a seguinte declaração: `base[posição].atributo`

- Exemplo:

  ```JavaScript
  base = [
          {"nome": "Lucas", "idade": 24},
          {"nome": "João", "idade": 25}
        ]

  console.log(base[0].nome)
  ```

- Saída:
  ```JavaScript
  Lucas
  ```

E claro que podemos ter arrays sendo o valor de um dado atributo. Por exemplo:

```JavaScript
{"pesos": [50, 80, 100]}
```

# **9. JAVASCRIPT ASSINCRONO**

## 9.1 AJAX

O ajax é uma requisição assincrona que fazemos ao backend da nossa aplicação. Ou seja, nossa pagina pode ser atualizada sem precisar ficar recarregando ela.

> OBS.: Antes que já começe a surtar com o ajax, saiba que vamos usar a biblioteca `axios` no proximo tópico, e ela faz nossa vida com o ajax muito mais simples e mais limpa, mas primeiro entenda o ajax em sí e depois vá para ela.

Para seguir com essa parte, você deve criar um arquivo html e um arquivo js (para facilitar coloque os dois na mesma pasta).

- Arquivo HTML

  ```HTML
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <meta http-equiv="X-UA-Compatible" content="ie=edge" />
      <title>Document</title>
    </head>
    <body>
      <script src="ex009 - Ajax.js"></script>
    </body>
  </html>
  ```

> OBS.: Onde está `ex009 - Ajax.js` troque para o nome do seu arquivo js

Agora no arquivo js siga as instruções abaixo.

Para fazer uma requisição ajax, vamos começar definindo uma variável/objeto do tipo `XMLHttpRequest`.

```JavaScript
var xhr = new XMLHttpRequest();
```

Essa classe `XMLHttpRequest` é que nos da acesso a funcionalidade do ajax que nos permite fazer a requisição do servidor.

E para exemplo, vou utilizar a api do github para pegar informações de usuário, assim podemos brincar com o ajax. Você pode dar uma olhada melhor nessa api nesse link [aqui](https://developer.github.com/v3/users/).

Mas para começar a consumir essa api, vamos utilizar o seguinte código (ele vem logo abaixo da declaração da variável):

```JavaScript
xhr.open("GET", "https://api.github.com/users/LucasFDutra");
xhr.send(null); //obrigatório
```

Isso fará com que ocorra um pedido (get) no endereço ao lado, que nesse caso foi é da api do github mais especificamente pedindo as informações do meu usuário.

Agora abra o arquivo html no browser, abra o inspetor (F12 no google chrome), vá em network e você verá que a requisição foi feita, e verá a informação.

Mas agora vamos pegar essa informação e mostrar ela no console. E para isso vamos utilizar a função abaixo:

```JavaScript
xhr.onreadystatechange = function() {
  if (xhr.readyState === 4) {
    //4 indica que houve retorno
    console.log(JSON.parse(xhr.responseText)); // json pois a api do github retorna um json
  }
};
```

Se você notar bem, podemos colocar

```JavaScript
const data = JSON.parse(xhr.responseText);
```

E teremos a informação da api dentro da variável data, e agora sim podemos trabalhar com esses dados. Porém por hora vamos apenas mostar eles no console.

Se quiser, o código completo está aqui abaixo:

```JavaScript
var xhr = new XMLHttpRequest();

xhr.open("GET", "https://api.github.com/users/LucasFDutra");
xhr.send(null);

xhr.onreadystatechange = function() {
  if (xhr.readyState === 4) {
    console.log(JSON.parse(xhr.responseText));
  }
};
```

Recarregue a pagina (daquele mesmo html que criou no inico desse tópico), abra o inspetor no console e você verá o resultado.

```JavaScript
Object
avatar_url: "https://avatars2.githubusercontent.com/u/42756392?v=4"
bio: null
blog: ""
company: null
created_at: "2018-08-28T00:17:43Z"
email: null
events_url: "https://api.github.com/users/LucasFDutra/events{/privacy}"
followers: 1
followers_url: "https://api.github.com/users/LucasFDutra/followers"
following: 1
following_url: "https://api.github.com/users/LucasFDutra/following{/other_user}"
gists_url: "https://api.github.com/users/LucasFDutra/gists{/gist_id}"
gravatar_id: ""
hireable: null
html_url: "https://github.com/LucasFDutra"
id: 42756392
location: null
login: "LucasFDutra"
name: "Lucas Felipe Dutra"
node_id: "MDQ6VXNlcjQyNzU2Mzky"
organizations_url: "https://api.github.com/users/LucasFDutra/orgs"
public_gists: 0
public_repos: 22
received_events_url: "https://api.github.com/users/LucasFDutra/received_events"
repos_url: "https://api.github.com/users/LucasFDutra/repos"
site_admin: false
starred_url: "https://api.github.com/users/LucasFDutra/starred{/owner}{/repo}"
subscriptions_url: "https://api.github.com/users/LucasFDutra/subscriptions"
type: "User"
updated_at: "2019-08-07T04:06:42Z"
url: "https://api.github.com/users/LucasFDutra"
__proto__: Object
```

## 9.2 PROMISES

> OBS.: Antes de iniciar, recicle o código html que utilizou no ajax, troque apenas o nome do arquivo js para condizer com o novo arquivo que você criará agora.

As promises, como o proprio nome diz, são promessas, e essas promessas são funções que vão devolver um resultado, seja ele de sucesso ou erro, porém elas vão devolver esse resultado somente depois de um tempo, e nós não precisamos nos preocupar com o quando esse valor será retornado, pois sabemos que o código js irá continuar sendo executado normalmente.

Pense em uma promisse da seguinte forma: Você pede algo para um amigo, e ele promete que fará essa determinada atividade para você. Então, enquanto seu amigo faz a atividade dele você vai seguindo com a sua vida e em um dado momento seu amigo reaparece dizendo se a tarefa dele deu certo ou errado, e te apresenta o resultado disso.

A construção de uma promisse é dada da seguinte forma:

```JavaScript
const minhaPromise = function() {
    return new Promise(function(resolve, reject){

    });
}
```

`minhaPromise` é o nome da minha promisse, ela é uma função, e retorna uma `Promise` que é uma classe, a qual recebe como parâmetro uma função que recebe duas outras funções como parâmetro a `resolve` e a `reject`.

A `resolve` serve para quando a promise obteve uma resposta de sucesso. A `reject` é para quando a resposta for de falha.

Agora vamos utilizar o código da requisição ajax dentro de uma promise.

```JavaScript
const minhaPromise = function() {
  return new Promise(function(resolve, reject) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://api.github.com/users/LucasFDutra");
    xhr.send(null);

    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          // 200 indica sucesso na requisição
          resolve(JSON.parse(xhr.responseText));
        } else {
          reject("erro na requisição");
        }
      }
    };
  });
};

var resultado = minhaPromise();
console.log(resultado);
```

Veja que temos um `if else` para tratar os dados. Se tivermos `xhr.readyState === 4` quer dizer que houve retorno. Mas se tivermos `xhr.status === 200` quer dizer que o retorno foi um sucesso, então quem trabalha com o sucesso é o resolve. Já se não foi 200 então houve falha, e quem trata falhas é o reject.

Ai depois de tudo, atribuimos a minhaPromise a uma variável resultado e mostramos ela.

Veja o resultado abaixo:

- Saída:

  ```JavaScript
  Promise {<pending>}
  ```

Veja que a resposta da promisse foi um `pending`, isso significa que a resposta da promise está pendente. Ou seja, ele executou o `console.log` antes de ter o resultado da promise. Isso mostra para nós esse propriedade da promisse de ser executada por trás enquanto a aplicação segue seu curso normalmente.

Agora vamos exibir o resultado que a promise retorna (esse é o jeito certo de estar fazendo).

Quando chamamos a promise, colocamos um `.then` e um `.catch` que ficará da seguinte forma:

```JavaScript
minhaPromise()
  .then(function(response) {})
  .catch(function(error) {});
```

Sendo que o `.then` serve para tomarmos uma atitude caso a resposta seja um sucesso (se a promise chegou no resolve). Já o `.catch` é para quando tivermos a resposta como sendo uma falha (se a promise chegou no reject). E veja que em ambas temos uma função como parâmetro, esse função é o que será executado de acordo com sucesso ou falha.

Agora se eu quiser exibir o resultado da promise em caso de sucesso e exibir uma mensagem de erro em caso de falha (a qual definimos que seria "erro na requisição"), é só fazer o seguinte código:

```JavaScript
minhaPromise()
  .then(function(response) {
    console.log(response);
  })
  .catch(function(error) {
    console.log(error);
  });
```

Se o código estiver correto, então o que vamos receber é a resposta que veio da api do github. Mas se modificarmos o endereço da api, para um endereço invalido, como por exemplo: `"http://api11111111.github.com/users/LucasFDutra"` a nossa promise tentará encontrar o endereço, irá ocorrer um erro então vamos receber a seguinte mensagem:

- Saída:
  ```JavaScript
  erro na requisição
  ```

## 9.3 ASYNC/AWAIT

O async/await é nada mais que uma promise, porém escrita de uma forma mais bonitinha.

A construção da função promise é exatamente igual, o que muda é que agora não usamos mais o `.then` e o `.catch`, a escrita agora ficará da seguinte forma:

```JavaScript
const functionName = async () => {
  const resposta = await minhaPromise();
};

functionName();
```

Basicamente estamos dizendo aqui é: A minha função `functionName`, vai esperar (await) a resposta de uma função assincrona (async), que nesse caso é a nossa promise e vai guardar isso em uma variável resposta.

Nesse caso, o nosso código completo fica:

```JavaScript
const minhaPromise = function() {
  return new Promise(function(resolve, reject) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://api.github.com/users/LucasFDutra");
    xhr.send(null);

    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          // 200 indica sucesso na requisição
          resolve(JSON.parse(xhr.responseText));
        } else {
          reject("erro na requisição");
        }
      }
    };
  });
};

const promessa = async () => {
  const resposta = await minhaPromise();
  console.log(resposta);
};

promessa();
```

Obtem-se na saída os dados da api do github.

Porém se trocarmos a url (forçar um erro), essa forma base não serve, pois a `resposta` só irá pegar a resposta caso ela seja sucesso. Para isso, temos que utilizar o `try/catch`.

```JavaScript
const promessa = async () => {
  try {
    const resposta = await minhaPromise();
    console.log(resposta);
  } catch (error) {
    console.log(error);
  }
};

promessa();
```

Mude o código para ficar com essa forma, e troque o endereço da api e mande rodar, você vará que a mensagem que pré-configuramos irá aparecer.

## 9.4 [AXIOS](https://github.com/axios/axios)

Agora sim, a biblioteca axios vai nos ajudar a fazer as requisições ajax de uma forma um pouco mais simples.

Mas primeiro vamos adicionar o axios ao nosso projeto. Copie aquele mesmo .html que estamos usando, e ajuste ele para o novo arquivo js. Coloque a seguinte linha nele:

```HTML
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```

Deixando o body do código da seguinte forma:

```HTML
<body>
  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  <script src="ex012 - axios Promise.js"></script>
</body>
```

> OBS.: O axios tem que vir antes do arquivo js.

### **9.4.1 Axios com promises**

Agora o arquivo js completo, fica da seguinte forma:

```JavaScript
axios.get("https://api.github.com/users/LucasFDutra")
  .then(function(response) {
    console.log(response);
  })
  .catch(function(error) {
    console.log(error);
  });
```

Você notou que o axios já construiu toda aquela estrutura que antes nos tinhamos feito com o `minhaPromise`? Pois é, ele facilita bastante nossa vida.

Porém, quando você rodar isso, você verá no seu console que ele agora retorna um objeto com mais de um campo além do data, que é o que estavamos acostumados no método com ajax, mas note que um dos campos do objeto é justamente o campo `data`, em que todo o nosso conteúdo de interesse está alocado:

```JavaScript
Object
> config:{...}
> data: {...}
> headers: {...}
> request: XMLHttpRequest {...}
  status: 200
  statusText: "OK"
  __proto__: Object
```

Dai se eu quiser pegar especificamente o resultado de `data`, é só eu fazer o seguinte:

```JavaScript
axios.get("https://api.github.com/users/LucasFDutra")
  .then(function(response) {
    console.log(response.data);
  })
  .catch(function(error) {
    console.log(error);
  });
```

Assim a resposta retornará apenas o que tiver em `data`, e como data é um objeto eu poderia colocar `response.data.login` para pegar apenas o login, e assim por diante.

### **9.4.2 Axios com async/await**

A chamada do axios acontece da seguinte forma:

```JavaScript
const promessa = async () => {
  try{
    const resposta = await axios.get("https://api.github.com/users/LucasFDutra");
    console.log(resposta);
  } catch (error) {
    console.log(error)
  }
};

promessa();
```

e como resposta temos também o objeto:

```JavaScript
Object
> config:{...}
> data: {...}
> headers: {...}
> request: XMLHttpRequest {...}
  status: 200
  statusText: "OK"
  __proto__: Object
```

e assim como na promise, podemos obter os dados fazendo `resposta.data`.
