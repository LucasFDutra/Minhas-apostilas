## Controle de fluxo com condicionais

- [Veja](https://www.vuemastery.com/courses/intro-to-vue-js/conditional-rendering/)

Se quisermos controlar o fluxo da nossa aplicação utilizando o vue, podemos utilizar os comando:

```JavaScript
v-if
v-else-if
v-else
```

Essa condição deve ser inserida no componente html em questão, veja o exemplo:

- Arquivo HTML
  ```HTML
  <div id="app">
      <div class="product">
          <div class="product-info">
              <h1>{{product}}</h1>
              <p v-if="inventory > 10">In Stock</p>
              <p v-else-if="inventory<=10 && inventory > 0">Almost sold out!!</p>
              <p v-else>Out of Stock</p>
          </div>
      </div>
  </div>
  ```

Nesse exemplo teremos três possíveis retornos para o nosso componente `<p>`, veja que as condições são colocadas entre as aspas, e as fazemos assim como na linguagem C.

```HTML
<p v-if="condição">mensagem 1</p>
<p v-else-if="condição">mensagem 2</p>
<p v=esle>mensagem 3</p>
```

Agora veja o código js para essa aplicação

- Arquivo JavaScript
  ```JavaScript
  var app = new Vue({
      el: '#app',
      data: {
          product: 'Socks',
          image: 'Socks-green.jpg',
          inventory: 0 //coloque o valor aqui
      }
  })
  ```

[Proximo Passo](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/tree/master/VueJS/004%20-%20List%20Rendering)
