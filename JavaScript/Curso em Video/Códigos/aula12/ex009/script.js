function carregar(){
    var msg = window.document.querySelector('div#msg')
    var img = window.document.querySelector('img#imagem')
    var data = new Date()
    var hora = data.getHours()
    
    msg.innerHTML = `Agora são ${hora} horas`
    if (hora < 12){
        // Bom dia
        img.src = 'Imagens/manha.png'
        window.document.body.style.background = '#bbcbae'
    }
    else if (hora < 18){
        // Boa tarde
        img.src = 'Imagens/tarde.png'
        window.document.body.style.background = '#f4c1a2'
    }
    else{
        // Boa noite
        img.src = 'Imagens/noite.png'
        window.document.body.style.background = '#013458'
    }
}

