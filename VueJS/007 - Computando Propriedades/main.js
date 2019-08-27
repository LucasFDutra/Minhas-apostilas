var app = new Vue({
    el: '#app',
    data: {
        brand: "Vue Mastery",
        product: 'Socks',
        // image: 'Socks-green.jpg',
        selectedVariant: 0, // indica que começo com a variante zero (meia verde)
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
        cart: 0
    },
    methods:{
        addToCart: function(){
            this.cart += 1
        },
        removeToCart: function(){
            this.cart -= 1
        },
        updateProduct: function(index){
            this.selectedVariant = index
            // this.image = variantImage
        }
    },
    computed: {
        title(){
            return this.brand + ' ' + this.product
        },
        image(){
            return this.variants[this.selectedVariant].variantImage
        },
        inStock(){
            return this.variants[this.selectedVariant].variantQuantity
        }
    }
})

