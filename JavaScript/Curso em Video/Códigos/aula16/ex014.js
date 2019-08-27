class Pessoa{
    constructor(n, i){
        this.setNome(n)
        this.setIdade(i)
    }
    // setters e getters
    setNome(n){
        this.nome = n
    }
    setIdade(i){
        this.idade = i
    }
    getNome(){
        return this.nome
    }
    getIdade(){
        return this.idade
    }

    // outros métodos
    mostrarNome(){
        console.log(this.getNome())
    }
    mostrarIdade(){
        console.log(this.getIdade())
    }
}

pessoa = new Pessoa('Lucas', 24)
pessoa.mostrarNome()
pessoa.mostrarIdade()
