# Notas de estudo

Autor: Lucas Felipe Dutra

Basicamente essa foi a primeira versão da apostila de javascript, por isso muito do que tem lá vai ter aqui. Porém aqui não está de uma forma que fiquei satisfeito. Mas o material ainda é valido.

# SUMÁRIO

- [**1. ESTRUTURANDO**](#1-estruturando)
- [**2. VARIÁVEIS**](#2-variáveis)
  - [2.1 CONVERSÃO DE VARIÁVEIS](#21-conversão-de-variáveis)
  - [2.2 FORMATANDO STRINGS](#22-formatando-strings)
  - [2.3 FORMATANDO NÚMEROS](#23-formatando-números)
- [**3. ESCREVENDO NA TELA**](#3-escrevendo-na-tela)
- [**4. DOM**](#4-dom)
  - [4.1 ÁRVORE DOM](#41-árvore-dom)
    - [4.1.1 Window](#411-window)
    - [4.1.2 Document](#412-document)
  - [4.2 SELECIONANDO ELEMENTOS](#42-selecionando-elementos)
    - [4.2.1 Por Marca](#421-por-marca)
    - [4.2.2 Por ID](#422-por-id)
    - [4.2.3 Por Nome](#423-por-nome)
    - [4.2.4 Por Classe](#424-por-classe)
    - [4.2.5 Por Seletor](#425-por-seletor)
  - [4.3 EVENTOS DOM](#43-eventos-dom)
- [**5. CONDICIONAIS**](#5-condicionais)
  - [5.1 IF](#51-if)
  - [5.2 ELSE IF](#52-else-if)
  - [5.3 ELSE](#53-else)
  - [5.4 OPERADORES](#54-operadores)
- [**6. ADICIONANDO ARQUIVOS CSS E JS SEPARADOS DO HTML**](#6-adicionando-arquivos-css-e-js-separados-do-html)
- [**7. ESTRUTURAS DE REPETIÇÕES**](#7-estruturas-de-repetições)
  - [7.1 FOR](#71-for)
  - [7.2 WHILE](#72-while)
  - [7.3 DO WHILE](#73-do-while)
  - [7.4 BREAK](#74-break)
- [**8. Arrays**](#8-arrays)
  - [8.1 DECLARAÇÃO](#81-declaração)
  - [8.2 INSERINDO NOVOS TERMOS](#82-inserindo-novos-termos)
  - [8.3 ACESSAR UM TERMO](#83-acessar-um-termo)
  - [8.4 MUDANDO UM TERMO](#84-mudando-um-termo)
  - [8.5 REMOVE E RETORNAR O ULTIMO TERMO](#85-remove-e-retornar-o-ultimo-termo)
  - [8.6 REMOVE E RETORNA O PRIMEIRO TERMO](#86-remove-e-retorna-o-primeiro-termo)
  - [8.7 ADICIONA ELEMENTO AO INICIO](#87-adiciona-elemento-ao-inicio)
  - [8.8 DELETANDO ELEMENTO](#88-deletando-elemento)
  - [8.9 INSERIR ELEMENTOS](#89-inserir-elementos)
  - [8.10 CONCATENANDO ARRAYS](#810-concatenando-arrays)
  - [8.11 ORDENANDO ARRAY](#811-ordenando-array)
  - [8.12 INVERTENDO ARRAY](#812-invertendo-array)
  - [8.13 MAIOR TERMO DO ARRAY](#813-maior-termo-do-array)
  - [8.14 MENOR TERMO DO ARRAY](#814-menor-termo-do-array)
  - [8.15 LIMPANDO ARRAY](#815-limpando-array)
  - [8.16 OBTER ÍNDICE DE UM ELEMENTO](#816-obter-índice-de-um-elemento)
  - [8.17 COPIANDO UM ARRAY](#817-copiando-um-array)
  - [8.18 RETORNAR O TAMANHO DE UM ARRAY](#818-retornar-o-tamanho-de-um-array)
  - [8.19 ARRAY COM FOR](#819-array-com-for)
  - [8.20 FOREACH](#820-foreach)
- [**9. MÉTODOS/FUNÇÕES**](#9-métodosfunções)
  - [9.1 FUNCÕES ANÔNIMAS](#91-funcões-anônimas)
  - [9.2 ARROW FUNCTIONS](#92-arrow-functions)
  - [9.3 FUNÇÕES CALLBACK](#93-funções-callback)
  - [9.4 IIFE](#94-iife)
- [**10. JSON**](#10-json)
  - [10.1 LER ARQUIVO JSON](#101-ler-arquivo-json)
- [**11. POO**](#11-poo)
  - [11.1 CLASSES](#111-classes)
    - [**11.1.1 A partir do Class**](#1111-a-partir-do-class)
    - [**11.1.2 A partir de uma função**](#1112-a-partir-de-uma-função)
    - [**11.1.3 A partir de uma função segunda maneira**](#1113-a-partir-de-uma-função-segunda-maneira)
  - [11.3 VISIBILIDADE](#113-visibilidade)
  - [11.4 MÉTODOS ESPECIAIS (GETTERS, SETTERS E CONSTRUCTS)](#114-métodos-especiais-getters-setters-e-constructs)
  - [11.5 RELACIONAMENTO ENTRE CLASSES](#115-relacionamento-entre-classes)
  - [11.6 HERANÇA](#116-herança)
  - [11.7 POLIMORFISMO](#117-polimorfismo)
    - [**11.7.1 Polimorfismo de sobreposição**](#1171-polimorfismo-de-sobreposição)

# **1. ESTRUTURANDO**

Em meio ao arquivo HTML podemos colocar os comando CSS e o código JS.

- Colocando CSS: Coloque a tag `<style>` e entre ela escreva o CSS.

- Colocando JS: Coloque a tag `<script>` e entre ela escreva o JS.

Claro que o melhor é que esses códigos estejam em arquivos separados, mas para inicio podemos colocar o seguinte exemplo:

- Exemplo:

  ```HTML
  <!DOCTYPE html>
  <html lang="pt-br">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Primeiro Programa</title>
      <style>
          body{
              background-color: rgb(115, 115, 170);
              color: white;
              font-size: normal 20pt Arial;
          }
      </style>
  </head>
  <body>
      <h1>Olá mundo!</h1>
      <p>Arquivo html para teste</p>
      <script>
          window.alert('Minha primeira mensagem')
      </script>
  </body>
  </html>
  ```

- Saída:
  O comando JS faz aparecer o alerta

  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/Imagens/Figura_01.png?raw=true)

Após clicar em "OK", o body aparece configurado confome o CSS

![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/Imagens/Figura_02.png?raw=true)

# **2. VARIÁVEIS**

Para atribuir variáveis utilizamos o `var` antes da variável.

> OBS.: O tipo de variável é reconhecida automaticamente pelo JS.

```JavaScript
var nome_da_variavel = valor
```

```JavaScript
//string
var nome = 'nome'
//numeros
var numero1 = 1
var numero2 = 3.14
//boolean
var teste = true
var teste = false
```

> OBS.: Para reduzir o tamanho do código, irei colocar apenas a parte referente ao JavaScript (ou seja, entre a tag script). Porém todo o código estará no link que deixarei a seguir.

- Exemplo 1: [Código Completo](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/C%C3%B3digos/aula05/ex002.html)

  ```JavaScript
  <script>
    var nome = window.prompt('Qual o seu nome?') //recebe o nome
    window.alert('é um prazer te conhecer '+nome) // mostra o nome
  </script>
  ```

- Saída 1:

  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/Imagens/Figura_03.png?raw=true)

  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/Imagens/Figura_04.png?raw=true)

- Exemplo 2: [Código Completo](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/C%C3%B3digos/aula05/ex003.html)

  ```JavaScript
  <script>
      var numero1 = window.prompt('digite um numero: ')
      var numero2 = window.prompt('digite outro numero: ')
      numero1 = Number.parseInt(numero1) // converter para int
      numero2 = Number.parseInt(numero2) // converter para int
      var soma = numero1+numero2 // efetua a soma
      window.alert('a soma dos numeros é: '+soma) // mostra o resultado da soma
      // outra opção porém note que tem que ter a crase e não aspas simples
      window.alert(`a soma dos numeros é: ${soma}`) // mostra o resultado da soma
  </script>
  ```

- Saída 2:

  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/Imagens/Figura_05.png?raw=true)

  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/Imagens/Figura_06.png?raw=true)

  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/Imagens/Figura_07.png?raw=true)

> OBS.: Foi necessário converter os números digitados para inteiros, pois o retorno de window.prompt é uma string.

## 2.1 CONVERSÃO DE VARIÁVEIS

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

# **3. ESCREVENDO NA TELA**

Vamos mostrar coisas escritas na tela do browser. Para isso vamos utilizar o comando `document.write`.

- Exemplo: [Código Completo](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/C%C3%B3digos/aula05/ex004.html)

  ```JavaScript
  <script>
      var nome = window.prompt('digite seu nome: ') // pede o nome
      document.write(`olá ${nome}</br>`) // mostra o nome e pula uma linha com </br>
      document.write(`<b>como vai você?</b>`) // pergunta como está em negrito com <b>
  </script>
  ```

- Saída:

  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/Imagens/Figura_08.png?raw=true)

  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/Imagens/Figura_09.png?raw=true)

# **4. DOM**

Antes de qualquer coisa, se ao ler o que escrito aqui nessa seção achar que tudo está meio vago, ou confuso, te pesso duas coisas:

- Primeiro: veja esses links
  - [Link 1](https://medium.com/@mateusdamasceno/utilizando-dom-em-javascript-4683c3b9395a)
  - [Link 2](https://www.youtube.com/watch?v=WWZX8RWLxIk&list=PLHz_AreHm4dlsK3Nr9GVvXCbpQyHQl1o1&index=15)
  - [Link 3](https://www.w3schools.com/js/js_htmldom.asp)
  - [Link 4](https://www.devmedia.com.br/trabalhando-com-dom-em-javascript/29039)
- Segundo: Depois que entender melhor, se puder contribuir editando esse arquivo e mandando um pull request eu agradeço muito.

DOM significa Document Object Model. Que é um conjunto de objetos dentro do navegador que irá dar acesso aos componentes internos do site.

## 4.1 ÁRVORE DOM

### 4.1.1 Window

A raiz da árvore é a `window`, que seria toda a janela do navegador.

Dentro da window temos 3 outros objetos o `location`, `document` e `history`.

- location: Diz qual a localização do site, ou seja, a URL, qual a página atual, qual a página anterior.
- document: Documento atual.
- history: Diz em que página o navegador estava antes (usar o botão de voltar).

### 4.1.2 Document

Dentro de document temos o arquivo HTML, sendo que dentro do html temos o `head` e `body`. Sendo que dentro desses dois temos outros componentes, como `meta`, `title`, `h1`, `p`, `div` entre outros.

Veja na imagem abaixo um exemplo de arvore DOM

![](https://www.todoespacoonline.com/w/wp-content/uploads/2014/05/Diagrama1.png)

Fonte: [O DOM E JAVASCRIPT – MANIPULANDO A PÁGINA HTML](https://www.todoespacoonline.com/w/2014/05/dom-e-javascript/)

E isso é importante pois sabendo qual o nome de cada componente e o que eles são, podemos começar a utilizar o JS para modificar a nossa página.

Veja no exemplo do gif abaixo que a sentença é feita da seguinte forma `window.document.write` ou seja, será escrito no documento que está dentro da janela.

![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/Imagens/Figura_10.gif?raw=true)

> OBS.: Utilize o visual code com a extensão Watch in Chrome para que a página seja modificada conforme digita os códigos.

## 4.2 SELECIONANDO ELEMENTOS

Antes de tudo, veja o que são tags, ids, classes lá em HTML.

### 4.2.1 Por Marca

Utiliza o comando `getElementsByTagName()`. Ou seja, o elemento será selecionado pela sua tag HTML. Sendo assim se colocarmos para selecionar pela tag `<div>` todos os elementos que utilizam essa tag serão selecionados. Por isso na hora de exibir temos que escolher qual será o elemento exibido.

- Por exemplo, se tivermos 3 elementos com a tag `<p>`
  - <p>texto 0</p>
  - <p>texto 1</p>
  - <p>texto 2</p>
- Se fizermos a seleção por marca teremos então um elemento `a` que contém esses tres elementos `p`, logo se fizermos

  - a[0]: texto 0
  - a[1]: texto 1
  - a[2]: texto 2

- Exemplo:

  ```JavaScript
  <body>
      <h1>Iniciando estudos com o DOM</h1>
      <p>Aqui vai o resultado</p>
      <p>Aprendendo a usar o <b>dom<b> em JavaScript</b></p>
      <div>Clique em mim</div>
      <button>Clique aqui</button></br>
      <script>
          var p1 = window.document.getElementsByTagName('p')[0]
          window.document.write(p1.innerText) // innerText signica que queremos pegar o texto que está em p1
      </script>
  </body>
  ```

- Saída:

  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/Imagens/Figura_11.png?raw=true)

> OBS.: A última linha é a linha de saída

Se derrepente eu quiser mudar o que acontece com o elemento P1 é só eu fazer `p1.alguma_coisa`.

- Exemplo

  ```JavaScript
  p1.style.color = 'black'
  ```

- Saída:

  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/Imagens/Figura_12.png?raw=true)

Veja que agora podemos brincar com isso. Se atribuirmos variáveis para as partes da nossa window podemos modificar os textos, utilizá-los, modificar o css.

Veja alguns exemplos com o gif abaixo

![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/Imagens/Figura_13.gif?raw=true)

### 4.2.2 Por ID

Tudo que foi feito utilizando as tags pode ser feito com o uso do ID com `getElementByID()`

![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/Imagens/Figura_14.gif?raw=true)

### 4.2.3 Por Nome

Tudo que foi feito utilizando as tags pode ser feito com o uso do Name com `getElementsByName()`

### 4.2.4 Por Classe

Tudo que foi feito utilizando as tags pode ser feito com o uso do Class com `getElementsByClassName()`

### 4.2.5 Por Seletor

Agora temos uma diferença, que é utilizando o `querySelector()` ou `querySelectorAll()`.

![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/Imagens/Figura_15.gif?raw=true)

## 4.3 EVENTOS DOM

Existem vários eventos, e nesse [link](https://developer.mozilla.org/en-US/docs/Web/Events) você pode ver a lista completa. Porém aqui irei mostrar alguns utilizando um exemplo.

Veja o gif abaixo, cujo código completo está [aqui](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/C%C3%B3digos/aula10/ex006.html).

![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/Imagens/Figura_16.gif?raw=true)

Outro método de fazer isso, com o código mais limpo (é o que vai ficar na versão final) é essa mostrada no gif abaixo.

![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/Imagens/Figura_17.gif?raw=true)

Veja o exemplo abaixo cujo código está [aqui](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/C%C3%B3digos/aula10/ex007.html)

![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/Imagens/Figura_18.gif?raw=true)

# **5. CONDICIONAIS**

## 5.1 IF

```JavaScript
if (condição){
  // Código...
}
```

## 5.2 ELSE IF

É uma condição que só é analisada caso a condição em `if` não seja atendida.

```JavaScript
else if (condição){
  // Código...
}
```

## 5.3 ELSE

Engloba tudo que for o contrário das condições impostas em `if` e `else if`.

```JavaScript
else{
  // Código...
}
```

## 5.4 OPERADORES

- **&&:** Condição 'a' e condição 'b' devem ser atendidas.

- **||:** Condição 'a' ou condição 'b' devem ser atendidas.

- **maior:** >

- **maior ou igual:** >=

- **menor:** <

- **menor ou igual:** <=

- **diferente:** !=

- **igual:** ==

- **identicos:** ===

- **Verdadeiro:** true

- **Falso:** false

> OBS.: cuidado com os operadores `==` e `===` o `==` não olha o tipo de dados, já o `===` olha. Veja o exemplo
> 5 == '5' True
> 5 === '5' False
> 5 === 5 True

- Exemplo 1:

  ```JavaScript
  var a = 1
  var b = 2

  if (a == b){
      console.log("'a' é igual à 'b'") // console.log seria o printf do JS
      }
  else if (a > b){
      console.log("'a' é maior do que 'b'")
  }
  else if(a==2 || a==3){
      console.log("'a' é igual a 2 ou igual a 3")
  }
  else if(a==2 && b==3){
      console.log("'a' é igual a 2 e 'b' é igual a 3")
  }
  else{
      console.log("'a' é diferente de 'b'")
  }
  ```

- Saída 1:
  ```JavaScript
  'a' é diferente de 'b'
  ```

Vejamos um exemplo com o brower, em que iremos pedir dois valores e iremos verificar as condições igual ao exemplo acima.

- Exemplo 2: [Código Completo](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/C%C3%B3digos/aula11/ex008.html)

  ```JavaScript
  <body>
      <h1>Verificando números</h1>
      <input type="number" id = "n1">
      <input type="number" id = "n2">
      <input type="button" value="Análise" onclick="clicar()">
      <div id="res">Resposta</div>
      <script>
          function clicar(){
              var n1 = window.document.querySelector('input#n1')
              var n2 = window.document.querySelector('input#n2')
              var res = window.document.querySelector('div#res')

              var a = Number.parseFloat(n1.value)
              var b = Number.parseFloat(n2.value)

              if (a == b){
                  res.innerHTML = "'a' é igual à 'b'"
              }
              else if (a > b){
                  res.innerHTML = "'a' é maior do que 'b'"
              }
              else if(a==2 || a==3){
                  res.innerHTML = "'a' é igual a 2 ou igual a 3"
              }
              else if(a==2 && b==3){
                  res.innerHTML = "'a' é igual a 2 e 'b' é igual a 3"
              }
              else{
                  res.innerHTML = "'a' é diferente de 'b'"
              }
          }
      </script>
  </body>
  ```

- Saída

![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/Imagens/Figura_19.png?raw=true)

# **6. ADICIONANDO ARQUIVOS CSS E JS SEPARADOS DO HTML**

Para um código mais limpo, é viável que os arquivos html, css e js estejam separados, para isso é só fazer conforme a imagem abaixo.

Indico que veja os vídeos do curso em video, pois tem muito conteúdo bom e foi de onde retirei as ideias dos programas criados abaixo.

- [Video 1](https://www.youtube.com/watch?v=b2K7eo5Jdj8&list=PLHz_AreHm4dlsK3Nr9GVvXCbpQyHQl1o1&index=20)
- [Video 2](https://www.youtube.com/watch?v=UXSWgnbSHxs&list=PLHz_AreHm4dlsK3Nr9GVvXCbpQyHQl1o1&index=21)
- [Video 3](https://www.youtube.com/watch?v=f5es-PpaUI8&list=PLHz_AreHm4dlsK3Nr9GVvXCbpQyHQl1o1&index=22)

  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/Imagens/Figura_20.png?raw=true)

Esse é o protótipo de um pequeno site que verifica se está de dia, tarde ou noite de acordo com o horario do computador.

Veja a execução no gif abaixo e o site completo [aqui](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/tree/master/C%C3%B3digos%20JS/aula12/ex009)

![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/Imagens/Figura_21.gif?raw=true)

Veja também esse outro exemplo, que é mostrado no gif abaixo, em que de acordo com uma idade e sexo uma imagem é mostrada. O código completo está [aqui](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/tree/master/C%C3%B3digos%20JS/aula12/ex010)

![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/Imagens/Figura_22.gif?raw=true)

# **7. ESTRUTURAS DE REPETIÇÕES**

## 7.1 FOR

```JavaScript
for(inicialização; condição; incremento){
    // Código...
}
```

- Exemplo:
  ```JavaScript
  for(i=0; i<10; i++){
      console.log(i)
  }
  ```
- Saída:
  ```JavaScript
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
  ```

## 7.2 WHILE

```JavaScript
while(condição){
  // Código...
}
```

- Exemplo:

  ```JavaScript
  i = 0
  while(i<10){
      console.log(i)
      i++
  }
  console.log(`o valor de i após o while: ${i}`)
  ```

- Saída:
  ```JavaScript
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
  O valor de i após o while: 10
  ```

## 7.3 DO WHILE

A diferença entre o `do while` e `while` é que no `do while` o código é executado primeiro e depois que a condição é verificada.

```JavaScript
do{
  // Código...
}while(condição)
```

- Exemplo:

  ```JavaScript
  i = 0
  do{
      console.log(i)
      i++
  }while(i<10)
  console.log(`o valor de i após o while: ${i}`)
  ```

- Saída:
  ```JavaScript
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
  O valor de i após o do While: 10
  ```

## 7.4 BREAK

O comando `break` serve para interromper um loop caso alguma condição especial ocorra.

- Exemplo:

  ```JavaScript
  for (i=0; i<10; i++){
      console.log(i)
      if(i==5){
          break
      }
  }
  ```

- Saída:
  ```JavaScript
  0, 1, 2, 3, 4, 5,
  ```

Veja o exemplo do gif abaixo que mostra a tabuada de um número. O exemplo é bem simples, inclusive nem utilizei contenções para os erros, mas trabalhei um pouco a parte de CSS, então vale a pena dar uma olhada no [Código Completo](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/tree/master/C%C3%B3digos%20JS/aula14).

![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/Imagens/Figura_23.gif?raw=true)

# **8. Arrays**

## 8.1 DECLARAÇÃO

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

## 8.2 INSERINDO NOVOS TERMOS

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

## 8.3 ACESSAR UM TERMO

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

## 8.4 MUDANDO UM TERMO

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

## 8.5 REMOVE E RETORNAR O ULTIMO TERMO

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

## 8.6 REMOVE E RETORNA O PRIMEIRO TERMO

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

## 8.7 ADICIONA ELEMENTO AO INICIO

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

## 8.8 DELETANDO ELEMENTO

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

## 8.9 INSERIR ELEMENTOS

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

## 8.10 CONCATENANDO ARRAYS

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

## 8.11 ORDENANDO ARRAY

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

## 8.12 INVERTENDO ARRAY

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

## 8.13 MAIOR TERMO DO ARRAY

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

## 8.14 MENOR TERMO DO ARRAY

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

## 8.15 LIMPANDO ARRAY

```JavaScript
array = []
```

## 8.16 OBTER ÍNDICE DE UM ELEMENTO

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

## 8.17 COPIANDO UM ARRAY

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

## 8.18 RETORNAR O TAMANHO DE UM ARRAY

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

## 8.19 ARRAY COM FOR

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

## 8.20 FOREACH

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

## **9. MÉTODOS/FUNÇÕES**

- [Link](https://www.youtube.com/watch?v=zNimSYkrs6w)

```JavaScript
function nome_da_função(parâmetros){
  // Código...
}
```

- Exemplo 1:

  ```JavaScript
  function soma(a, b){
      return a+b
  }

  soma = soma(1, 3)
  console.log(soma)
  ```

- Saída 1:

  ```JavaScript
  4
  ```

- Exemplo 2:

  ```JavaScript
  function soma(a, b){
      x = a[1]
      y = b[1]
      return(x+y)
  }

  n1 = [1,2,3,4]
  n2 = [2,4,6]

  soma = soma(n1, n2)
  console.log(soma)
  ```

- Saída 2:
  ```JavaScript
  6
  ```

## 9.1 FUNCÕES ANÔNIMAS

No JS podemos escrever funções anônimas que seriam funções atribuidas a variáveis.

```JavaScript
variavel = function(parametros){
  // código
}
```

- Exemplo:

  ```JavaScript
  s = function(a, b){
      return (a+b)
  }
  console.log(s(1,2))
  ```

- Saída:
  ```JavaScript
  3
  ```

Veja que agora ao em vez de char a função por um nome qualquer podemos chamá-la por s. Ou seja, a função foi atribuida a uma variável.

## 9.2 ARROW FUNCTIONS

- [Link](https://www.youtube.com/watch?v=AgOwGKB8D2M)

Arrow functions são um jeito diferente e mais fácil de fazer funções anônimas. Temos dois métodos de fazer isso, o primeiro é quando temos um corpo para a função, ou seja, ela possui códigos dentro dela.

```JavaScript
variavel = (parametros)=>{
  // Código
}
```

O outro modelo é quando a função tem apenas o return, sendo assim podemos declará-la da seguinte forma

```JavaScript
variavel = (parametros) => //expressão
```

- Exemplo 1:

  ```JavaScript
  s = (a, b) => {
      soma = a+b
      return soma
  }
  console.log(s(1,2))
  ```

- Saída 1:

  ```JavaScript
  3
  ```

- Exemplo 2:

  ```JavaScript
  s = (a, b) => a+b
  console.log(s(1,2))
  ```

- Saída 2:
  ```JavaScript
  3
  ```

Com arrays, podemos utilizar a função `map` em conjunto com arrow functions e efetuaremos algumas operações com arrays bem rápido.

- Exemplo 3:

  ```JavaScript
  array = [1,2,3]
  array_2 = array.map(valor => valor*2) //map recebe os valores do array e passa como parametro
  console.log(array_2)
  ```

- Saída
  ```JavaScript
  [ 2, 4, 6 ]
  ```

> OBS.: Arrow functions possuem limitações quanto ao uso do `this` em POO, porém não vem ao caso abordar isso agora, mas veja o video recomendado no link que deixei anteriormente, para entender um pouco melhor.

## 9.3 FUNÇÕES CALLBACK

Eu poderia ficar aqui explicando o que é uma função callback, mas honestamente eu acho desnecessário, pois alguém já fez isso de uma forma muito melhor do que eu poderia trazer aqui, e esse ser humano abençoado colocou tudo em um post no medium, que está nesse link [aqui](https://medium.com/totvsdevelopers/entendendo-fun%C3%A7%C3%B5es-callback-em-javascript-7b500dc7fa22).

## 9.4 IIFE

IIFE: Immediately Invoked Function Expression

Ou seja, uma função que será invocada assim que criada.

Como fazer isso? bem, veja abaixo:

```JavaScript
(function(parametro){//código})(passar_parametro)
```

- Exemplo:

  ```JavaScript
  (function(i){console.log(i)})(1)
  ```

- Saída:
  ```JavaScript
  1
  ```

Recomendo que veja esse vídeo [aqui](https://www.youtube.com/watch?v=eY7u388cvM4)

E também uma lida nesse post [aqui](https://medium.com/javascript-in-plain-english/https-medium-com-javascript-in-plain-english-stop-feeling-iffy-about-using-an-iife-7b0292aba174)

# **10. JSON**

Um json é um objeto js que basicamente é utilizado para comportar informações. Veja o [vídeo](https://www.youtube.com/watch?v=P81dE-tkaaA).

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

Veja os vídeos abaixo:

- [Link 1](https://www.youtube.com/watch?v=t4Y7jd4h-T8)
- [Link 2](https://www.youtube.com/watch?v=8deUBCncNaA)

## 10.1 LER ARQUIVO JSON

> OBS.: Não tem dado muito certo, então estou esperando conseguir para prosseguir com isso... maas até lá irei escrever a parte de POO

# **11. POO**

Toda a base teorica para POO está na apostila de POO, que também foi escrita por mim. Então todo o conteúdo que colocarei aqui nessa apostila está baseado na teoría da apostila de POO, então abra ela ai também e acompanhe as duas juntas. A mesma está nesse [link](https://github.com/LucasFDutra/Minha-Apostila-De-POO).

E aqui vão umas referências pra ajudar mais um pouco:

- [Link 1](https://www.devmedia.com.br/poo-trabalhando-com-classes-e-objetos-em-javascript/28434)
- [Link 2](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Introduction_to_Object-Oriented_JavaScript)
- [Link 3](https://www.w3schools.com/js/js_classes.asp)

## 11.1 CLASSES

O JavaScript é diferente do restante, e para a criação de classe não utilizamos a denominação `class`, apesar de ser possível.

### **11.1.1 A partir do Class**

Mas vamos lá, vamos mostrar o como criar uma classe com o uso do `class`, mas ressalto que não é a melhor ideia (mas sério, é muito mais fácil com o class).

Nesse video [aqui](https://www.youtube.com/watch?v=po9Ik_v5koU) o cara explica o porque de não usar o `class`.

Nesse video [aqui](https://www.youtube.com/watch?v=ACZi0KRIsoc) ele fala o porque o `this` não é muito viável.

```JavaScript
class ClassName{
  constructor(parametros){
    // Atributos
  }

  // métodos
}

nome_do_objeto = new ClassName(parametros)
nome_do_objeto.método()
```

- Exemplo:

  ```JavaScript
  class Pessoa {
      constructor(nome_1){
          this.nome = nome_1
          this.idade = 24
      }
      mostrarNome() {
          console.log(this.nome)
          console.log(this.idade)
      }
  }

  nome = new Pessoa('Lucas') //passando o nome assim que constroi
  nome.mostrarNome() // chamando o método mostrar nome
  ```

- Saída:
  ```JavaScript
  Lucas
  24
  ```

### **11.1.2 A partir de uma função**

Esse é o melhor método para criar uma classe em JS.

```JavaScript
function ClassName(parametros){
  // Atributos

  return{
    // arow function 1 (método 1),
    // arrow function 2 (método 2),
    // ...
  }
}

nome_do_objeto = new ClassName(parametros)
nome_do_objeto.arrow_function_name()
```

Com a classe declarada desse forma, o construtor passa a ser a propria função.

> OBS.: **não precisa ser necessariamente uma arrow function, mas é melhor pois evita problemas com o this, assim como foi visto no video recomendado do porque não utilizar o class (serio, vê esse video).**

- Exemplo:

  ```JavaScript
  function Pessoa(nome){
      this.nome = nome
      this.idade = 24

      return {
          mostrarNome: ()=>{
              console.log(this.nome)
          },
          mostrarIdade: () => console.log(this.idade)
      }
  }
  nome = new Pessoa('Lucas')
  nome.mostrarNome()
  nome.mostrarIdade()
  ```

- Saída:
  ```JavaScript
  Lucas
  24
  ```

### **11.1.3 A partir de uma função segunda maneira**

Agora vamos fazer de uma forma que fica um pouco mais entendivel para quem vem de outras linguagens. Nos não utilizaremos arrow functions, e não utilizaremos aquele `return`.

```JavaScript
function ClassName(parametros){
  // Atributos
  // this.metodo = metodo

  // metodos
}
nome_do_objeto = new ClassName(parametros)
nome_do_objeto.metodo()
```

- Exemplo:

```JavaScript
function Pessoa(nome){
    nome = nome
    idade = 24
    this.mostrarNome = mostrarNome
    this.mostrarIdade = mostrarIdade

    function mostrarNome(){
        console.log(nome)
    }
    function mostrarIdade(){
        console.log(idade)
    }
}

pessoa = new Pessoa('Lucas')
pessoa.mostrarNome()
pessoa.mostrarIdade()
```

- Saída:
  ```JavaScript
  Lucas
  24
  ```

> OBS.: Veja que é necessário identificar as função lá em cima junto ao this, é esse o nome que usaremos para chamar o método. Por exemplo, se fosse feito `this.a = mostrarNome` iriamos utilizar `pessoa.a()`

Outro modo de fazer, seria assim (meu favorito e o que mais trabalharei aqui):

```JavaScript
function Pessoa(nome){
    nome = nome
    idade = 24

    this.mostrarNome = function(){
        console.log(nome)
    }
    this.mostrarIdade = function(){
        console.log(idade)
    }
}

pessoa = new Pessoa('Lucas')
pessoa.mostrarNome()
pessoa.mostrarIdade()
```

Afinal, se você notar, ao fazer `this.metodo = metodo` estamos atribuindo o metodo a uma variável, logo daria na mesma que fazer uma função anonima. E se você já pegou o jeito, isso implica que também podemos utilizar arrow functions dessa mesma forma, veja abaixo.

```JavaScript
function Pessoa(nome){
    nome = nome
    idade = 24

    this.mostrarNome = () => {
        console.log(nome)
    }
    this.mostrarIdade = () => {
        console.log(idade)
    }
}

pessoa = new Pessoa('Lucas')
pessoa.mostrarNome()
pessoa.mostrarIdade()
```

**Agora vamos entender o problema com o this.**

Se fizermos do mesmo jeito que está nos exemplos anteriores, utilizando

```JavaScript
function mostrarNome(){
    console.log(nome)
}
```

Vamos obter o nome `Lucas` normalmente. Porém, se fizermos da seguinte forma:

```JavaScript
function mostrarNome(){
    console.log(this.nome)
}
```

Não iremos obter nada além de um `undefined`, pois o this olha a referencia da function antecessora à ele, logo ele procura o this de mostrarNome, porém isso não existe.

## 11.3 VISIBILIDADE

Diferentemente de outras linguagens, o javascript não possui os atributos `private`, `public` e `protected`.

## 11.4 MÉTODOS ESPECIAIS (GETTERS, SETTERS E CONSTRUCTS)

Considerando a função de um método `getter` e `setter` que é de modificar de forma indireta os atributos privados de uma classe, eles não fazem muito sentido em JS, pois não existe isso de privado, publico e protegido. Porém, na minha cabeça de programador java/python/c++/algumas outras linguagens em que isso acontece, eu penso que faz mais sentido utilizá-los, logo eu vou criar eles aqui.

Veja o exemplo abaixo como faremos isso:

- Exemplo:

  ```JavaScript
  function Pessoa(){
      // atributos
      this.nome
      this.idade

      // setters e getters
      this.setNome = function(n){
          nome = n
      }
      this.setIdade = function(i){
          idade = i
      }
      this.getNome = function(){
          return nome
      }
      this.getIdade = function(){
          return idade
      }

      // outros métodos
      this.mostrarNome = function(){
          console.log(this.getNome())
      }
      this.mostrarIdade = function(){
          console.log(this.getIdade())
      }
  }

  pessoa = new Pessoa()
  pessoa.setNome('lucas')
  pessoa.setIdade(24)

  pessoa.mostrarNome()
  pessoa.mostrarIdade()
  ```

- Saída
  ```JavaScript
  Lucas
  24
  ```

Agora vamos ver na notação que se assemela mais à notação clássica de poo.

- Exemplo:

  ```JavaScript
  class Pessoa{
      constructor(n, i){
          this.setNome(n)
          this.setIdade(i)
      }
      // setters e getters
      setNome(n){
          this.nome = n
      }
      setIdade(i){
          this.idade = i
      }
      getNome(){
          return this.nome
      }
      getIdade(){
          return this.idade
      }

      // outros métodos
      mostrarNome(){
          console.log(this.getNome())
      }
      mostrarIdade(){
          console.log(this.getIdade())
      }
  }

  pessoa = new Pessoa('Lucas', 24)
  pessoa.mostrarNome()
  pessoa.mostrarIdade()
  ```

> OBS.: Veja que no primeiro caso o método constructor não existe explicitamente, pois ele seria a propria função, porém eu preferi não utilizá-la pois assim poderia uzar os setters, caso contrario eles estariam ali sem ser utilizados.

## 11.5 RELACIONAMENTO ENTRE CLASSES

Quando temos uma determinada classe em que algum atributo é do tipo de outra classe. Para demonstrar isso, irei utilizar a classe pessoa, que ja estamos trabalhando (porém agora retirei os setters, pois estão desnecessários devido ao nosso objetivo e pela sintax escolhida, e também deixei apenas o atributo nome, para reduzir código), e irei criar outra classe, a classe atleta, que irá receber uma pessoa, e nesse caso irei adicionar o parâmetro velocidade, supondo que para esse atleta isso seja relevante.

- Classe pessoa:

  ```JavaScript
  function Pessoa(nome){
      // getters
      this.getNome = function(){
          return nome
      }

      // outros métodos
      this.mostrarNome = function(){
          console.log(this.getNome())
      }
  }
  ```

- Classe atleta

  ```JavaScript
  function Atleta(p, velocidade){
      // Getter
      this.getVelocidade = function(){
          return velocidade
      }
      this.mostrarVelocidade = function(){
          console.log(this.getVelocidade())
      }
      this.mn = function(){
          p.mostrarNome()
      }
  }
  ```

- Chamada:

  ```JavaScript
  pessoa = new Pessoa('Lucas')
  atleta = new Atleta(pessoa, 10)
  atleta.mostrarVelocidade()
  atleta.mn()
  ```

- Saída:
  ```JavaScript
  10
  Lucas
  ```

> OBS.: Os três códigos estão em um mesmo arquivo. Se quiser ver o código completo abra [aqui](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/JavaScript/Curso%20em%20Video/C%C3%B3digos/aula16/ex013.js).

## 11.6 HERANÇA

Utilizamos o comando `prototype` para podermos extender uma classe.

- Exemplo:

  ```JavaScript
  function Pessoa(nome){
      this.getNome = function(){
          return nome
      }
      this.mostarNome = function(){
          console.log(this.getNome())
      }
  }

  function Atleta(velodade){
      this.getVelocidade = function(){
          return velodade
      }
      this.mostarVelocidade = function(){
          console.log(this.getVelocidade())
      }
  }

  Atleta.prototype = new Pessoa('Lucas') // extendendo a classe pessoa para atleta
  atleta = new Atleta(10)

  atleta.mostarNome()
  atleta.mostarVelocidade()
  ```

  - Saída:

  ```JavaScript
  Lucas
  10
  ```

> OBS.: tem como fazer isso com a utilização do `class` e `extend`, bem parecido com o java, mas tem umas coisas que não entendi direito lá, então por hora não irei abordar isso aqui. mas se quiser ir vendo sobre, veja esse video [aqui](https://www.youtube.com/watch?v=OuN2UpwRY7c)

Uma coisa que é possivel de fazer, é adicionar métodoas a uma função com o comando prototype.

```JavaScript
function ClassName(){
  // Código
}

ClassName.prototype.novo_metodo = function(parametros){
  // Código
}
```

- Exemplo:

  ```JavaScript
  function Pessoa(nome){
      this.getNome = function(){
          return nome
      }
      this.mostarNome = function(){
          console.log(this.getNome())
      }
  }

  Pessoa.prototype.mostrarIdade = function(idade){
      console.log(idade)
  }

  pessoa = new Pessoa('Lucas')
  pessoa.mostarNome()
  pessoa.mostrarIdade(24)
  ```

- Saída:
  ```JavaScript
  Lucas
  24
  ```

## 11.7 POLIMORFISMO

O polimorfismo consiste em efetuar a mesma coisa de diversas formas. Isso voltado para orientação a objeto significa que um determinada classe irá executar a sua tarefa de diferentes formas dependendo do objeto que a está usando.

Temos dois tipos principais de polimorfismo, sendo eles, o polimorfismo de sobreposição e sobrecarga. Porém aqui irei abordar apenas o de sobreposição.

### **11.7.1 Polimorfismo de sobreposição**

O polimorfismo de sobreposição acontece quando substituimos um método de uma superclasse na sua subclasse, usando a mesma assinatura. Ou seja, nos utilizamos o mesmo nome para o método e os mesmos parâmetros.

```JavaScript
function ClassePai(Parametros){
  // Código
  // método_1
}

function ClasseFilha(Parametros){
  // Código
}

ClasseFilha.prototype = new ClassePai(Parametros)
filha = new ClasseFilha(Parametros)

ClasseFilha.prototype.método_1 = function(){
  // Código sobrepondo o método_1
}

filha.método_1()
```

- Exemplo:

  ```JavaScript
  function Pessoa(valor){
      this.getValor = function(){
          return valor
      }
      this.adicionarValor = function(){
          console.log(this.getValor() + 2)
      }
  }

  Matematico = function(){}
  Fisico = function(){}

  Matematico.prototype = new Pessoa(1)
  Fisico.prototype = new Pessoa(1)
  m = new Matematico()
  f = new Fisico()

  Matematico.prototype.adicionarValor = function(){
      console.log(4 + 3)
  }

  m.adicionarValor() // modificou o método
  f.adicionarValor() // não modificou nada
  ```

- Saída:
  ```JavaScript
  7 // Saída do matemático, ou seja, a saída modificada
  3 // Saída do físico, ou seja, a saída não modificada
  ```

# 12. DELAYS

Temos dois delays no js, um seria o `setTimeout` e o outro o `setInterval`

- `setInterval`: Executa uma dada função seguidamente, mas em intervalos de tempo. Exemplo:

  - Exemplo:

    ```JavaScript
    function escreverNome(){
      conlose.log('Lucas');
    }

    setInterval(escreverNome, 1000);
    ```

  - Saída:
    ```JavaScript
    // passado 1 segundo
    Lucas
    // passado 1 segundo
    Lucas
    // isso irá se repetir até fechar o programa
    ```

- `setTimeout`: Executa a ação apenas uma vez, mas demora um dado tempo até executá-la.

  - Exemplo:

    ```JavaScript
    function escreverNome(){
      conlose.log('Lucas');
    }

    setTimeout(escreverNome, 1000);
    ```

  - Saída:
    ```JavaScript
    // passado 1 segundo
    Lucas
    ```
