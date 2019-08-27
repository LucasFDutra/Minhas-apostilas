## Componentes

- [Veja](https://www.vuemastery.com/courses/intro-to-vue-js/components)

A vantagem de criar um componente é que podemos replicá-lo diversas vezes, com caracteristicas diferentes, e de uma forma mais simples.

Pense bem, imagine se o aplicativo que estamos criando até agora tivesse que receber um segundo modelo de meia? precisariamos recriar tudo do zero para ela, e isso não é nem um pouco viável. Sendo assim se tudo que fizemos até agora for um componente é só chamarmos esse componente novamente e mandar outras propriedades como parametro.

Para definir um componente em vue vamos fazer da seguinte forma

```JavaScript
Vue.component('component_name', {
    props: {
        message: {
            type: String,
            required: true,
            default: "hi"
        }
    },
    template: `<div>{{message}}</div>` // todo código html
    data(){...}, // todos os dados
    methodes: {...}, //todos os métodos
    computed: {...} // todos os computeds
})
```

```HTML
<!-- Produto 1 -->
<component_name message="hello!"></component_name>
<!-- Produto 2 -->
<component_name message="como vai!"></component_name>
```

no caso do exemplo ficou assim:

- Arquivo HTML
  ```HTML
  <div id="app">
      <product :premium="premium"></product>
      <product></product>
  </div>
  ```

Veja que eu criei dois produtos, um para usuários primium que sairá de graça, e outro que não tem beneficios para usuários primiuns e sai por 2.99. Esse exemplo 'besta' pode moldado, e ao em vez de mandar se o produto premium ou não, poderiamos mandar uma imagem diferente para o produto, um preço diferente e ainda assim utilizar todo o layout e todos os métodos de um produto qualquer.

- Arquivo JavaScript

  ```JavaScript
  Vue.component('product', {
      props: {
          premium: {
              type: Boolean,
              required: true
          }
      },
      template: `
      <div class="product">
          <div class="product-image">...</div>

          <div class="product-info">
              <h1>{{title}}</h1>
              <p v-if="inStock > 10">In Stock</p>
              <p v-else-if="inStock<=10 && inStock > 0">Almost sold out!!</p>
              <p v-else>Out of Stock</p>
              <p> Shipping: {{shipping}}</p>
          </div>

          <ul>...</ul>
          <div v-for="(variant,index) in variants"... >...</div>
          <button @click="addToCart"... >...</button>
          <button @click="removeToCart"...>...</button>
          <div class="cart">...</div>
      </div>
      `,
      data() {
          return{
              brand: "Vue Mastery",
              product: 'Socks',
              selectedVariant: 0,
              inventory: 15,
              details: ["80% cotton", "20% polyester", "Gender-neutral"],
              variants: [
                  {
                      variantId: 2234,
                      variantColor: "green",
                      variantImage: "Socks-green.jpg",
                      variantQuantity: 0
                  },
                  {
                      variantId: 2235,
                      variantColor: "blue",
                      variantImage: "Socks-blue.jpg",
                      variantQuantity: 20
                  }
              ],
              cart: 0,
          }
      },
      methods:{
          addToCart: function(){...},
          removeToCart: function(){...},
          updateProduct: function(index){...}
      },
      computed: {
          title(){...},
          image(){...},
          inStock(){...},
          shipping(){
              if (this.premium){
                  return "Free"
              }else{
                  return 2.99
              }
          }
      }
  })

  var app = new Vue({
      el: '#app',
      data: {
          premium: true
      }
  })
  ```

[Proximo Passo](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/tree/master/VueJS/009%20-%20Comunicating%20Events)
