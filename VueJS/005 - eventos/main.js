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
        removeToCart: function(){
            if(this.cart>0){
                this.cart -= 1
            }else{
                this.cart = 0
            }
        },
        updateProduct: function(variantImage){
            this.image = variantImage
        }
    }
})