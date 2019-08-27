function verificar(){
    var nasc = window.document.querySelector('input#txtano')
    var resultado = window.document.querySelector('p#resultado')
    var date = new Date()
    var ano = date.getFullYear()
    
    // verificando se está tudo preenchido para dar segmento
    if (nasc.value.length == 0 || Number(nasc.value) > ano){
        window.alert('Verifique a data')
    }else{
        var sexo = window.document.getElementsByName('radsex')
        var img = window.document.querySelector('img#imagem')
        var genero
        var idade = ano - Number(nasc.value)

        // verificando o sexo
        if (sexo[0].checked){
            genero = 'Homem'
            if (idade<14){
                //criança
                img.src = 'Imagens/man0.png'
                window.document.body.style.background = '#cdcc99'
            }
            else if(idade<60){
                //adulto
                img.src = 'Imagens/man1.png'
                window.document.body.style.background = '#1dcbb0'
            }
            else{
                // idoso
                img.src = 'Imagens/man2.png'
                window.document.body.style.background = '#89a2a8'
            }
        }else{
            genero = 'Mulher'
            if (idade<14){
                //criança
                img.src = 'Imagens/woman0.png'
                window.document.body.style.background = '#ee886a'
            }
            else if(idade<60){
                //adulto
                img.src = 'Imagens/woman1.png'
                window.document.body.style.background = '#919a95'
            }
            else{
                // idoso
                img.src = 'Imagens/woman2.png'
                window.document.body.style.background = '#a66f33'
            }
        }
        // resultado.style.textAlign = 'center'
        resultado.innerHTML = `${genero} com ${idade} anos`
    }
}