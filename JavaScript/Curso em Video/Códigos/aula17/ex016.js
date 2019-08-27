function Pessoa(valor){
    this.getValor = function(){
        return valor
    }
    this.adicionarValor = function(){
        console.log(this.getValor() + 2)
    }
}

Matematico = function(){}
Fisico = function(){}

Matematico.prototype = new Pessoa(1)
Fisico.prototype = new Pessoa(1)
m = new Matematico()
f = new Fisico()

Matematico.prototype.adicionarValor = function(){
    console.log(4 + 3)
}
    
m.adicionarValor() // modificou o método
f.adicionarValor() // não modificou nada