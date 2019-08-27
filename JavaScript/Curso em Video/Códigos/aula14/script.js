function tabuada(){
    tab = window.document.querySelector('select#selec')
    n1 = window.document.querySelector('input#n1')
    n1 = Number(n1.value)

    tab.innerHTML = ''

    for (i=1; i<=10; i++){
        item = window.document.createElement('option')
        item.text = `${n1} x ${i} = ${n1*i}`
        tab.appendChild(item)
    }
}