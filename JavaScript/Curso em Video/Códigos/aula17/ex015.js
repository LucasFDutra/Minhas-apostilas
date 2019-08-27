function Pessoa(nome){
    this.getNome = function(){
        return nome
    }
    this.mostarNome = function(){
        console.log(this.getNome())
    }
}

function Atleta(velodade){
    this.getVelocidade = function(){
        return velodade
    }
    this.mostarVelocidade = function(){
        console.log(this.getVelocidade())
    }
}

Atleta.prototype = new Pessoa('Lucas')
atleta = new Atleta(10)

atleta.mostarNome()
atleta.mostarVelocidade()