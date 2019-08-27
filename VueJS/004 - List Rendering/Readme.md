## List Rendering - Loop

- [Veja](https://www.vuemastery.com/courses/intro-to-vue-js/list-rendering)

Faremos aparecer uma lista dentro da nossa página utilizando `v-for`.

Utilizando o comando

```HTML
v-for = "variavel in lista">{{variavel}}
```

Au seja, variavel recebe cada elemento da lista e joga dentro das chaves.

Agora se colocarmos isso dentro de uma lista html `ul` ou `ol` teremos então que cada elemento da lista será dado automaticamente de acordo com o array desejado. Veja como fica no nosso exemplo:

- Arquivo HTML

  ```HTML
  <ul>
      <!-- fara o loop for em details e armazenará em d -->
      <li v-for="d in details">{{d}}></li>
  </ul>
  ```

- Arquivo JavaScript
  ```JavaScript
  var app = new Vue({
      el: '#app',
      data: {
          details: ["80% cotton", "20% polyester", "Gender-neutral"]
      }
  })
  ```

Veja o código completo [aqui](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/tree/master/VueJS/004%20-%20List%20Rendering/ex001)

[Proximo Passo](https://github.com/LucasFDutra/Meu-Material-Basico-De-Web/tree/master/VueJS/005%20-%20eventos)
