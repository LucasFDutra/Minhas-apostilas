function Pessoa(nome){
    // getters
    this.getNome = function(){
        return nome
    }

    // outros métodos
    this.mostrarNome = function(){
        console.log(this.getNome())
    }
}

function Atleta(p, velocidade){
    // Getter
    this.getVelocidade = function(){
        return velocidade
    }
    this.mostrarVelocidade = function(){
        console.log(this.getVelocidade())
    }
    this.mn = function(){
        p.mostrarNome()
    }
}

pessoa = new Pessoa('Lucas')
atleta = new Atleta(pessoa, 10)
atleta.mostrarVelocidade()
atleta.mn()