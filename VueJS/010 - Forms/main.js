Vue.component('product-review', {
    template: `
    <form class="review-form" @submit.prevent="onSubmit">
        <p>
            <label for="name">Nome:</label>
            <input for="name" v-model="name" placeholder="name" required>
        </p>

        <p>
            <label for="review">Review:</label>
            <textarea id="review" v-model="review" required></textarea>
        </p>

        <p>
            <label for="rating">Rating</label>
            <select id="rating" v-model.number="rating" required>
                <option>5</option>
                <option>4</option>
                <option>3</option>
                <option>2</option>
                <option>1</option>
            </select>
        </p>

        <p>
            <input type="submit" value="Submit">
        </p>
    </form>
    `,
    data(){
        return{
            name: null,
            review: null,
            rating: null
        }
    },
    methods:{
        onSubmit: function(){
            let productReview = {
                name: this.name,
                review: this.review,
                rating: this.rating
            }
            this.$emit('review-submitted', productReview)
            this.name = null
            this.review = null
            this.rating = null
        }
    }
})

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
        </div>

        <div>
        <h2>Reviews</h2>
        <p v-if="!reviews.length">There are no reviews yet.</p>
        <ul>
            <li v-for="review in reviews">
                <p>{{review.name}}</p>
                <p>{{review.review}}</p>
                <p>Rating: {{review.rating}}</p>
            </li>
        </ul>
        </div>

        <product-review @review-submitted="addReview"></product-review>
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
                    variantQuantity: 10
                },
                {
                    variantId: 2235,
                    variantColor: "blue",
                    variantImage: "Socks-blue.jpg",
                    variantQuantity: 20
                }
            ],
            reviews: []
        }
    },
    methods:{
        addToCart: function(){
            this.$emit('add-to-cart', this.variants[this.selectedVariant].variantId)
        },
        updateProduct: function(index){
            this.selectedVariant = index
        },
        addReview(productReview){
            this.reviews.push(productReview)
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
        premium: true,
        cart: []
    },
    methods: {
        updateCart: function(id){
            this.cart.push(id)
        }
    }
})
