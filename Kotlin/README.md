# Apostila de kotlin

Autor: Lucas Felipe Dutra

**ANTES DE QUALQUER COISA, VEJA ESSE VIDEO [AQUI](https://www.youtube.com/watch?v=9w3o9NHXqu0&list=PLMdYygf53DP5Sc6yFYs6ZmjsuuA2fu0TK) PARA APRENDER MAIS SOBRE CLEAN CODE**

# SUMÁRIO

- [**1. FERRAMENTAS**](#1-ferramentas)

- [**2. IDENTAÇÃO**](#2-identação)

- [**3. INTERAÇÃO USUÁRIO/SOFTWARE**](#3-interação-usuáriosoftware)

  - [3.1 RECEBER ENTRADA](#31-receber-entrada)
  - [3.2 IMPRIMIR NA TELA](#32-imprimir-na-tela)

- [**4. ESTRUTURAS COMPOSTAS - LISTAS**](#4-estruturas-compostas---listas)
  - [4.1 DECLARAÇÃO](#41-declaração)
  - [4.2 INSERINDO NOVOS TERMOS](#42-inserindo-novos-termos)
  - [4.3 ACESSAR UM TERMO](#43-acessar-um-termo)
  - [4.4 INCORPORANDO UMA LISTA À OUTRA](#44-incorporando-uma-lista-à-outra)
  - [4.5 INSERINDO ELEMENTO EM UMA POSIÇÃO ESPECÍFICA](#45-inserindo-elemento-em-uma-posição-específica)
  - [4.6 EXCLUINDO TERMO](#46-excluindo-termo)
  - [4.7 LIMPANDO UMA LISTA](#47-limpando-uma-lista)
  - [4.8 OBTER ÍNDICE DE UM ELEMENTO](#48-obter-índice-de-um-elemento)
  - [4.9 COPIANDO UMA LISTA](#49-copiando-uma-lista)
  - [4.10 RETORNAR O TAMANHO DE UMA LISTA](#410-retornar-o-tamanho-de-uma-lista)
  - [4.11 INVERTER OS ELEMENTOS](#411-inverter-os-elementos)
  - [4.12 ORDENAR UMA LISTA](#412-ordenar-uma-lista)
  - [4.13 MAIOR TERMO DA LISTA](#413-maior-termo-da-lista)
  - [4.14 VERIFICAR SE UM TERMO EXISTE NA LISTA](#414-verificar-se-um-termo-existe-na-lista)

* [**5. CONDICIONAIS**](#5-condicionais)

  - [5.1 IF](#51-if)
  - [5.2 ELSE IF](#52-else-if)
  - [5.3 ELSE](#53-else)
  - [5.4 OPERADORES](#54-operadores)

* [**6. ESTRUTURAS DE REPETIÇÃO**](#6-estruturas-de-repetição)

  - [6.1 FOR](#61-for)
    - [**6.1.1 Operador `..`**](#611-operador-)
    - [**6.1.2 Operador `until`**](#612-operador-until)
    - [**6.1.3 Operador `downTo`**](#613-operador-downto)
    - [**6.1.4 Loop for com uma lista**](#614-loop-for-com-uma-lista)
    - [**6.1.5 Observação importante**](#615-observação-importante)
  - [6.2 WHILE](#62-while)
  - [6.4 DO WHILE](#64-do-while)
  - [6.3 BREAK](#63-break)

* [**7. FUNÇÕES**](#7-funções)
  [7.1 FUNÇÕES COM N PARÂMETROS](#71-funções-com-n-parâmetros)
* [**8. PACOTES**](#8-pacotes)
* [**9. TRATAMENTO DE ERRO**](#9-tratamento-de-erro)

* [**10. CLASSE**](#10-classe)

  - [10.1 DECLARANDO UMA CLASSE](#101-declarando-uma-classe)
  - [10.2 EXTENDENDO UMA CLASSE](#102-extendendo-uma-classe)

* [**11. PROGRAMAÇÃO ORIENTADA A OBJETO**](#11-programação-orientada-a-objeto)
  - [11.1 DEFININDO OBJETOS](#111-definindo-objetos)
  - [11.2 DATA CLASS](#112-data-class)
  - [11.3 CONSTRUTOR PRIVADO](#113-construtor-privado)
  - [11.4 HERANÇA](#114-herança)
  - [11.5 SOBREPOSIÇÃO](#115-sobreposição)
  - [11.6 CLASSE ABSTRATA](#116-classe-abstrata)
  - [11.7 VISIBILIDADE DE VARIÁVEIS](#117-visibilidade-de-variáveis)

# **1. FERRAMENTAS**

- [Intellij IDEA](https://www.jetbrains.com/idea/)
- [Documentação](https://kotlinlang.org/docs/reference/)

# **2. IDENTAÇÃO**

Veja algumas caracteristicas do kotlin:

- **Comentários:** Para criar comentários utilize o caracter '//'.

- **Fim de comando:** O final de um comando é identificado quando acaba a linha.

```kotlin
println("ola") // comando 1
print("mundo") // comando 2
```

- **Bloco de código** Um bloco de código é representado pelo caracter `{}`.

```kotlin
  fun main(args: Array<String>){
    // testando
    println('Hello World')
  }
```

- **Variáveis:** Teremos os seguintes tipos de variáveis:

  - Int
  - Long
  - String
  - Char
  - Double
  - Boolean

  Podemos declarar variáveis utilizando os comandos `var` ou `val`. A diferença entre eles é:

  - var: A variável pode mudar seu valor.
  - val: A variável é imutável.

  Sendo que no processo de declaração da variável podemos ou não definir a qual tipo ela pertence. Pois o kotlin consegue identificar o tipo da variável automaticamente. Veja como fazer a declaração de variáveis.

  ```kotlin
  // Utilizando var
  var nome_da_variavel: tipo_da_variavel // não definida
  var nome_da_variavel: tipo_da_variavel = valor // pré-definida
  var nome_da_variavel = valor

  // Utilizando val
  val nome_da_variavel: tipo_da_variavel // não definida -> assim que definir um valor ele não poderá mudar
  val nome_da_variavel: tipo_da_variavel = valor // pré-definida
  val nome_da_variavel = valor
  ```

  - **String:** Uma string é basicamente um array, logo ela terá algumas propriedades próprias.

    - **Tamanho da string:**

      - `nome_da_string.length`

    - **Pegando caracter especifífico da string:**
      - `nome_da_string[posição]`

  - **Conversão de variáveis:** Como não podemos efeturar atribuições entre variáveis de tipos diferentes, muitas vezes torna-se necessário efetuar a conversão de tipos, para isso utilizamos:

    ```kotlin
    var_1 = var_2.toTipo_var_1
    ```

    As conversões que temos são:

    - `toByte()`
    - `toChar()`
    - `toDouble()`
    - `toFloat()`
    - `toInt()`
    - `toLong()`
    - `toShort()`
    - `toString()`

    Veja o exemplo abaixo:

    ```kotlin
    var x: Int = 10
    var y: String

    y = x.toString()
    ```

# **3. INTERAÇÃO USUÁRIO/SOFTWARE**

## 3.1 RECEBER ENTRADA

Para receber uma entrada utiliza-se o comando `readLine`

```kotlin
//caso não seja string
var nome_da_variável: Tipo = readLine()?.toTipo()!!

//caso seja string
var nome_da_variável = readLine()!!
```

> OBS.: Os caracteres `?` e `!!` estão ali pois podemos ter a atribução de um valor nulo para x, e o kotlin não nos deixa prosseguir, então o comando `?` indica que eu quero que ele faça a operação de conversão de tipo caso não tenhamos nulo, e o operador `!!` indica que é para considerar o valor somente se não for nulo.

Veja o Exemplo:

```kotlin
fun main(){
    var x: Int
    println("digite o valor de x: ")
    x = readLine()?.toInt()!!

    println(x)
}
```

## 3.2 IMPRIMIR NA TELA

Para exibir algo na tela utiliza-se o comando `println`

```kotlin
println("texto") //Mostra apenas um texto
println(var) //mostra o valor da variável
println("texto %var") //Mostra um texto seguido do valor de uma variável
println("texto %{comando}") //Mostra um texto seguido do retorno de uma função
```

Veja um exemplo:

```kotlin
var linguagem: String = "kotlin"

println(linguagem) //retorna 'kotlin'
println("A linguagem é: $linguagem") //retorna 'A linguagem é: kotlin'
println("${linguagem[1]}") //retorna 'o'
println("${linguagem.length}") //retorna '6'
```

# **4. ESTRUTURAS COMPOSTAS - LISTAS**

Listas conseguem receber diferentes tipos de variáveis dentro delas, ou seja, var_0 pode ser de tipo diferente de var_1.

Porém, também podemos criar essas listas definido quais os tipos de variáveis que elas receberão, assim podemos deixar elas em branco, e ir preenchendo durante o código (claro, somente aquelas que forem mutáveis).

## 4.1 DECLARAÇÃO

Temos diferentes jeitos de criar listas, com os comandos:

- `listOf`: A lista é imutável. Ou seja, é impossível adicionar novos termos durante o código.
- `mutableListOf`: A lista é mutável.
- `arrayListOf`: Que também é mutável.
- `setOf`: Cria uma lista que não permite que existam elementos repetidos. E é imutável.
- `mutableSetOf`: Cria uma lista que não permite que existam elementos repetidos. E é mutável.

**pré definindo os valores**

```kotlin
var lista_1 = listOf(var_0,...,var_n)
var lista_2 = mutableListOf(var_0,...,var_n)
var lista_3 = arrayListOf(var_0,...,var_n)
var lista_4 = setOf(var_0,...,var_n)
var lista_5 = mutableSetOf(var_0,...,var_n)
```

**Adicionando depois**

```kotlin
var lista_1: MutableList<Int> = mutableListOf()
var lista_2: ArrayList<Int> = arrayListOf()
var lista_3: MutableSet<Int> = mutableSetOf()
```

## 4.2 INSERINDO NOVOS TERMOS

Utilize o comando `add`.

```kotlin
lista.add(valor)
```

Veja o exemplo abaixo:

```kotlin
fun main(){
    var lista_1: MutableList<Int> = mutableListOf()
    var lista_2: ArrayList<Int> = arrayListOf()
    var lista_3: MutableSet<Int> = mutableSetOf()


    lista_1.add(1)
    lista_2.add(2)
    lista_3.add(3)

    println(lista_1) //saída: [1]
    println(lista_2) //saída: [2]
    println(lista_3) //saída: [3]
}
```

## 4.3 ACESSAR UM TERMO

```kotlin
lista[posição_do_termo]
```

## 4.4 INCORPORANDO UMA LISTA À OUTRA

```kotlin
lista.addAll(lista_2)
```

## 4.5 INSERINDO ELEMENTO EM UMA POSIÇÃO ESPECÍFICA

```kotlin
lista.add(index = posição, element = valor)
```

## 4.6 EXCLUINDO TERMO

```kotlin
lista.remove(valor_a_ser_removido)
lista.removeAt(posição)
```

O primeiro método vai elimina por valor, já o segundo elimina por posição. Ou seja, se tivermos uma lista `[1,2,3,1]` e mandarmos retirar o valor o segundo valor 1 os resultados serão:

```
lista.remove(1) # lista final: [2,3,1] -> não cumpre a função quando temos um número mais de uma vez
lista.removeAt(3) # lista final: [1,2,3]
```

## 4.7 LIMPANDO UMA LISTA

```kotlin
lista.clear()
```

## 4.8 OBTER ÍNDICE DE UM ELEMENTO

```kotlin
lista.indexOf(termo)
```

A busta é feita por valor, ou seja o que a função retorna é o valor da menor posição na lista em que se encontra o termo desejado.

## 4.9 COPIANDO UMA LISTA

```kotlin
nova_lista.addAll(lista) //meio na gambiarra
```

## 4.10 RETORNAR O TAMANHO DE UMA LISTA

```kotlin
lista.count()
lista.size
```

## 4.11 INVERTER OS ELEMENTOS

```kotlin
lista.reverse()
```

## 4.12 ORDENAR UMA LISTA

```kotlin
lista.sort()
```

## 4.13 MAIOR TERMO DA LISTA

```kotlin
lista.max()
```

## 4.14 VERIFICAR SE UM TERMO EXISTE NA LISTA

```kotlin
lista.contains(termo)
```

# **5. CONDICIONAIS**

## 5.1 IF

```kotlin
if (condição){
  Código...
}
```

## 5.2 ELSE IF

É uma condição que só é analisada caso a condição em `if` não seja atendida.

```kotlin
else if (condição){
  Código...
}
```

## 5.3 ELSE

Engloba tudo que for o contrário das condições impostas em `if` e `else if`.

```kotlin
else{
  Código...
}
```

## 5.4 OPERADORES

- **&&:** Condição 'a' e condição 'b' devem ser atendidas.

- **||:** Condição 'a' ou condição 'b' devem ser atendidas.

- **maior:** >

- **maior ou igual:** >=

- **menor:** <

- **menor ou igual:** <=

- **diferente:** !=

- **igual:** ==

- **Verdadeiro:** true

- **Falso:** false

Veja o exemplo:

```kotlin
var a = 1
var b = 2

if (a == b){
  println("$a é igual à $b")
}
else if (a > b){
  println("$a é maior do que $b")
}
else if(a==2 || a==3){
  println("'a' é igual a 2 ou igual a 3")
}
else if(a==2 && b==3){
  println("'a' é igual a 2 e 'b' é igual a 3")
}
else{
  println("$a é diferente de $b")
}

```

# **6. ESTRUTURAS DE REPETIÇÃO**

## 6.1 FOR

> OBS.: A variável que será o contador (`i`) não precisa ser declarada anteriormente.

### **6.1.1 Operador `..`**

Faz com que o limite máximo seja incluido no for.

```kotlin
for (i in de_onde..até_onde){
  Código...
}
```

Veja o exemplo de uma função que irá mostrar o valor de i indo de 0 até 10.

```kotlin
for (i in 0..10){
  println(i) //saída: 0,1,2,3,4,5,6,7,8,9,10
}
```

### **6.1.2 Operador `until`**

O valor do limite máximo não entra no for.

```kotlin
for (i in de_onde until até_onde){
  Código...
}
```

Pode-se utlizar em conjunto o operador `step` para pular casas.

```kotlin
for (i in de_onde until até_onde step passo){
  Código...
}
```

Veja o exemplo:

```kotlin
for (i in 0 until 10 step 2){
  println(i) // saída: 0,2,4,6,8
}
```

### **6.1.3 Operador `downTo`**

Os limites são inclusos, e sua função é ir reduzindo o valor do contador.

Ele também pode acompanhar o operador `step`, porém sem ele a redução ocorrerá de um em um.

```kotlin
for (i in de_onde downTo até_onde step passo)
```

Veja o exemplo:

```kotlin
for (i in 10 downTo 0){
  println(i) //saída: 10,9,8,7,6,5,4,3,2,1,0
}
```

### **6.1.4 Loop for com uma lista**

```kotlin
for (i in lista){
  println(i) //saída: var_0, var_1,...var_n
}
```

### **6.1.5 Observação importante**

Quando utilizamos um loop for, o contador não precisa ser definido antes do loop. Porém se tentarmos utilizá-lo após o loop teremos um erro. Pois o contador só existe dentro do loop. Logo se quisermos utilizar ele fora do loop precisamos declará-lo anteriormente, porém aqui temos outro problema, as modificações que são feitas no contador serão excluidas e ele retornará ao seu estado original assim que acabar o loop.

Veja o exemplo:

```kotlin
var i = 15
for (i in 0 until 3){
  println(i) //saída: 0,1,2
}
println(i) //saída: 15
```

## 6.2 WHILE

No while a variável de controle precisa ser declara anteriormente. E diferentemente do `for`, as auterações que ela recebe dentro do loop permanecem fora dele.

```kotlin
while(condição){
  Código...
}
```

Veja o exemplo:

```kotlin
var i = 6
while(i>3){
  println(i) //saída: 6,5,4
  i--
}
println(i) //saída: 3
```

## 6.4 DO WHILE

a diferença entre o `do while` e `while` é que no `do while` o código é executado primeiro e depois que a condição é verificada.

```kotlin
do{
  Código...
}while(condição)
```

Veja o exemplo:

```kotlin
var i = 6
do{
  println(i) //saída: 6,5,4
  i--
}while(i>3)
```

Veja agora dois códigos iguais utilizando `do while` em um e `while` no outro.

- Aqui o programa entra do `do` e executa, depois quando ve que a condição não foi satisfeita ele sai do loop

```kotlin
var i = 0

do{
  println(i) //saída: 0
}while(i>1)
```

- Aqui o programa verifica a condição antes de entrar no loop, e ve que ela não é satisfeita, logo ele pula o loop.

```kotlin
var i = 0

while(i>1){
  println(i) //saída:
}
```

## 6.3 BREAK

O comando `break` serve para interromper um loop caso alguma condição especial ocorra.

```kotlin
for(i in 0 until 3){
  println(i) //saída: 0,1
  if (i==1){
    break
  }
  println(i) //saída: 0
}
```

# **7. FUNÇÕES**

Para criar uma função utilize o comando `fun`

```kotlin
fun nome_da_função(parâmetro_1: tipo_1, parâmetro_2: tipo_2,...): tipo_do_retorno{
  Código...
  return o_que_retornar
}
```

> OBS.: Não coloque nada em tipo_do_retono e nem a linha `return` caso não vá retornar nada

Vejamos um exemplo de função

```kotlin
fun função(a: Int, b: Int): Int{
  return a+b
}

fun main(){
  var x: Int
  x = função(3,4)
  println(x) //exibe o valor 7

  x = função(a=3, b=4)
  println(x) //exibe o valor 7
}
```

## 7.1 FUNÇÕES COM N PARÂMETROS

Quando não sabemos quantos parâmetros iremos passar para uma função, precisamos utilizar o comando `vararg`. Veja como fazemos isso:

```kotlin
fun nome_da_função(vararg parametro: Tipo){
  Código...
}

fun main(){
  nome_da_função(parametro_1, parametro_2,..., parametro_n)
}
```

O único problema desse método é que todos os parâmetros precisão ser do mesmo tipo de dados. Para contornar esse problema fazemos:

```kotlin
fun <uma_palavra_qualquer> nome_da_função(vararg parametro: uma_palavra_qualquer){
  Código...
}

fun main(){
  nome_da_função(parametro_1, parametro_2,..., parametro_n)
}
```

Veja um exemplo:

```kotlin
fun <T> funcao(vararg parametro: T){
    for (i in parametro){
        println(i) //saída: string de teste, 1, 3.1415, outra string
    }
}

fun main(){
    funcao("string de teste", 1, 3.1415, "outra string")
}
```

# **8. PACOTES**

Um pacote é a mesma coisa que uma biblioteca. Para criar um pacote e usá-lo siga os passo:

- 1. Crie um arquivo `.kt` e na primeira linha escreva `package nome_do_pacote`.
- 2. Escreva os códigos para sua biblioteca.
- 3. No arquivo principal digite:
  - Para importar uma função específica: `import nome_do_pacote.função`.
  - Para importar todas as funções: `import nome_do_pacote.*`.

Veja o exemplo

```kotlin
// esse seria o aquivo do pacote
package pacote

fun função_1(){
  println("olá")
}

fun função_2(){
  println("mundo")
}
```

```kotlin
// esse seria o arquivo principal
import pacote.*

fun main(){
  função_1()
  função_2()
}
```

# **9. TRATAMENTO DE ERRO**

Para tratar um erro vamos utilizar `try`, `catch` e `finally`.

- try: O código irá tentar executar o que está dentro dessa seção.
- catch: O catch precisa ter uma exceção (erro) especificado que ele irá tratar. Ou seja, caso ocorra um erro específico no bloco `try` entraremos no bloco `catch`.
- finally: O bloco `finally` irá executar independentemente se houver ou não um erro. Esse bloco é opcional.

Veja como utilizar esses comandos:

```kotlin
try{
  Código...
} catch (e: nome_da_exeção){
  Código de tratamento...
} catch (e: outra_exeção){
  Código de tratamento...
} finally{
  Código que será executado em qualquer caso...
}
```

Veja o exemplo:

```kotlin
try{
  var numero = "1".toString() //gera um erro de NumberFormatException
} catch(e: NumberFormatException){
  println("deu erro de NumberFormatException") //irá entrar nessa seção e executará
} finally{
  println("o finally executa de qualquer forma") //irá entrar nessa seção e executará
}
```

> OBS.: Se quisermos um tratamento de erro mais generalista, podemos colocar a exceção: `Exception` que é uma exceção generica.

- Veja mais sobre exceções na [documentação](https://kotlinlang.org/docs/reference/exceptions.html) da linguagem.

# **10. CLASSE**

## 10.1 DECLARANDO UMA CLASSE

```kotlin
class nome_da_classe(){
  Conjunto_de_funções...
}

fun main(){
  val objeto_classe = nome_da_classe()

  objeto_classe.função_da_classe()
}
```

Veja o exemplo:

```kotlin
class Pessoa(){
    fun dados(nome: String, idade: Int){
        println("$nome tem $idade anos")
    }
}

fun main(){
    val obj_pessoa = Pessoa()

    obj_pessoa.dados("joão", 18) // saída: joão tem 18 anos
}
```

> OBS.: não se pode executar código fora de algum método da classe. Ou seja, não pdemos fazer:

```kotlin
class classe(){
  println("não é possível fazer issso")
}
```

## 10.2 EXTENDENDO UMA CLASSE

Quando extendemos uma classe estamos apenas acressentando novas funções à classe em questão. Ou seja, estamos criando extensões para essa classe.

```kotlin
class nome_da_classe(parametros){ //os parâmetros são opcionais
  Conjunto_de_funções...
}

fun main(){
  val objeto_classe = nome_da_classe()

  nome_da_classe.nova_função_da_classe(){
    Código da função
  }

  objeto_classe.nova_função_da_classe()
}
```

Veja o exemplo:

```kotlin
class Pessoa(){
    fun dados(nome: String, idade: Int){
        println("$nome tem $idade anos")
    }
}

fun main(){
    val obj_pessoa = Pessoa()

    fun Pessoa.novos_dados(peso: Int, sexo: String){
        println("peso: $peso, sexo: $sexo")
    }


    obj_pessoa.dados("João", 18) // Saída: 'João tem 18 anos'
    obj_pessoa.novos_dados(75, "masculino") // Saída: 'peso: 75, sexo: masculino'
}
```

> OBS.: não é possível sobreescrever um método de uma classe.

# **11. PROGRAMAÇÃO ORIENTADA A OBJETO**

Toda a programação orientada a objeto é feita com base em classes. E como todo objeto possui seus atributos (cor, tamanho, peso, etc) e seus métodos (funções desse objeto, como por exemplo, reproduzir música), uma classe irá conter exatamente essas duas coisas.

## 11.1 DEFININDO OBJETOS

Uma classe equivale à um dado objeto, porém generico, como por exemplo um carro. Os parâmetros de uma classe são os atributos desse objeto, como por exemplo o modelo do carro, sua velocidade máxima. E as funções de uma classe seriam os métodos de um objeto, como por exemplo o método freiar. Veja a construção de um objeto.

```kotlin
class nome_da_classe(parametros){
  init{
    Código que se inicia junto com a classe...
  }

  Código da classe...
}

fun main(){
  val obj_1 = nome_da_classe(parametros)
  val obj_2 = nome_da_classe(parametros) //utilizei val pq normalmente um objeto não fica mudando
}
```

O método `init` é opcional, mas quando ele está presente tudo o que estiver dentro dele será executado assim que um objeto da classe for instanciado no bloco `main`.

Veja um exemplo:

```kotlin
class carro(var modelo: String, var velocidade_maxima: Int){
    init {
        println("Objeto definido")
    }

    fun mostrar_objeto(){
        println("o modelo do carro é o: $modelo")
        println("a velocidade maxima do carro é de: $velocidade_maxima")
    }
}

fun main(){
    val fusca = carro(modelo = "fusca", velocidade_maxima = 120) //saída: Objeto definido

    fusca.mostrar_objeto() //saída: o modelo do carro é o: fusca
                           //       a velocidade maxima do carro é de: 120
}
```

## 11.2 DATA CLASS

Se declararmos uma classe utilizando o comando `class` e depois definirmos dois objetos idênticos, não tem como (não de um jeito simples) varificarmos se esses dois objetos são realmente iguais. Pois cada objeto é alocado em espaços diferentes da mémoria então por mais que os atributos sejam iguais o comando `equals` não consegue identificar se o objeto A é igual a B.

> OBS.: O comando `equals` é utilizado da seguinte forma: `obj_a.equals(obj_2)` e retorna `true` se obj_a == obj_2, e caso contrário retorna `false`.

No caso de um programa de cadastro de pessoas veja o tanto que a falta de capacidade de verificar se a mesma pessoa está se cadastrando mais de uma vez é horrivel.

Para resolver esse problema podemos utilizar `data class` para declarar uma classe. Pois com ele é possível efetuar essa verificação facilmente.

Veja um exemplo de cadastro de pessoas

```kotlin
data class pessoa (var nome: String ,var idade: Int){
    init {
        println("$nome tem $idade anos")
    }
}

fun main(){
    var pessoa_1 = pessoa("joão", 18) //saída: joão tem 18 anos
    var pessoa_2 = pessoa("joão", 18) //saída: joão tem 18 anos

    println(pessoa_1.equals(pessoa_2)) //saída: true
}
```

Agora que foi possível verificar que são iguais é possivel criar algoritmos para impedir cadastros duplicados.

## 11.3 CONSTRUTOR PRIVADO

O construtor é aquilo que constroi o objeto, ou seja, é aquela linha no `main` em que dizemos que uma variável é igual à nossa classe e passamos os seus parâmetros. Porém tem como declararmos que o construtor de uma classe será privado.

Quando o construtor é privado significa que é impossível criar o objeto a partido do `main`. E obviamente como essa classe não pode construir objetos em outros lugares ela não será chamada, então não tem porque poder passar parâmetros para ela (atributos). Sendo assim a declaração de uma classe com construtor privado fica da seguinte maneira:

```kotlin
class nome_da_classe private constructor(){
  // Atributos
  // métodos
}
```

Nesse caso o que é mais comum de ser feito é a criação de atributos dentro da classe, visto que não da para construí-los.

## 11.4 HERANÇA

Herança é o nome dado para a relação entre uma classe pai e uma classe filha. A filha herda os métodos e os atributos da classe pai, ou seja, se o pai faz uma coisa 'x', a filha também fará, se a classe pai possui y, a classe filha também. Porém, é possível que a classe filha herde somente uma das duas coisas.

```kotlin
open class pai(var: parametros_de_pai){
  //métodos
}

class filha(parametros_herdados, var: parametros_de_filha) : pai(parametros_de_pai){
  //métodos_da_filha
}
```

Veja um exemplo de herança apenas de métodos.

```kotlin
open class pai(){
    init {
        println("classe pai")
    }

    fun função_pai(){
        println("função pai")
    }
}

class filha() : pai(){
    init {
        println("classe filha")
    }
    fun função_filha(){
        println("função filha")
    }
}

fun main(){
    var p = pai() //saída: classe pai
    var f = filha() //saída: primeiro 'classe pai', depois sairá 'classe filha'

    // executa a função pai
    p.função_pai() //saída: função pai

    // executa a função filha
    f.função_filha() //saída: função filha

    // a filha executa a função pai
    f.função_pai() //saída: função pai
}
```

O proximo exemplo possui atributos, ou seja a herança será de métodos e atributos.

Nesse exemplo podemos ver que a classe filha não precisa ficar colocando `var nome` `var idade` pois isso tudo já foi herdado da classe pai, ela só precisa dizer que foi herdado, já o atributo `cabelo` é algo novo, logo é necessário colocar o comando `var`.

```kotlin
open class pai(var nome: String, var idade: Int){
    init {
        println("classe pai")
    }

    fun função_pai(){
        println("função pai. nome: $nome, idade: $idade")
    }
}

class filha(nome: String, idade: Int, var cabelo: String) : pai(nome, idade){
    init {
        println("classe filha")
    }
    fun função_filha(){
        println("função filha. $nome, $idade, $cabelo")
    }
}

fun main(){
    var p = pai("PAI", 50) //saída: classe pai
    var f = filha("FILHA", 18, "loira") //saída: primeiro 'classe pai' e depois 'classe filha'

    p.função_pai() //saída: função pai. nome: PAI, idade: 50
    f.função_filha() //saída: funçao filha. FILHA, 18, loira
    f.função_pai() //saída: função pai. nome: FILHA, idade: 18
}
```

## 11.5 SOBREPOSIÇÃO

É quando a classe filha tem um método identico ao da classe pai, porém ela vai preferir fazer do jeito dela, sendo assim ela desconsidera o jeito que o pai faz aquele método e o sobrescreve. Para isso basta apenas escrever uma função na classe filha que tenha o mesmo nome que a função na classe pai, antecedido do comando `override` e a função na classe pai precisa ter escrito na frente o comando `open`.

````kotlin
open class pai(){
  open fun teste_sobreposição(){
    // Códigos pai
  }
}

class filha() : pai(){
  override fun teste_sobreposição(){
    // Códigos filha
  }
}

Veja um exemplo:

```kotlin
open class pai(){
    init {
        println("classe pai")
    }

    open fun teste_sobreposição(){
        println("função pai")
    }
}

class filha() : pai(){
    init {
        println("classe filha")
    }
    override fun teste_sobreposição(){
        println("função filha")
    }
}

fun main(){
    var p = pai() //saída: classe pai
    var f = filha() //saída: primeiro 'classe pai', depois sairá 'classe filha'

    p.teste_sobreposição() //saída: função pai
    f.teste_sobreposição() //saída: função filha
}
````

## 11.6 CLASSE ABSTRATA

Uma classe abstrata não pode ser instanciada, porém ela é útil quando queremos definir dentro dela vários métodos e atributos que serão obrigatórios, porém não fazem sentido em serem instanciados apenas herdados.

```kotlin
abstract class classe(parametros){
  //métodos
}
```

> OBS.: é possivel criar um método sem corpo, que está ali apenas para ser sobrescrito.

```kotlin
abstract class pai(parametros){
  abstract metodo()
}

class filha() : pai(){
  override fun metodo(){
    //código..
  }
}
```

## 11.7 VISIBILIDADE DE VARIÁVEIS

Temos aqui o `private` e `protected`.

- private: Faz com que a variável exista somente dentro da classe, assim ela só pode ser modificada por algum método da mesma.
- protected: extende a existencia do atributo para as classes filhas dessa classe.

```kotlin
class nome_da_classe(){
  private var variável: Tipo = valor
  protected var variável: Tipo = valor
}
```

Veja que no exemplo abaixo é possível auterar o valor de x_2 pela classe filha, mas o valor de x_1 só foi possível de auterar pelas funções da classe pai.

```kotlin
open class pai(){

    private var x_1 = 0
    protected var x_2 = 0

    fun mudar_x1() {
        x_1 = 80
        println(x_1)
    }
}

class filha() : pai(){
    fun mudar_x2(){
        x_2 = 120
        println(x_2)
    }
}

fun main(){
    val obj_pai = pai()
    val obj_filha = filha()

    obj_pai.mudar_x1() //saída: 80
    obj_filha.mudar_x2() //saída: 120
}
```
