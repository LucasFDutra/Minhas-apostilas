# Apostila de CSS

Autores: Lucas Felipe Dutra e Uilen Helei Leles Moreira

- [Documentação](https://devdocs.io/css/)
- [Referencias CSS](https://cssreference.io/)
- [Referencias CSS - Mozilla](https://developer.mozilla.org/pt-BR/docs/Web/CSS/CSS_Reference)
- [MDN web docs](https://developer.mozilla.org/pt-BR/docs/Web/CSS)
- [W3Schools](https://www.w3schools.com/cssref/)

# Dica

De uma olhada [aqui](https://www.hostinger.com.br/tutoriais/o-que-e-css-guia-basico-de-css/) para ver o que é um css.

E como sugestão de onde escrever seus códigos e praticar eu recomendo duas ferramentas. Primeiro o VScode, que é um editor de texto e você provavelmente acabará utilizando ele quando for fazer projetos web. Mas se for só para praticar rapidamente seu css, html ou JavaScript, eu recomendo um site chamado [codepen](https://codepen.io), nele você coloca seus códigos e já tem o resultado da implementação logo abaixo, é muito bom para treinar e ver como seus estilos se comportão.

# Sumário

- [**1. ESTRUTURA**](#1-estrutura)
- [**2. COMO UTILIZAR**](#2-como-utilizar)
  - [2.1 INLINE](#21-inline)
  - [2.2 INTERNAL](#22-internal)
  - [2.3 EXTERNAL](#23-external)
    - [2.3.1 O arquivo CSS](#231-o-arquivo-css)
    - [2.3.2 O arquivo html](#232-o-arquivo-html)
- [**3. SELETOR**](#3-seletor)
  - [3.1 AGRUPAMENTO DE SELETORES](#31-agrupamento-de-seletores)
  - [3.2 SELETOR POR CLASSE](#32-seletor-por-classe)
  - [3.3 SELETORES POR ID](#33-seletores-por-id)
- [**4. PROPRIEDADES**](#4-propriedades)
  - [4.1 DIMENSÃO DO OBJETO](#41-dimensão-do-objeto)
  - [4.2 ESPAÇAMENTO INTERNO](#42-espaçamento-interno)
  - [4.3 MARGEM](#43-margem)
  - [4.4 TEXTO](#44-texto)
  - [4.5 BOX](#45-box)
  - [4.6 BORDAS](#46-bordas)
  - [4.7 FONTES](#47-fontes)
    - [**4.7.1 Obter fonte externa**](#471-obter-fonte-externa)
  - [4.8 COMPORTAMENTO](#48-comportamento)
- [**5. PLANO DE FUNDO**](#5-plano-de-fundo)
- [**6. TRANSITION**](#6-transition)
- [**7. VARIÁVEIS**](#7-variáveis)
- [**8. NORMALIZE OU RESET**](#8-normalize-ou-reset)
- [**9. CÁLCULO**](#9-cálculo)
- [**10. FILTROS**](#10-filtros)

# **1. ESTRUTURA**

Um código css é constituido da seguinte forma:

```CSS
tag_html_1 {
	configurações;
}
tag_html_2 {
	configurações;
}
```

# **2. COMO UTILIZAR**

O código CSS pode ser utilizado de três formas:

- Inline: Utilizando o atributo `style` em uma tag html.
- Internal: Utiliza a tag `<style>` dentro de `<head>` e define os estilos lá.
- External: Utiliza um arquivo CSS com todos os estilos.

## 2.1 INLINE

- Estrutura

  ```HTML
  <body>
      <nome_da_tag style="Propriedade_1: valor; Propriedade_2: valor">Texto</nome_da_tag>
  </body>
  ```

- Exemplos

  ```HTML
  <p style='color: red; text-align: center; font-size: 50pt'>Estilização com css inline</p>
  ```

- Saída:

  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/CSS/Imagens/Figura_01.png?raw=true)

## 2.2 INTERNAL

- Estrutura

  ```HTML
  <head>
      <style>
        nome_da_tag {
          Propriedade_1: valor;
          Propriedade_2: valor
        }
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
      h1{color: red;}
      p{font-family: cursive;}
      </style>
  </head>
  <body>
      <h1>Titulo em vermelho</h1>
      <p>Primeiro parágrafo com a fonte cursive</p>
  </body>
  ```

- Saída:

  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/CSS/Imagens/Figura_02.png?raw=true)

## 2.3 EXTERNAL

### 2.3.1 O arquivo CSS

- Estrutura

  ```CSS
  nome_da_tag_html{
      Propriedade_1: valor;
      Propriedade_2: valor
  }
  ```

- Exemplo: Vou chamar esse arquivo de `estilos.css`

  ```CSS
  h1{
    color: red;
  }

  p{
    font-family: cursive;
  }
  ```

### 2.3.2 O arquivo html

- Estrutura

  ```HTML
  <head>
      <link rel="stylesheet" href="arquivo_CSS.css">
  </head>
  ```

- Exemplo: Vou chamar esse arquivo de `index.html`

  ```HTML
  <head>
  <link rel="stylesheet" href="estilos.css">
  </head>
  <body>
      <h1>Titulo em vermelho</h1>
      <p>Primeiro parágrafo com a fonte cursive</p>
  </body>
  ```

- Saída:

  ![](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/blob/master/CSS/Imagens/Figura_03.png?raw=true)

> OBS: Todos os exemplos agora serão modificações que farei nesses dois arquivos, então não ficarei mais colocando os nomes deles.

# **3. SELETOR**

Tudo o que está entre `{}` pode ser chamado de seletor.

## 3.1 AGRUPAMENTO DE SELETORES

E como você bem pode ter pensado, se diversos itens da nossa página tiverem a mesma estilização, então é bem viável que façamos o agrupamento desses seletores. E é bem simples fazer isso, basta colocar:

```CSS
tag_1, tag_2 {
    Propriedade: valor
}
```

- Exemplo:
  ```CSS
  h1, h2, p{
      color: black
  }
  ```

## 3.2 SELETOR POR CLASSE

Como você também pode ter imaginado, não é muito viável estilizar as coisas colocando como referencia as tags html, pois se você quiser que dois parágrafos `<p>` tenham estilos diferentes seria impossível, mas se nos utilizarmos a estilização por classes ou pelo id de um componente html.

Para as classes vamos utilizar duas possíveis notações:

- `.nomeDaClasse {Propriedade: valor}`
- `nomeDaTag.nomeDaClasse {Propriedade: valor}`

- Exemplo:
  ```CSS
  .titulo1{
      color: black
  }
  h1.titulo2{
      color: green
  }
  ```

Lembrando que vários componentes html podem pertencer a mesma classe.

## 3.3 SELETORES POR ID

Diferente da classe, o id é único para cada componente html. No css para fazer a identificação de uma classe utilizamos o `.`, já para um id utilizamos o `#`. E assim como na classe temos aqui duas notações:

- `#id {Propriedade: valor}`
- `nomeDaTag#id {Propriedade: valor}`

- Exemplo:
  ```CSS
  #titulo1{
      color: black
  }
  h1#titulo2{
      color: green
  }
  ```

# **4. PROPRIEDADES**

Agora vamos ver algumas das propriedades que podemos tratar com um css, mas claro que não trarei todas aqui, porém é possivel ver todas as propriedades olhando nas referencias do css ou na documentação, e ambas estão nos links deixados no inicio desse material

Para os exemplos posteriores, veja sempre esse corpo html (em caso de modificações para melhorar os exemplos, irei colocar o novo corpo)

```HTML
<body>
  <div class="container">
    <p id="paragrafo">Texto</p>
  </div>
</body>
```

## 4.1 DIMENSÃO DO OBJETO

- [**width**](https://developer.mozilla.org/pt-BR/docs/Web/CSS/width): Largura, pode ser dada em pixel ou em porcentagem

  - **max-width**: estipula a largura máxima
  - **min-width**: estipula a largura minima

- [**height**](https://developer.mozilla.org/pt-BR/docs/Web/CSS/height): Altura, pode ser dada em pixel ou em porcentagem

  - **max-height**: Altura máxima
  - **min-height**: Altura minima

- Exemplo:

  ```CSS
  .container {
    <!-- colocando em pixels -->
    width: 500px;
    <!-- colocando em porcentagem -->
    height: 20%;
  }
  ```

## [4.2 ESPAÇAMENTO INTERNO](https://developer.mozilla.org/pt-BR/docs/Web/CSS/padding)

- **padding**: Estabelece um espaçamento para todas as direções.
- **padding-top**: Espaçamento superior
- **padding-right**: Espaçamento a direita
- **padding-bottom**: Espaçamento a baixo
- **padding-left**: Espaçamento a esquerda

- Exemplo 1:

  ```CSS
  #paragrafo {
    padding: 10px;
  }
  ```

- Exemplo 2:

  ```CSS
  #paragrafo {
    padding-top: 5px;
    padding-bottom: 5px;
    padding-left: 10px;
    padding-right: 10px;
  }
  ```

## [4.3 MARGEM](https://developer.mozilla.org/pt-BR/docs/Web/CSS/margin)

**margin**: Estabelece um espaçamento para todas as direções.

- **margin-top**: Espaçamento superior
- **margin-right**: Espaçamento a direita
- **margin-bottom**: Espaçamento a baixo
- **margin-left**: Espaçamento a esquerda

## 4.4 TEXTO

- [color](https://developer.mozilla.org/pt-BR/docs/Web/CSS/color): alteração da cor, em hexadecimal, rgb, rgba e etc

- currentColor: Funciona como uma variável que armazena o valor de uma cor que esta sendo usada no campo das propriedades.

- [text-align](https://developer.mozilla.org/pt-BR/docs/Web/CSS/text-align): alinhamento do texto, pode ser do tipo justify, right, left e center

- [text-decoration](https://developer.mozilla.org/pt-BR/docs/Web/CSS/text-decoration): fazer algum tipo de decoração no texto, como por exemplo um underline, overline, line-through

- [text-transform](https://developer.mozilla.org/pt-BR/docs/Web/CSS/text-transform): transformação do texto, por exemplo a uppercase (letras maiúsculas), lowercase (letras minúsculas), capitilize (primeira letra em maiúscula de cada palavra)

- [text-indent](https://developer.mozilla.org/pt-BR/docs/Web/CSS/text-indent): Criar um recuo na primeira linha dada em pixels

- [line-height](https://developer.mozilla.org/pt-BR/docs/Web/CSS/line-height): Espaçamento das linhas, dadas em pixels

- [direction](https://developer.mozilla.org/pt-BR/docs/Web/CSS/direction): Direção do texto, pode ser rtl (right to left), ltr (left to right)

- [letter-spacing](https://developer.mozilla.org/pt-BR/docs/Web/CSS/letter-spacing): Espaçamento entre as letras dada em pixels, aceita valores positivos e negativos

- [word-spacing](https://developer.mozilla.org/pt-BR/docs/Web/CSS/word-spacing): Espaçamento entre as palavras dada em pixels, aceita valores positivos e negaticos

- [text-shadow](https://developer.mozilla.org/pt-BR/docs/Web/CSS/text-shadow): Adicionar uma sombra ao texto
  - Deslocamento Horizontal
  - Deslocamento Vertical
  - Desfoque
  - Cor da sombra

## 4.5 BOX

- [box-sizing](https://developer.mozilla.org/pt-BR/docs/Web/CSS/box-sizing): Configura o tamanho do conjunto de uma div com um determinado comprimento e um padding, pois quando adiciona o padding, ele acrescenta ao valor do comprimento, o que dependendo da aplicação é indesejado, e por este motivo utiliza-se o `box-sizing: border-box` para garantir que o comprimento da div se mantenha inalterado e ainda sim se tenha o padding, geralmente utiliza-se no seleter universal

- [box-shadow](https://developer.mozilla.org/pt-BR/docs/Web/CSS/box-shadow): Configura o sombreamento da caixa, assemelha-se a text-shadow

- [overflow](https://developer.mozilla.org/pt-BR/docs/Web/CSS/overflow): geralmente quando se tem um conteúdo que ultrapassa o temanha de sua div, tem-se 3 opções

  - visible
  - hidding
  - auto

- [opacity](https://developer.mozilla.org/pt-BR/docs/Web/CSS/opacity): Representa a porcentagem de transparência de algum conteúdo na qual 0 é o menos visível e 1 é o mais visível

## 4.6 BORDAS

- [border-radius](https://developer.mozilla.org/pt-BR/docs/Web/CSS/border-radius): Cria bordas arredondadas na qual o parâmetro é dado em pixels. E os parâmetros são o raio dos quatro cantos tem-se:
  - 1 campo: (todos os lados recebem este valor)
    ```CSS
    border-radius: 20px;
    ```
  - 2 campos: (a diagonal superior esquerda e inferior direita recebem 20px, e a diagonal superior direita e inferior esquerda rebem 5px)
    ```CSS
    border-radius: 20px 5px;
    ```
  - Preenchendo todos os valores, tem-se individualmente os valores para cada aresta.

Configuração de apenas uma borda pode-se utilizar:

- `border-top-left-radius: valor;`
- `border-top-right-radius: valor;`
- `border-bottom-left-radius: valor;`
- `border-bottom-right-radius: valor;`

[border-style](https://developer.mozilla.org/pt-BR/docs/Web/CSS/border-style): É o estilo da borda, pode ser do tipo do tipo cotted, dashed, solid, double, groove, ridge, inset, outset

[border-width](https://developer.mozilla.org/pt-BR/docs/Web/CSS/border-width): Define a espessura da borda

[border-color](https://developer.mozilla.org/pt-BR/docs/Web/CSS/border-color): Define a cor da borda

[outline](https://developer.mozilla.org/pt-BR/docs/Web/CSS/outline): Coloca linha externa ao elemente e não trabalha com lados individuais

## 4.7 FONTES

- [font-family](https://developer.mozilla.org/pt-BR/docs/Web/CSS/font-family): Familias de fontes

  ```CSS
  p{
    font-family: Times, "Times New Roman", serif;
  }
  ```

- [font-variant](https://developer.mozilla.org/pt-BR/docs/Web/CSS/font-variant): Apresenta a opção NORMAL e SMALL-CAPS

- [font-weight](https://developer.mozilla.org/pt-BR/docs/Web/CSS/font-weight): Apresenta a opção NORMAL e BOLD

- [font-style](https://developer.mozilla.org/pt-BR/docs/Web/CSS/font-style): Apresenta o NORMAL, ITALIC e OBLIQUE

- [font-size](https://developer.mozilla.org/pt-BR/docs/Web/CSS/font-size): Define o tamanho da fonte em pixels

### **4.7.1 Obter fonte externa**

```CSS
@font-face {
  font-family: open_sans;
  src: url(Endereço da fonte.woff)
}
```

> OBS: woff é a extensão do arquivo de fonte para web

- Exemplo:

```CSS
p {
  font-family: open_sans;
}
```

## 4.8 COMPORTAMENTO

- [float](https://developer.mozilla.org/pt-BR/docs/Web/CSS/float): Faz um certo componente flutar dentro de uma determinada divisão, para isso necessita-se colocar a qual lado a divisão irá flutua

- [position](https://developer.mozilla.org/pt-BR/docs/Web/CSS/position):

  - relative: Ajusta a posição do elemento, sem alterar o layout (e assim, mantendo o elemento caso não tivesse sido alterado).

  - absolute: Fica referenciado a página web, pode se colocar as direções rigth, top, left, e bottom

  - fixed: mantém fixa com as variações da página

# **5. PLANO DE FUNDO**

- [background](https://developer.mozilla.org/pt-BR/docs/Web/CSS/background): É o plano de fundo de uma divisão

- [background-color](https://developer.mozilla.org/pt-BR/docs/Web/CSS/background-color): Altera a cor do plano de fundo, pode ser dada em rgb(r, g, b), rgba(r, g, b, opacity), hexadecimal(#aaaaaa) e etc.

```CSS
p {
  background-color: black;
  background-color: rgb(100, 100, 100);
  background-color: rgba(100, 100, 100, 0.7);
}
```

- [linear-gradient](https://developer.mozilla.org/pt-BR/docs/Web/CSS/linear-gradient): Gradiente de cor na qual se tem duas cores, e o gradiente acontece da primeira cor para a segunda cor de acordo com a direção que foi dada para a direita, o default é para baixo(caso não coloque o campo da direção), há a possibilidade de se colocar mais de duas direções e até mesmo direções de acordo com angulos.

```CSS
p {
  background: linear-gradient(to rigth, red, blue);
}
```

- [radial-gradient](https://developer.mozilla.org/pt-BR/docs/Web/CSS/radial-gradient): A base é o centro da figura

```CSS
p {
  background: radial-gradient(red, green);
}
```

- [background-image](https://developer.mozilla.org/pt-BR/docs/Web/CSS/background-image): Colocar uma imagem como imagem de fundo

```CSS
p {
  background-image: url("https://i2.wp.com/ambientologia.com.br/wp-content/uploads/2016/03/css-logo.png?ssl=1");
}
```

- [background-repeat](https://developer.mozilla.org/pt-BR/docs/Web/CSS/background-repeat): pode ser do tipo

  - repeat-x: eixo horizontal
  - repeat-y: eixo vertical
  - no repeat

- [background-position](https://developer.mozilla.org/pt-BR/docs/Web/CSS/background-position): Define a posição do plano de fundo

- [background-attachment](https://developer.mozilla.org/pt-BR/docs/Web/CSS/background-attachment): Define se o plano de fundo irá acompanhar a barra de rolagem, para isso tem-se:

  - fixed: Plano de fundo fixo com relação a barra de rolagem
  - scroll: Acompanha a barra de rolagem

- [background-size](https://developer.mozilla.org/pt-BR/docs/Web/CSS/background-size): Define o tamanha do plano de fundo, dado em pixels ou porcentagem

# **6. TRANSITION**

- [transition](https://developer.mozilla.org/pt-BR/docs/Web/CSS/transition): controla a mudança de estados de acordo com alguns eventos

- [transition-property](https://developer.mozilla.org/pt-BR/docs/Web/CSS/transition-property): Propriedade que vai sofrer o efeito do transition

- [transition-duration](https://developer.mozilla.org/pt-BR/docs/Web/CSS/transition-duration): O tempo em que a duração demorará

- [transition-delay](https://developer.mozilla.org/pt-BR/docs/Web/CSS/transition-delay): Tempo para começar a transição

- [transition-timing-function](https://developer.mozilla.org/pt-BR/docs/Web/CSS/transition-timing-function): tem as funçães

  - ease-in: inicialize lenta
  - ease-out: termine lenta
  - ease-in-out: inicializa e termina lenta
  - linear

# **7. VARIÁVEIS**

- Exemplo:

```CSS
: root {
    --nomeDaVariável: valor;
    --bg-color: blue;
    --cor-do-texto: #fff;
    --espacamento: 20px;
  }
#div1 {background-color: var (--bg-color); color: var (--cor-do-texto); padding: var(--espacamento);}
```

# **8. NORMALIZE OU RESET**

Utiliza-se o normalize ou o reset para fazer com que as propriedades do CSS3 mantenha-se mais estável para todos os navegadores. Para isso tem-se:

- tem-se que fazer download do normalize ou reset (utiliza-se geralmente o do Eric Mayer).
- Cria-se um arquivo css com o conteúdo do download
- Cria-se um link, antes daquele referente a folha de estilo css da página referenciado ao arquivo baixado.

# **9. CÁLCULO**

Utilizado para realizar cálculos com os valores númericos das propriedades

```CSS
p {
  heigth: calc(100vw - 80px);
}
```

# **10. FILTROS**

Os filtros são propriedades de imagens

- [blur](https://developer.mozilla.org/pt-BR/docs/Web/CSS/filter-function/blur): Aplica desfoque em pixels

- [brightness](https://developer.mozilla.org/pt-BR/docs/Web/CSS/filter-function/brightness): Aplica brilho na tela em porcentagem, lembrando que o default é de 100%

- [contrast](https://developer.mozilla.org/pt-BR/docs/Web/CSS/filter-function/contrast): O padrão é 100%

- [grayscale](https://developer.mozilla.org/pt-BR/docs/Web/CSS/filter-function/grayscale): Adiciona tons de cinza na imagem, é dado em porcentagem, sendo que ela representa a quantidade de cinza que se aplica na imagem, na qual 100 é toda cinza

- [invert](https://developer.mozilla.org/pt-BR/docs/Web/CSS/filter-function/invert): inverte a coloração de 0 a 100%

- [opacity](https://developer.mozilla.org/pt-BR/docs/Web/CSS/filter-function/opacity): vai de 0 a 100% na qual 100% é a imagem totalmente visível

- [saturate](https://developer.mozilla.org/pt-BR/docs/Web/CSS/filter-function/saturate): Saturação da coloração da imagem em cores, 0 significa preto e branco, sendo que 100 é a coloração normal e acima de 100 as cores se tornam saturadas

- [sepia](https://developer.mozilla.org/pt-BR/docs/Web/CSS/filter-function/sepia): Sepia é uma coloração meio amarelada, envelhecida vai de 0 a 100%

- row-rotate: mudar as cores de acordo com a coloração de 0 a 100 deg

- [drop-shadow](https://developer.mozilla.org/pt-BR/docs/Web/CSS/filter-function/drop-shadow): aplica sombreamento na imagem
