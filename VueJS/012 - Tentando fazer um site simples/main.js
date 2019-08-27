Vue.component('bar', {
    template:`
    <div id="div-geral">
        <div>
            <h1 id="title-box">{{title}}</h1>
            <ul id="menu-box">
                <li v-for="(m, index) in menu"
                @mouseover="updateImage(index)">{{m}}</li>
            </ul>
            <img v-bind:src="image" id="img-box">
        </div>
    </div>
    `,
    data() {
        return{
            selectedVariant: 0,
            menu: ["Python", "Java", "JavaScript", "C", "C++"],
            variants: [
                {
                    variantName: "Python",
                    varianteColor: "blue",
                    varianteImage: "Python-logo.png"
                },
                {
                    variantName: "Java",
                    varianteColor: "red",
                    varianteImage: "Java-logo.png"
                },
                {
                    variantName: "JavaScript",
                    varianteColor: "yellow", 
                    varianteImage: "JavaScript-logo.png"
                },
                {
                    variantName: "C",
                    varianteColor: "blue", 
                    varianteImage: "C-logo.png"
                },
                {
                    variantName: "C++",
                    varianteColor: "purple", 
                    varianteImage: "C++-logo.png"
                }
            ]
        }
    },
    methods: {
        updateImage(index){
            this.selectedVariant = index
        }
    },
    computed: {
        image(){
            return this.variants[this.selectedVariant].varianteImage
        },
        title(){
            return this.variants[this.selectedVariant].variantName
        }
    } 
})

var app = new Vue({
    el: '#app',
    
})