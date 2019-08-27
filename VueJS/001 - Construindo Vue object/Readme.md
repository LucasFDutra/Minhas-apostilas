## Iremos criar nossa primeira página, vamos utilizar o vue para controlar o HTML.

---

- [Veja](https://www.vuemastery.com/courses/intro-to-vue-js/vue-instance)

Primeiramente precisa-se criar dois aquivos (no minimo), o arquivo `html` e o arquivo `js`. Dentro do arquivo html crie um script adicionando o vue, e outro adicionando o arquivo js. Veja abaixo:

```HTML
<body>
    <script src="https://cdn.jsdelivr.net/npm/vue"></script>
    <script src="main.js"></script>
</body>
```

---

Depois escreva o seu html normalmente, nesse caso terá apenas uma div como mostrado abaixo.

```HTML
    <body>
    <div id="app">
        <h1>{{ product }}</h1>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue"></script>
    <script src="main.js"></script>
</body>
```

escolha um lugar que quiser que seja variável, nesse caso eu escolhi dentro de h1, e coloque a variavel entre `{{ variável }}`, ou seja, no exemplo anterior a variável é `product`.

---

Agora vamos ver o arquivo js.

Primeiramente precisamos criar um objeto Vue, e passar alguns parametros para ele, são eles:

- el: Elemento a ser modificado no html
- data: dados que o elemento recebe

Sendo que esse parametro na verdade é um json.

Seguindo o exemplo anterior o código ficará da seguinte forma.

```JavaScript
var app = new Vue({
    el: '#app', //# pois utiliza-se o id
    data: {
        product: 'Socks'
    }
})
```

[Proximo Passo](https://github.com/LucasFDutra/Minhas-apostilas/tree/master/VueJS/002%20-%20v-bind)
