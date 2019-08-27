# Apostila de C++

Autor: Lucas Felipe Dutra

**ANTES DE QUALQUER COISA, VEJA ESSE VIDEO [AQUI](https://www.youtube.com/watch?v=9w3o9NHXqu0&list=PLMdYygf53DP5Sc6yFYs6ZmjsuuA2fu0TK) PARA APRENDER MAIS SOBRE CLEAN CODE**

# **DICAS**

[Documentação](https://devdocs.io/cpp/)

[Code Blocks](http://www.codeblocks.org/)

[Visual Studio Code](https://code.visualstudio.com/)

[Atom](https://atom.io/)

[Sublime Text](https://www.sublimetext.com/)

Para compilar os códigos sem utilizar uma IDE, primeiro você deve instalar o compilador.

> sudo apt-get install g++

Após ter instalado o compilador, utilize o comando abaixo para compilar e executar o seus códigos:

> g++ nome_do_arquivo.cpp -o nome_do_arquivo.run && ./nome_do_arquivo.run

# SUMÁRIO

- [**1. TIPOS DE VARIÁVEL**](#1-tipos-de-variável)
  - [1.1 DECLARAÇÃO](#11-declaração)
- [**2. ESTRUTURA DO CÓDIGO**](#2-estrutura-do-código)
- [**3. LENDO E ESCREVENDO**](#3-lendo-e-escrevendo)
- [**4. CODICIONAIS**](#4-codicionais)
  - [4.1 IF](#41-if)
  - [4.2 ELSE IF](#42-else-if)
  - [4.3 ELSE](#43-else)
- [**5. ESTRUTURAS DE REPETIÇÃO**](#5-estruturas-de-repetição)
  - [5.1 FOR](#51-for)
  - [5.2 WHILE](#52-while)
  - [5.3 DO WHILE](#53-do-while)
  - [5.4 BREAK](#54-break)

# **1. TIPOS DE VARIÁVEL**

Teremos os seguintes tipos de variáveis:

- **Int:** Para números inteiros.
- **Float:** Número real.
- **Double:** Número real muito grande.
- **Char:** É utilizado para armazenar caracteres, em geral letras, porém também serve para armazenar números, porém os mesmos não ficam operáveis.
- **Boolean:** Verdadeiro ou falso.
- **String:** São um conjunto de char, ou seja, em geral são utilizadas para armazenar palavras inteiras.
  - Strings são classes, e para utilizá-las devemos importar a biblioteca `string` .

## 1.1 DECLARAÇÃO

- Estrutura

```cpp
tipo_da_variavel nome_da_variavel = valor;
```

- Exemplo

```cpp
int a;
int a = 3;
float b;
float b = 2.134;
double c;
double c = 3.11233445;
char d;
char d = 'd';
bool e = false;
bool e = true;
string f;
string f = 'texto';
```

> Veja que as variáveis podem ou não terem seus valores pré-definidos.

# **2. ESTRUTURA DO CÓDIGO**

- Todo código em C++ precisa de uma função `main` para poder saber por onde iniciar o código.
- Todo código em C++ precisa, antes da função `main` utilizar o comando `using namespace std;`.
- Toda linha de código deve terminar com um `;`.
- Todo bloco de código deve estar entre chaves.

# **3. LENDO E ESCREVENDO**

Normalmente em um programa haverá a necessidade de interação entre usuário e máquina, e para isso precisamos efetuar entradas e saídas de informação. Para isso vamos utilizar uma biblioteca que se chama `iostream` que nada mais é do que uma biblioteca responsável por fazer a integração entre as entradas e saídas do pc com o programa.

No exemplo abaixo vamos utilizar o comando `cout` para mostrar uma mensagem qualquer e vamos utilizar o comando `cin` para receber um valor qualquer.

- Estrutura

```cpp
std::cout << "/* message */" << '\n';  // Forma 1
std::cout << "/* message 1*/" << "/* message 2*/" << nome_da_variavel<< '\n';  // Forma 2
std::cout << "/* message */" << endl;  // Forma 3
std::cout << "/* message */";  // Forma 4
std::cin >> /* nome_da_variavel */;
```

> - `/n`: pula uma linha
> - `endl`: pula uma linha
> - É completamente opcional colocar `std::` no inicio dos comandos `cout` e `cin`.

- Exemplo

```cpp
#include <iostream>
using namespace std;
int main(){
  int x = 3;
  std::cout << "o valor de x é: "<< x << '\n';
  std::cout << "Digite um novo valor para x: ";
  std::cin >> x;
  std::cout << "O novo valor de x é: "<< x << '\n';
  return 0;
}
```

- Saída <br>

```
o valor de x é: 3
Digite um novo valor para x: __ //ficará esperando digitar, vamos supor que digitamos 10
O novo valor de x é: 10
```

# **4. CODICIONAIS**

Temos aqui as condições:

- igual: ==
- maior: >
- menor: <
- maior ou igual: >=
- menor ou igual: <=
- diferente: <> ou !=

Também podemos utilizar multiplas condições, utilizando os operadores:

- ou: ||
- e: &&

Para indicar para o computador que queremos estabelecer uma condição utilizamos o comando `if`. Após o comando `if` ser utilizado podemos utilizar um outro comando, que seria o comando `else`.

## 4.1 IF

o comando `if` precisa ter na frente uma dada condição.

- Estrutura

```cpp
if (condição){
    // Código...
}
```

## 4.2 ELSE IF

Essa condição somente será vista caso a condição do `if` não seja atendida. Isso evita gasto computacional, pois se tivessemos dois `ifs` iriamos verificar duas condições diferentes, assim nós só nos preocuparemos com as condições seguintes caso a primeira seja invalida.

- Estrutura

```cpp
else if (condição){
    // Código...
}
```

## 4.3 ELSE

Engloba tudo que for o contrário das condições impostas no `if` e no `else if`. Logo não coloca-se condições para o comando else.

- Estrutura

```cpp
else{
    // Código...
}
```

- Exemplo

```cpp
#include <iostream>
using namespace std;
int main(){
  int x = 10;
  if (x>5){
    std::cout << "O valor de x é maior que 5" << '\n';
  }
  else if (x>8){
    std::cout << "O valor de x é maior que 8" << '\n';
  }
  else{
    std::cout << "O valor de x não atende as condições anteriores" << '\n';
  }
}
```

- Saída <br>

```
O valor de x é maior que 5
```

> OBS.: Veja que o mesmo a condição `x>8` sendo verdadeira ela não foi verificada, pois a condição do `if` já havia sido atendida.

# **5. ESTRUTURAS DE REPETIÇÃO**

Quando queremos que uma dada instrução seja repetida diversas vezes, nós chamamos as estruturas de repetição. São elas:

## 5.1 FOR

O for vai definir uma variação em um dado parâmetro, e só irá parar de executar quando esse parâmetro atingir uma dada condição, sendo que a cada interação algo acontece com esse parâmetro.

- Estrutura

```cpp
for(inicialização; condição; incremento){
    // Código...
}
```

- Exemplo:

```cpp
#include <iostream>
using namespace std;
int main(){
  int i;
  for (i=0; i<5; i++){
    std::cout << "o valor de i é: " << i << '\n';
  }
}
```

- Saída <br>

```
o valor de i é: 0
o valor de i é: 1
o valor de i é: 2
o valor de i é: 3
o valor de i é: 4
```

## 5.2 WHILE

Diferentemente do `for` o comando `while` tem como objetivo colocar apenas uma condição de parada, assim o loop vai parar somente quando algo dentro do código acontecer.

Veja bem, se tivermos definido que queremos que o loop pare quando x for igual a y, mas não sabemos quando isso ocorrerá, então precisamos de um while, pois o for nós temos que saber exatamente quantas interações serão necessárias para atingirmos o objetivo.

- Estrutura

```cpp
while(condição){
    // Código...
}
```

- Exemplo

```cpp
#include <iostream>
using namespace std;
int main(){
  int i = 0;
  while (i<5){
    std::cout << "o valor de i é: " << i << '\n';
    i++;
  }
}
```

- Saída <br>

```
o valor de i é: 0
o valor de i é: 1
o valor de i é: 2
o valor de i é: 3
o valor de i é: 4
```

## 5.3 DO WHILE

A diferença do `while` e do `do while` é que o `while` avalia a condição antes de executar o código, já o comando `do while` avalia a condição depois de executar o código.

- Estrutura

```cpp
do{
    // Código...
}while(condição);
```

Se utilizarmos o mesmo exemplo de antes, não vamos notar diferença no resultado.

- Exemplo 1

```cpp
#include <iostream>
using namespace std;
int main(){
  int i = 0;
  do{
    std::cout << "o valor de i é: " << i << '\n';
    i++;
  }while(i<5);
}
```

- Saída 1 <br>

```
o valor de i é: 0
o valor de i é: 1
o valor de i é: 2
o valor de i é: 3
o valor de i é: 4
```

Porém se fizermos um código em que i inicia em 5, o código com `while` não iria ser executádo, pois a verificação acontece antes, já o código com `do while` seria executado, pois a verificação só ocorre depois.

- Exemplo 2: while

```cpp
#include <iostream>
using namespace std;
int main(){
  int i = 5;
  while(i<5){
    std::cout << "o valor de i é: " << i << '\n';
    i++;
  }
  std::cout << "fora do while o valor de i é: " << i << '\n';
}
```

- Saída 2: while <br>

```
fora do while o valor de i é: 5
```

- Exemplo 2: do while

```cpp
#include <iostream>
using namespace std;
int main(){
  int i = 5;
  do{
    std::cout << "o valor de i é: " << i << '\n';
    i++;
  }while(i<5);
}
```

- Saída 2: do while <br>

```
o valor de i é: 5
fora do do while o valor de i é: 6
```

Veja que no primeiro código não entramos dentro do loop, por isso o valor de i fora dele não foi alterado. Já no segundo bloco foi possível entrar no loop, porém veja que o valor de i foi alterado em apenas uma unidade, isso porque quando acabou o loop já foi identificado que o valor de i era maior do que 5, então o loop não foi executado novamente.

## 5.4 BREAK

O comando break é utilizado para parar a execução de um loop mediante uma condição específica. Ou seja, ele vai dentro de um `if`.

- Estrutura

```cpp
while(Condição){
    // Código...
    if(Condição){
        break;
    }
}
```

- Exemplo

```cpp
#include <iostream>
using namespace std;
int main(){
  int a = 0;
  int b = 5;
  std::cout << "iniciando o loop while" << '\n';

  while (1) {
    std::cout << "Valor de a é: " << a <<'\n';
    a++;
    if (a==b){
      break;
    }
  }

  std::cout << "Iniciando o loop for" << '\n';
  a = 0;
  for(;;){
    std::cout << "Valor de a é: " << a << '\n';
    a++;
    if (a==b){
      break;
    }
  }
}
```

> OBS.: Opções para loop infinito

```cpp
while(1)
for(;;)
```

- Saída <br>

```
iniciando o loop while
Valor de a é: 0
Valor de a é: 1
Valor de a é: 2
Valor de a é: 3
Valor de a é: 4
Iniciando o loop for
Valor de a é: 0
Valor de a é: 1
Valor de a é: 2
Valor de a é: 3
Valor de a é: 4
```
