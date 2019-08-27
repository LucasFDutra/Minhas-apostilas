Vue.component('product', {
    props: {
        premium: {
            type: Boolean,
            required: true
        }
    },
    template: `
    <div class="product">
                
        <div class="product-image">
            <img v-bind:src="image">
        </div>

        <div class="product-info">
            <div>
                <h1>{{title}}</h1>
                <p v-if="inStock > 10">In Stock</p>
                <p v-else-if="inStock<=10 && inStock > 0">Almost sold out!!</p>
                <p v-else>Out of Stock</p>
                <p> Shipping: {{shipping}}</p>
            </div>

            <ul>
                <li v-for="detail in details">{{detail}}></li>
            </ul>

            <div v-for="(variant,index) in variants" 
            :key="variant.variantId"
            class="color-box"
            :style="{backgroundColor: variant.variantColor}"
            @mouseover="updateProduct(index)">
            </div>

            <button @click="addToCart" 
            :disabled="inventory==0"
            :class="{disabledButton: inStock==0}">Add to Cart</button>
            
            <button @click="removeToCart" 
            :disabled="cart==0"
            :class="{disabledButton: cart==0}">Remove to Cart</button>

            <div class="cart">
                <p>Cart({{cart}})</p>
            </div>
        </div>
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
        },
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

