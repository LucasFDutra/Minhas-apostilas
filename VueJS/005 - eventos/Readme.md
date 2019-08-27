## Eventos

- [Veja](https://www.vuemastery.com/courses/intro-to-vue-js/event-handling)

Vamos inserir um evento à nossa aplicação, e para controlar o evento vamos utilizar métodos, e para adicionar um método precisaremos fazer a seguinte modificação no nosso arquivo js.

```JavaScript
var app = new Vue({
    el: '#app',
    data: {
        // dados
    },
    methods:{
        // métodos
    }
})
```

No caso do exemplo iremos inserir um botão para poder adicionar um item ao carrinho, para tal precisaremos efetuar a seguinte mudança ao nosso código.

- Arquivo HTML
  ```HTML
  <button v-on:click="addToCart">Add to Cart</button>
  <div class="cart">
      <p>Cart({{cart}})</p>
  </div>
  ```

O comando `v-on` fica vigiando e retornará para o vue quando algo acontecer, e nesse caso um click, e quando isso ocorrer ele chamará o método `addToCart`. O qual podemos ver implementado abaixo.

- Arquivo JavaScript
  ```JavaScript
  methods:{
      addToCart: function(){
          this.cart += 1
      }
  }
  ```

O `this` é necessário pois estamos nos referindo a variavel cart que está dentro do nosso objeto json.

---

Porém agora iremos fazer com que a imagem da meia mude de acordo com onde passamos nosso mause, em blue ela ficará azul e em green ela ficará verde.

Para efetuar essa operação temos que efetuar alguns mudanças nos nossos arquivos.

- Arquivo HTML

```HTML
<div v-for="variant in variants" :key="variant.variantId">
    <p @mouseover="updateProduct(variant.variantImage)">{variant.variantColor}}</p>
</div>
```

Veja que agora eu não utilizei o `v-on` pois esse comando de mouseover e o click são bem comuns, então temos jeitos de fazer isso mais rápido, e um deles é esse `@mouseover`, que por sinal dessa vez chamará o método `updateProduct` e mandará como parametro a cor definida no arry variants.

O nosso arquivo js fica da seguinte forma:

- Arquivo JavaScript
  ```JavaScript
  var app = new Vue({
      el: '#app',
      data: {
          product: 'Socks',
          image: 'Socks-green.jpg',
          inventory: 0,
          details: ["80% cotton", "20% polyester", "Gender-neutral"],
          variants: [
              {
                  variantId: 2234,
                  variantColor: "green",
                  variantImage: "Socks-green.jpg"
              },
              {
                  variantId: 2235,
                  variantColor: "blue",
                  variantImage: "Socks-blue.jpg"
              }
          ],
          cart: 0
      },
      methods:{
          addToCart: function(){
              this.cart += 1
          },
          updateProduct: function(variantImage){
              this.image = variantImage
          }
      }
  })
  ```

Mas eu ainda colocarei um botão de retirada do carrinho, afinal de contas faz sentido a pessoa querer retirar produtos. Mas não colocarei isso aqui no readme, então veja o código completo.

---

Alguns exemplos de enventos:

```HTML
<button @click="metodo">mensagem</button>
<div @mouseover="metodo">mensagem</div>
<form @submit="metodo">mensagem</form>
<input @keyup.enter="metodo">
```

[Proximo Passo](https://github.com/LucasFDutra/Minhas-apostilas/tree/master/VueJS/006%20-%20classes%20e%20estilo)
