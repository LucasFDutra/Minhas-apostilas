## Controlar os atributos de um elemento HTML com o v-bind

- [Veja](https://www.vuemastery.com/courses/intro-to-vue-js/attribute-binding)

- [Exemplo 1](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/tree/master/VueJS/002%20-%20v-bind/ex001): O vue coloca uma imagem para a gente
- [Exemplo 2](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/tree/master/VueJS/002%20-%20v-bind/ex002): O vue adiciona um link a imagem

Podemos controlar dinâmicamente os atributos de um elemento html através do vue.

Por exemplo, se tivermos o seguinte código com a inserção de uma imagem:

- Arquivo HTML

  ```HTML
  <div id="app">
      <div class="product">

          <div class="product-image">
              <!-- v-bind:atributo="nomo do elemento" para poder controlar via vue -->
              <img v-bind:src="image">
          </div>
      </div>
  </div>
  ```

Assim no código JS podemos controlar a imagem que queremos da seguinte forma:

- Arquivo JavaScript
  ```JavaScript
  var app = new Vue({
      el: '#app',
      data: {
          image: 'Socks-green.jpg'
      }
  })
  ```

Ou seja, se tivermos qualquer outro atributo e colocarmos `v-bind` na frente ele pode ser controlado com vue.

[Proximo Passo](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/tree/master/VueJS/003%20-%20condicional)
