# Apostila de HTML

Autor: Lucas Felipe Dutra

- [Documentação](https://devdocs.io/html/)
- [Curso](https://www.w3schools.com/html/default.asp)

# Sumário

- [1. INTRODUÇÃO](#1-introdução)
- [2. HTML](#2-html)
  - [2.1 LANG](#21-lang)
- [3. HEAD](#3-head)
  - [3.1 META](#31-meta)
    - [3.1.1 Charset](#311-charset)
    - [3.1.2 Descrição](#312-descrição)
    - [3.1.3 Palavras chave](#313-palavras-chave)
    - [3.1.4 Autor](#314-autor)
    - [3.1.4 Refresh automático](#314-refresh-automático)
    - [3.1.5 Auto ajuste da página](#315-auto-ajuste-da-página)
  - [3.2 TITLE](#32-title)
- [4. BODY](#4-body)
- [5. TITULOS](#5-titulos)
- [6. PARÁGRAFOS](#6-parágrafos)
- [7. HIPERLINK](#7-hiperlink)
  - [7.1 HIPERLINK COM TITULOS](#71-hiperlink-com-titulos)
- [8. IMAGENS](#8-imagens)
  - [8.1 IMAGEM COMO HIPERLINK](#81-imagem-como-hiperlink)
  - [8.2 IMAGEM FLUTUANDO](#82-imagem-flutuando)
  - [8.3 MAPEAR IMAGEM](#83-mapear-imagem)
- [9. BOTÕES](#9-botões)
- [10. LISTAS](#10-listas)
  - [10.1 LISTA HOIZONTAL](#101-lista-hoizontal)
- [11. FORMATAÇÃO DE TEXTO](#11-formatação-de-texto)
  - [11.1 TEXTO EM NEGRITO](#111-texto-em-negrito)
  - [11.2 TEXTO EM ITÁLICO](#112-texto-em-itálico)
  - [11.3 TEXTO SUBLINHADO](#113-texto-sublinhado)
  - [11.4 TEXTO SUBSCRITO](#114-texto-subscrito)
  - [11.5 TEXTO SOBRESCRITO](#115-texto-sobrescrito)
  - [11.6 TEXTO COM FONTE MAIOR DO QUE O PADRÃO](#116-texto-com-fonte-maior-do-que-o-padrão)
  - [11.7 TEXTO COM FONTE MENOR DO QUE O PADRÃO](#117-texto-com-fonte-menor-do-que-o-padrão)
  - [11.8 PULAR UMA LINHA](#118-pular-uma-linha)
  - [11.9 CRIAR LINHA HORIZONTAL](#119-criar-linha-horizontal)
  - [11.10 TEXTO COM MARCA](#1110-texto-com-marca)
  - [11.11 RISCAR UM TEXTO](#1111-riscar-um-texto)
  - [11.12 ABREVIAR TEXTO](#1112-abreviar-texto)
- [12. TABELAS](#12-tabelas)
- [13. ESTILOS](#13-estilos)
  - [13.1 INLINE](#131-inline)
  - [13.2 INTERNAL](#132-internal)
  - [13.3 EXTERNAL](#133-external)
    - [13.3.1 O arquivo CSS](#1331-o-arquivo-css)
    - [13.3.2 O arquivo html](#1332-o-arquivo-html)
- [14. A TAG DIV](#14-a-tag-div)
- [15. CLASSES](#15-classes)
- [16. IFRAME](#16-iframe)
  - [16.1 UTILIZAR IFRAME COMO ALVO DE UM LINK](#161-utilizar-iframe-como-alvo-de-um-link)

# 1. INTRODUÇÃO

A linguagem HTML é composta de tags, que são comandos para que o browser interprete como queremos que a página seja mostrada.

Toda tag HTML segue uma estrutura padrão, que é:

```HTML
<nome_da_tag atributo=""> conteúdo </nome_da_tag>
```

A estrutura básica de um código HTML está dividida em três partes.

- O escopo geral que se inicia com a tag `<html>`. Nela podemos indicar a linguagem da página.
- `<head>` que contém o titulo da página, e a indicação da tabela de caracteres que devemos utilizar.
- `<body>` que contém toda a construção textual da página, sendo essa a parte que efetivamente aparecerá na tela do browser.

Veja um exemplo de um código HTML para apresentar essas três regiões:

```HTML
<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <meta charset="utf-8">
    <title>Primeira página html</title>
  </head>
  <body>
    Textos..
  </body>
</html>
```

- Atributos:
  - **alt:** Especifica um texto alternativa para uma imagem, quando não é possível mostrar a imagem
  - **disabled:** Especifica que um elemento de entrada deve ser desativado.
  - **href:** Especifica um URL para um link.
  - **id:** Especifica um ID único para um elemento.
  - **src:** Especifica um URL para uma imagem.
  - **style:** Especifica um estilo CSS para um elemento.
  - **title:** Especifica um titulo para um elemento.

Agora vamos olhar todas as tags que podemos utilizar no html.

# 2. HTML

## 2.1 LANG

`lang` é o indicador de qual linguagem a página utilizará.

- Portugues brasil: pt-br
- Inglês: en
- Qualquer outra linguagem e sua respectiva abraviação você encontrará [aqui](https://www.w3schools.com/tags/ref_language_codes.asp).

# 3. HEAD

Dentro de head vamos definir `meta charset` e `title`

## 3.1 META

A tag `<meta>` é utilizada para descrever qual tabela de caracteres vamos utilizar, para colocarmos uma descrição do site, palavras chave, autor da pagina, e mandar a pagina dar refresh automático, em resumo, aqui é onde estão os metadados da página.

### 3.1.1 Charset

Essa tag tem como função definir qual será a tabela de caracteres que utilizaremos. No caso vamos escolher `utf-8`, que possui os caracteres de acentuação e cidilha, típicos da lingua portuguesa.

- Estrutura

```HTML
<head>
    <meta charset="utf-8">
</head>
```

### 3.1.2 Descrição

- Estrutura

```HTML
<head>
    <meta name="description" content="Descrição da sua página">
</head>
```

### 3.1.3 Palavras chave

- Estrutura

```HTML
<head>
    <meta name="keywords" content="HTML, CSS, JAVASCRIPT, TODAS AS COISAS QUE QUISER">
</head>
```

### 3.1.4 Autor

- Estrutura

```HTML
<head>
    <meta name="author" content="Lucas Felipe Dutra">
</head>
```

### 3.1.4 Refresh automático

- Estrutura

```HTML
<head>
    <meta http-equiv="refresh" content="tempo em segundos">
</head>
```

### 3.1.5 Auto ajuste da página

Para fazer a pagina se ajustar ao seu dispositivo (pc, celular, tablete), basta utilizar os atributos abaixo.

- Estrutura

```HTML
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
```

## 3.2 TITLE

Como o próprio nome já diz, aqui iremos descrever o titulo da página, ou seja, aquele nome que aparece na aba do navegador.

- Exemplo

```HTML
<!DOCTYPE html>
<html lang="pt-br"> <!-- Aqui eu abri a tag html, preciso fechá-la depois -->
<head>
  <meta charset="utf-8">
  <title>Titulo da página</title>
</head>
```

# 4. BODY

Aqui definiremos o corpo da nossa página. Dentro dessa tag podemos colocar basicamente todas as outras tags que virão a seguir.

- Exemplo

```HTML
<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <meta charset="utf-8">
    <title>Apostila de HTML</title>
  </head>
  <body>
    Olá mundo
  </body>
</html>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_01.png?raw=true)

# 5. TITULOS

Para definir titulos utiliza-se a tag `<h_numero_do_titulo>` sendo que o número do titulo vai de 1 a 5.

- Exemplo e estrutura

```HTML
<body>
    <h1>TITULO 1</h1>
    <h2>TITULO 2</h2>
    <h3>Titulo 3</h3>
    <h4>Titulo 4</h4>
    <h5>Titulo 5</h5>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_02.png?raw=true)

# 6. PARÁGRAFOS

A tag de criação de parágrafo é: `<p>`

- Estrutura

```HTML
<body>
    <p>Digite seu texto</p>
</body>
```

- Exemplo

```HTML
<body>
    <p>Parágrafo 1</p>
    <p>Parágrafo 2</p>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_03.png?raw=true)

# 7. HIPERLINK

Para adicionar um link utilize a tag `<a>`.

- Estrutura:

```HTML
<body>
    <a href="cole o link aqui" title="titulo do link">digite o texto de hiperlink</a>
</body>
```

> OBS.: O titulo do link irá aparecer quando passar o mouse sobre o hiperlink, mas esse atributo é totalmente opicional.

- Exemplo

```HTML
<body>
    <a href="https://devdocs.io/html/" title="Veja a documentação da linguagem HTML">Documentação do HTML</a>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_04.png?raw=true)

## 7.1 HIPERLINK COM TITULOS

É possível linkar um titulo da página utilizando hiperlink. Para isso faça da seguinte forma:

- Estrutura

```HTML
<body>
    <a href="#id-do-titulo">Vá para o titulo</a>
    <h1 id="id do titulo">Titulo</h1>
</body>
```

- Exemplo

```HTML
<body>
    <a href="#T1">Vá para o titulo 1</a>
    <h1 id="T1">Titulo 1</h1>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_05.png?raw=true)

# 8. IMAGENS

Para adicionar uma imagem utilize a tag `<img src="">`

- Estrutura

```HTML
<body>
    <img src="endereço" width="largura" height="altura" title="Titulo da imagem">
</body>
```

> OBS.: O titulo aparecerá quando passar o mouse sobre a imagem.

- Exemplo

```HTML
<body>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/800px-HTML5_logo_and_wordmark.svg.png" alt="Texto" width='300' title="Logo do HTML 5">
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_06.gif?raw=true)

## 8.1 IMAGEM COMO HIPERLINK

Para utilizar uma imagem como um hiperlink basta inserir a imagem entre a tag `<a>`.

- Estrutura:

```HTML
<body>
    <a href="cole o link aqui">
        <img src="endereço" width="largura" height="altura" title="Titulo da imagem">
    </a>
</body>
```

- Exemplo

```HTML
<body>
    <a href="https://devdocs.io/html/">
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/800px-HTML5_logo_and_wordmark.svg.png" alt="Documentação do HTML" width="300" title="Veja a documentação da linguagem HTML">
    </a>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_07.gif?raw=true)

## 8.2 IMAGEM FLUTUANDO

É meio difícil descrever o que é isso, mas vendo um exemplo fica fácil de entender.

- Estrutura

```HTML
<body>
    <p><img src="endereço da imagem" style='float: posição'>Texto do parágrafo</p>
</body>
```

- Exemplo

```HTML
<body>
    <p><img src="https://image.flaticon.com/icons/svg/919/919852.svg" style="float: left; width: 42px; height: 42px">Sabe o que é interessante de aprender?</p>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_08.png?raw=true)

## 8.3 MAPEAR IMAGEM

Podemos dividir os pixels de uma imagem e fazer com que cada parte dela seja um hiperlink.

- Estrutura

```HTML
<body>
    <img src="endereço da imagem" usemap="#nome do mapa">
    <map name="nome do mapa">
        <area shape="formato (rect, circle)" coords="x0,y0,xf,yf" href="endereço de redirecionamento" alt="texto para caso a imagem suma">
        <area shape="formato (rect, circle)" coords="x0,y0,xf,yf" href="endereço de redirecionamento" alt="texto para caso a imagem suma">
        <area shape="formato (rect, circle)" coords="x0,y0,xf,yf" href="endereço de redirecionamento" alt="texto para caso a imagem suma">
    </map>
</body>
```

- Exemplo

```HTML
<body>
    <img src="https://cdn-images-1.medium.com/max/1600/1*lJ32Bl-lHWmNMUSiSq17gQ.png" usemap="#map_html_css" width="300">
    <map name="map_html_css">
        <area shape="rect" coords="0,0,150,300" href="https://en.wikipedia.org/wiki/HTML" title="HTML na wikipedia">
        <area shape="rect" coords="151,0,300,300" href="https://en.wikipedia.org/wiki/Cascading_Style_Sheets" title="CSS na wikipedia">
    </map>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_09.gif?raw=true)

# 9. BOTÕES

Para adicionar um botão a tela utlize a tag `<button>`

- Estrutura

```HTML
<body>
    <button>Texto do botão</button>
</body>
```

- Exemplo

```HTML
<body>
    <button>Clik aqui</button>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_10.png?raw=true)

# 10. LISTAS

Podemos criar listas ordenadas (tópico 1, tópico 2,...) ou listas desordenadas (utilizando apenas ponto).

- Para ordenadas: `<ol>`
  - Existem tipos de ordenação.
    - type="1": listagem por números (default).
    - type="A": listagem por letras maiúsculas.
    - type="a": listagem por letras minúsculas.
    - type="I": listagem por algoritmos romanos maiúsculos.
    - type="i": listagem por algoritmos romanos minúsculos.
- Para desordenadas: `<ul>`
- Para adicionar os tópicos: `<li>`

- Estrutura e exemplo

```HTML
<body>
    <!-- Lista ordenada -->
    <ol>
      <li>Tópico 1</li>
      <li>Tópico 2</li>
    </ol>
    <br>
    <!-- Lista ordenada por algoritmos romanos -->
    <ol type="I">
      <li>Tópico 1</li>
      <li>Tópico 2</li>
    </ol>
    <br>
    <!-- Lista desordenada -->
    <ul>
      <li>Tópico 1</li>
      <li>Tópico 2</li>
    </ul>
    <br>
    <!-- Lista com sub-itens-->
    <ul>
      <li>Tópico 1</li>
      <ul>
        <li>Tópico 1.1</li>
      </ul>
      <li>Tópico 2</li>
    </ul>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_11.png?raw=true)

## 10.1 LISTA HOIZONTAL

Para criar uma lista horizontal é necessário utilizar estilos em css, então de uma olhada na seção 13 em que é aborado os estilos, e depois volte aqui.

- Exemplo

```HTML
<head>
    <style>
        ul {
          list-style-type: none;
          margin: 0;
          padding: 0;
          overflow: hidden;
          background-color: #333333;
        }

        li {
          float: left;
        }

        li a {
          display: block;
          color: white;
          text-align: center;
          padding: 16px;
          text-decoration: none;
        }

        li a:hover {
          background-color: #111111;
        }
    </style>
</head>
<body>
  <ul>
      <li><a href="#home">Home</a></li>
      <li><a href="#news">News</a></li>
      <li><a href="#contact">Contact</a></li>
      <li><a href="#about">About</a></li>
  </ul>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_12.png?raw=true)

# 11. FORMATAÇÃO DE TEXTO

## 11.1 TEXTO EM NEGRITO

- Uma das tags de texto em negrito é: `<b>`
- A outra tag de texto em negrito é: `<strong>`

- Estrutura e exemplo

```HTML
<body>
    <b>Texto em negrito</b><br>
    <strong>Texto em negrito</strong><br>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_13.png?raw=true)

## 11.2 TEXTO EM ITÁLICO

- Uma das tags de texto em itálico é: `<i>`
- A outra tag de texto em itálico é: `<em>`

- Estrutura e exemplo

```HTML
<body>
    <i>Texto em itálico</i><br>
    <em>Texto em itálico</em><br>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_14.png?raw=true)

## 11.3 TEXTO SUBLINHADO

- A tag de texto sublinhado é: `<u>`

- Estrutura e exemplo

```HTML
<body>
    <u>Texto sublinhado</u>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_15.png?raw=true)

## 11.4 TEXTO SUBSCRITO

- A tag de texto subscrito é: `<sub>`

- Estrutura e exemplo

```HTML
<body>
    <sub>Texto subscrito</sub><br>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_16.png?raw=true)

## 11.5 TEXTO SOBRESCRITO

- A tag de Texto sobrescrito é: `<sup>`

- Estrutura e exemplo

```HTML
<body>
    <sup>Texto sobrescrito</sup><br>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_17.png?raw=true)

## 11.6 TEXTO COM FONTE MAIOR DO QUE O PADRÃO

- A tag de Texto com fonte maior do que o padrão é: `<big>`

- Estrutura e exemplo

```HTML
<body>
    <big>Texto com fonte maior do que o padrão</big><br>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_18.png?raw=true)

## 11.7 TEXTO COM FONTE MENOR DO QUE O PADRÃO

- A tag de Texto com fonte menor do que o padrão é: `<small>`

- Estrutura e exemplo

```HTML
<body>
    <small>Texto com fonte menor do que o padrão</small>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_19.png?raw=true)

## 11.8 PULAR UMA LINHA

- Para pular uma linha utilize `<br>` no final da linha.

- Estrutura

```HTML
<body>
    <alguma_tag>Algum texto </alguma_tag><br>
</body>
```

- Exemplo

```HTML
<body>
    Texto linha 1 <br>
    Texto linha 2
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_20.png?raw=true)

## 11.9 CRIAR LINHA HORIZONTAL

- Para criar uma linha horizontal entre duas linhas, podemos utilizar a tag `<hr>`.

- Estrutura e exemplo

```HTML
<body>
    <hr>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_21.png?raw=true)

## 11.10 TEXTO COM MARCA

Podemos marcar desde uma única palavra dentro de uma frase, até mesmo uma frase inteira. Basta colocar o texto em questão entre a tag `<mark>`.

- Estrutura

```HTML
<nome_da_tag> Inicio do texto <mark> Texto a ser marcado </mark> Parte final do texto</nome_da_tag>
```

- Exemplo

```HTML
<body>
    <p>Aqui o texto não será marcado, <mark> mas aqui ele será </mark>, e aqui ele voltará ao normal.</p>
    <p><mark>Já esse parágrafo será todo marcado.</mark></p>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_22.png?raw=true)

## 11.11 RISCAR UM TEXTO

Podemos riscar uma palavra, ou até mesmo um texto todo, basta essa região estar dentro da tag `<del>`.

- Estrutura

```HTML
<nome_da_tag> Inicio do texto <del> Texto a ser riscado </del> Parte final do texto</nome_da_tag>
```

- Exemplo

```HTML
<body>
    <p>Aqui o texto não será riscado, <del> mas aqui ele será </del>, e aqui ele voltará ao normal.</p>
    <p><del>Já esse parágrafo será todo riscado.</del></p>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_23.png?raw=true)

## 11.12 ABREVIAR TEXTO

Se quiser abreviar um texto para uma sigla, porém quando passar o mouse em cima da sigla apareça o texto completo, utilize a tag `<abbr>`.

- Estrutura

```HTML
<body>
    <nome_da_tag> Inicio do texto <abbr title="Texto completo">abreviação</abbr> Retomando o texto.</nome_da_tag>
</body>
```

- Exemplo

```HTML
<body>
    <p>Os algoritmos de <abbr title="Machine learning">ML</abbr> gastam muito poder computacional.</p>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_24.gif?raw=true)

# 12. TABELAS

Para a criação de tabelas utiliza-se a tag `<table>`. Sendo que:

- Cada linha deve ser criada com a tag `<tr>`.
- Cada célula deve ser criada com a tag `<td>`.
- O cabeçalho é opcional, mas ele é declarado com a tag `<th>`
- De modo opcional, o atributo `colspan` faz a mescla entre celulas de colunas diferentes.
- De modo opcional, o atributo `rowspan` faz a mescla entre celulas de linhas diferentes.

|        | `<th>` | `<th>` |
| ------ | ------ | ------ |
| `<tr>` | `<td>` | `<td>` |
| `<tr>` | `<td>` | `<td>` |

- Estrutura e exemplo

```HTML
<body>
    <table>
      <tr> <!-- cabeçalho -->
        <th>Coluna 1</th>
        <th>Coluna 2</th>
        <th>Coluna 3</th>
      </tr>
      <tr> <!--Linha 1 -->
        <td>Célula linha 1 coluna 1</td>
        <td>Célula linha 1 coluna 2</td>
        <td>Célula linha 1 coluna 3</td>
      </tr>
      <tr> <!--Linha 2 -->
        <td>Célula linha 2 coluna 1</td>
        <td>Célula linha 2 coluna 2</td>
        <td>Célula linha 2 coluna 3</td>
      </tr>
      <tr> <!--linha com mescla -->
        <td rowspan="2">Célula da primeira coluna</th>
        <td colspan="2">Primeria célula da segunda coluna</td>
      </tr>
      <tr>
        <td colspan="2">Segunda célula da segunda coluna</td>
      </tr>
    </table>
</body>
```

- Saída <br>
  <body>
      <table>
        <tr> <!-- cabeçalho -->
          <th>Coluna 1</th>
          <th>Coluna 2</th>
          <th>Coluna 3</th>
        </tr>
        <tr> <!--Linha 1 -->
          <td>Célula linha 1 coluna 1</td>
          <td>Célula linha 1 coluna 2</td>
          <td>Célula linha 1 coluna 3</td>
        </tr>
        <tr> <!--Linha 2 -->
          <td>Célula linha 2 coluna 1</td>
          <td>Célula linha 2 coluna 2</td>
          <td>Célula linha 2 coluna 3</td>
        </tr>
        <tr> <!--linha com mescla -->
          <td rowspan="2">Célula da primeira coluna</th>
          <td colspan="2">Primeria célula da segunda coluna</td>
        </tr>
        <tr>
          <td colspan="2">Segunda célula da segunda coluna</td>
        </tr>
      </table>
  </body>

> OBS.: Utilize comandos CSS para brincar com a sua tabela. Um comando útil, é alterar as propriedades da borda, com a tag `border`.

# 13. ESTILOS

Um estilo é um atributo que pode modificar coisas como a cor do fundo ou a cor da fonte que estamos utilizando. Para criar um estilo utiliza-se a linguagem CSS, e com ela podemos modificar as seguintes propriedades:

- Propriedades
  - Cor de fundo: background-color
  - Cor do texto: color
    - blue;
    - red;
    - rgba: (vermelho, verde, azul, transparência)
      - Vermelho: Varia de 0 a 255;
      - Verde: Varia de 0 a 255;
      - Azul: Varia de 0 a 255;
      - Transparência: Varia de 0 a 1, sendo que em 1 não existe transparência.
    - #valor em hexadecimal;
      - O valor segue a seguinte lógica: #rrggbb;
        - Ou seja, os dois primeiros valores são relativos ao red, os dois do meio ao green, e os dois do final ao blue;
          - Lembrando que hexadecimais seguem a sequência: 0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f. Sendo o f o mais forte.
      - background-color: #ff6347 -> equivalente à cor 'Tomato';
    - etc..
  - Fonte: font-family
    - verdana;
    - arial;
    - courier;
    - etc..
  - Tamanho do texto: font-size
    - Dado em porcentagem.
  - Alinhamento do texto: text-align
    - center;
    - up;
    - down;
    - left;
    - right;

O código CSS pode ser utilizado de três formas:

- Inline: Utilizando o atributo `<style>` em uma tag html.
- Internal: Utiliza a tag `<style>` dentro de `<head>` e define os estilos lá.
- External: Utiliza um arquivo CSS com todos os estilos.

## 13.1 INLINE

- Estrutura

```HTML
<body>
    <nome_da_tag style="Propriedade: valor;">Texto</nome_da_tag>
</body>
```

- Exemplos

```HTML
<body style="background-color: green;">
    <h1 style="color: red;">Titulo 1 escrito em vermelho</h1>
    <p style="font-family: verdana;">Parágrafo escrito com fonte verdana</p>
    <p style="font-size: 300%;">Parágrafo escrito com fonte de tamanho grande: 300%</p>
    <p style="text-align: right">Parágrafo com texto alinhado a direita</p>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_25.png?raw=true)

## 13.2 INTERNAL

- Estrutura

```HTML
<head>
    <style>
      nome_da_tag {Propriedade: valor;}
    </style>
</head>
<body>
    <nome_da_tag>O texto estará com sua respectiva formatação</nome_da_tag>
</body>
```

- Exemplo

```HTML
<head>
    <style>
      body{background-color: green;}
      h1{color: red;}
      p{font-family: cursive;}
    </style>
</head>
<body>
    <h1>Titulo em vermelho</h1>
    <p>Primeiro parágrafo com a fonte cursive</p>
    <p>Segundo parágrafo com a fonte cursive</p>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_26.png?raw=true)

## 13.3 EXTERNAL

### 13.3.1 O arquivo CSS

- Estrutura

```CSS
nome_da_tag_html{Propriedade: valor}
```

- Exemplo

```CSS
body{background-color: green;}
h1{color: red;}
p{font-family: cursive;}
```

### 13.3.2 O arquivo html

- Estrutura

```HTML
<head>
    <link rel="stylesheet" href="arquivo_CSS.css">
</head>
```

- Exemplo

```HTML
<head>
    <link rel="stylesheet" href="arquivo_CSS.css">
</head>
<body>
    <h1>Titulo em vermelho</h1>
    <p>Primeiro parágrafo com a fonte cursive</p>
    <p>Segundo parágrafo com a fonte cursive</p>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_27.png?raw=true)

# 14. A TAG DIV

Em tudo quanto é página a tag div será encontrada. Ela serve para criar blocos, assim os textos podem ser melhor divididos.

- Exemplo

```HTML
<body>
    <div>
        <h1>Titulo 1</h1>
        <p>Texto no parágrafo</p>
    </div>
    <div>
        <p>Texto no parágrafo da segunda divisão</p>
    </div>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_28.png?raw=true)

# 15. CLASSES

Quando vimos estilos, nota-se que se tivessemos um estilo para parágrafo, teriamos o mesmo estilo para todos os parágrafos. Porém, com classes podemos seguimentar isso, pois os estilos serão aplicados as classes e não as tags.

- Exemplo

```HTML
<head>
  <!--Primeiro definirei um estilo para qualquer tag que tiver como classe a classe_1 -->
  <!--Depois definirei um estilo para parágrafos pertencentes a classe_2-->
    <style>
        .classe_1{
          color: green;
        }
        p.classe_2{
          color: red;
        }
    </style>
</head>
<body>
    <div class="classe_1">
        <p>Texto em verde</p>
    </div>
    <div>
        <p class="classe_2">Texto em vermelho</p>
    </div>
    <p class="classe_1">Texto em verde</p>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_29.png?raw=true)

> OBS.: A mesma ideia pode ser aplicada ao atributo `id`. Porém, uma classe pode ser aplicada para vários elementos, já o id não, ele sempre único.

# 16. IFRAME

Aqui podemos colocar janelas no site. Isso é possível com o uso da tag `<iframe>`.

- Estrutura

```HTML
<body>
    <iframe coloque aqui qualquer atributo que deseja>
        Aqui dentro pode ter qualquer coisa
    </iframe>
</body>
```

- Exemplo

```HTML
<body>
    <iframe src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/800px-HTML5_logo_and_wordmark.svg.png" width="200" height="200" style="board:none;"></iframe>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_30.png?raw=true)

## 16.1 UTILIZAR IFRAME COMO ALVO DE UM LINK

Se quisermos podemos colocar uma página da web dentro do nosso frame. Para isso, utilizamos o atributo `target`.

- Estrutura

```HTML
<body>
    <iframe name="nome_do_frame" demais configurações do frame></iframe>
    <a href="link" target="nome_do_frame">texto do link</a>
</body>
```

- Exemplo

```HTML
<body>
    <iframe name="frame_1" width="100%"></iframe>
    <p><a href="https://devdocs.io/html/" target="frame_1">Documentação do HTML</a></p>
</body>
```

- Saída <br>
  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/HTML/Imagens/Figura_31.gif?raw=true)
