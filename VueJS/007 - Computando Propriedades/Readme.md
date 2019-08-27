## Computed Properties

- [Veja](https://www.vuemastery.com/courses/intro-to-vue-js/computed-properties)

Computed é uma maneira de criar dados a partir de outros dados. Basicamente os nossos dados serão gerados por funções

Nesse exemplo estou utilizando isso para modificar o titulo da aplicação.

Veja a parte do código html

- Arquivo HTML
  ```HTML
  <div class="product-info">
      <h1>{{title}}</h1>
      <p v-if="inventory > 10">In Stock</p>
      <p v-else-if="inventory<=10 && inventory > 0">Almost sold out!!</p>
      <p v-else>Out of Stock</p>
  </div>
  ```

Veja que antes tinhamos `<h1>{{product}}</h1>` e agora temos `<h1>{{title}}</h1>`. E esse title é uma função que está sendo buscada lá no nosso js.

- Arquivo JavaScript
  ```JavaScript
  data: {
      // dados
  },
  methods:{
          //metodos
      },
  computed: {
      title(){
          // computed geram dados, então não precisamos de titulo em dados, ele vai ser feito aqui.
          return this.brand + ' ' + this.product
      }
  }
  ```

> OBS.: Farei mais algumas modificações na aplicação, então veja o video que indiquei.

[Proximo Passo](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/tree/master/VueJS/008%20-%20Componentes)
