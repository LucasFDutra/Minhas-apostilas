# Apostila de Java

Autor: Lucas Felipe Dutra

**ANTES DE QUALQUER COISA, VEJA ESSE VIDEO [AQUI](https://www.youtube.com/watch?v=9w3o9NHXqu0&list=PLMdYygf53DP5Sc6yFYs6ZmjsuuA2fu0TK) PARA APRENDER MAIS SOBRE CLEAN CODE**

- [Sobre o java:](https://www.youtube.com/watch?v=sZAxLRMxEUo&list=PLVc5bWuiFQ8GgKm5m0cZE6E02amJho94o&index=28)

# SUMÁRIO

- [**1. FERRAMENTAS**](#1-ferramentas)
- [**2. IDENTAÇÃO**](#2-identação)
- [**3. INTERAÇÃO USUÁRIO/SOFTWARE**](#3-interação-usuáriosoftware)
  - [3.1 RECEBER ENTRADA](#31-receber-entrada)
  - [3.2 IMPRIMIR NA TELA](#32-imprimir-na-tela)
  - [3.3 UTILIZANDO O SWING](#33-utilizando-o-swing)
- [**4. CONDICIONAIS**](#4-condicionais)
  - [4.1 IF](#41-if)
  - [4.2 ELSE IF](#42-else-if)
  - [4.3 ELSE](#43-else)
  - [4.4 OPERADORES](#44-operadores)
  - [4.5 STRINGS](#45-strings)
  - [4.6 UTILIZANDO O SWING](#46-utilizando-o-swing)
- [**5. ESTRUTURAS DE REPETIÇÃO**](#5-estruturas-de-repetição)
  - [5.1 FOR](#51-for)
  - [5.2 WHILE](#52-while)
  - [5.3 DO WHILE](#53-do-while)
  - [5.4 BREAK](#54-break)
- [**6. Arrays**](#6-arrays)
  - [6.1 LOOP FOR COM UM ARRAY](#61-loop-for-com-um-array)
  - [6.2 MÉTODO ARRAY](#62-método-array)
    - [**6.2.1 Ordenação**](#621-ordenação)
    - [**6.2.2 Preenchimento automático**](#622-preenchimento-automático)
- [**7. Array List**](#7-array-list)
  - [7.1 DECLARAÇÃO](#71-declaração)
  - [7.2 INSERINDO NOVOS TERMOS](#72-inserindo-novos-termos)
  - [7.3 ACESSAR UM TERMO](#73-acessar-um-termo)
  - [7.4 MUDANDO UM TERMO](#74-mudando-um-termo)
  - [7.5 EXTENDENDO UM ARRAY](#75-extendendo-um-array)
  - [7.6 INSERINDO ELEMENTO EM UMA POSIÇÃO ESPECÍFICA](#76-inserindo-elemento-em-uma-posição-específica)
  - [7.7 EXCLUINDO TERMO](#77-excluindo-termo)
  - [7.8 LIMPANDO ARRAY](#78-limpando-array)
  - [7.9 OBTER ÍNDICE DE UM ELEMENTO](#79-obter-índice-de-um-elemento)
  - [7.10 COPIANDO UM ARRAY](#710-copiando-um-array)
  - [7.11 RETORNAR O TAMANHO DE UM ARRAY](#711-retornar-o-tamanho-de-um-array)
  - [7.12 ORDENAR UM ARRAY](#712-ordenar-um-array)
  - [7.13 VERIFICAR A EXISTENCIA DE UM ELEMENTO](#713-verificar-a-existencia-de-um-elemento)
- [**8. MÉTODOS/FUNÇÕES**](#8-métodosfunções)
- [**9. POO**](#9-poo)
  - [9.1 CLASSES](#91-classes)
  - [9.2 VISIBILIDADE](#92-visibilidade)
  - [9.3 MÉTODOS GETTER, SETTERS E CONSTRUCTS](#93-métodos-getter,-setters-e-constructs)
  - [9.4 ENCAPSULAMENTO](#94-encapsulamento)
  - [9.5 RELACIONAMENTO ENTRE CLASSES](#95-relacionamento-entre-classes)
  - [9.6 HERANÇA](#96-herança)
    - [**9.6.1 Tipos de classes e métodos**](#961-tipos-de-classes-e-métodos)
  - [9.7 POLIMORFISMO](#97-polimorfismo)
    - [**9.7.1 Polimorfismo de sobreposição**](#971-polimorfismo-de-sobreposição)
    - [**9.7.2 Polimorfismo de sobrecarga**](#972-polimorfismo-de-sobrecarga)

# **1. FERRAMENTAS**

- [Intellij IDEA](https://www.jetbrains.com/idea/)
- [Curso de Java para Iniciantes - Grátis, Completo e com Certificado - Curso em Video](https://www.youtube.com/playlist?list=PLHz_AreHm4dkI2ZdjTwZA4mPMxWTfNSpR)
- [Curso de POO Java (Programação Orientada a Objetos) - Curso em Video](https://www.youtube.com/playlist?list=PLHz_AreHm4dkqe2aR0tQK74m8SFe-aGsY)

# **2. IDENTAÇÃO**

Veja algumas caracteristicas do Java:

- **Comentários:** Para criar comentários utilize o caracter '//'.

- **Fim de comando:** O final de um comando é identificado quando é colocado `;`.

```Java
println("ola"); // comando 1
print("mundo"); // comando 2
```

- **Bloco de código** Um bloco de código é representado pelo caracter `{}`.

```Java
public class Main{
  public static void main(String[] args){
    System.out.println("Hello World");
  }
}
```

- **Variáveis:** Teremos os seguintes tipos de variáveis:

  - Int
  - Float
  - Char
  - Boolean
  - String
  - Double

  - Exemplo:

    ```Java
    int a = 3;
    float b = 3.1415;
    char c = 'c';
    boolean d = false;
    String e = "palavra";
    double f = 3.14159265;
    ```

  - **Tamanho da string:**

    - `nome_da_string.length`

  - **Conversão de variáveis:** Como não podemos efeturar atribuições entre variáveis de tipos diferentes, muitas vezes torna-se necessário efetuar a conversão de tipos, para isso utilizamos:
  - Qualquer coisa para `String`:
    - `s = TipoS.toString(a)`
  - String para qualquer coisa:

    - `x = Tipo.perseTipo(s)`

    - Exemplo:

      ```Java
      public class Main {
        public static void main(String[] args) {
          String a = "30";
          int b;
          float c;
          double d;

          b = Integer.parseInt(a);
          c = Float.parseFloat(a);
          d = Double.parseDouble(a);

          System.out.println(a);
          System.out.println(b);
          System.out.println(c);
          System.out.println(d);
        }
      }
      ```

    - Saída:
      ```Java
      30
      30
      30.0
      30.0
      ```

> OBS.: Strigns não são tipos primitivos, elas são classes.

# **3. INTERAÇÃO USUÁRIO/SOFTWARE**

## 3.1 RECEBER ENTRADA

Para receber uma entrada utiliza-se o comando `readLine`. E para utilizar esse comando precisamos importar a classe `java.util.Scanner`.

- Exemplo:

  ```Java
  import java.util.Scanner;

  public class Main {
      public static void main(String[] args) {
          Scanner teclado = new Scanner(System.in);

          String nome;
          int idade;

          System.out.println("Digite o nome");
          nome = teclado.nextLine();
          System.out.println("Digite a idade");
          idade = teclado.nextInt();
          System.out.printf("A idade de %s é de: %d \n", nome, idade);
      }
  }
  ```

- Saída:
  ```Java
  Digite o nome
  lucas
  Digite a idade
  24
  A idade de lucas é de: 24
  ```

## 3.2 IMPRIMIR NA TELA

Para exibir algo na tela utiliza-se o comando `println`, ou `printf`. A diferença entre eles é que o `println` pula uma linha após a exibição.

- Exemplo:

  ```Java
  public class Main {
      public static void main(String[] args) {
          String nome = "lucas";
          int idade = 24;

          System.out.printf("A idade de %s é de: %d \n", nome, idade);
          System.out.println("A idade de "+nome+" é de: "+idade);
      }
  }
  ```

- Saída:
  ```Java
  A idade de lucas é de: 24
  A idade de lucas é de: 24
  ```

> OBS.: `println` não aceita %s, %d, %f...

## 3.3 UTILIZANDO O SWING

No swing vamos criar a janela mostrada na figura abaixo.

![](https://github.com/LucasFDutra/Minha-Apostila-De-Linguagem-Java/blob/master/Imagens/Figura_01.gif?raw=true)

O objetivo desse programa é fazer a soma entre os valores que estão dentro das caixas de texto e exibir o resultado após apertar o botão.

Para pegarmos o que está escrito dentro das caixas de texto vamos utilizar o comando `getText()`, e para exibir no label vamos utilizar `setText`.

Todo o código vai poder ser visto no [Programa 01](https://github.com/LucasFDutra/Minha-Apostila-De-Linguagem-Java/tree/master/Programas/Programa%2001).

# **4. CONDICIONAIS**

## 4.1 IF

```Java
if (condição){
  // Código...
}
```

## 4.2 ELSE IF

É uma condição que só é analisada caso a condição em `if` não seja atendida.

```Java
else if (condição){
  // Código...
}
```

## 4.3 ELSE

Engloba tudo que for o contrário das condições impostas em `if` e `else if`.

```Java
else{
  // Código...
}
```

## 4.4 OPERADORES

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

- Exemplo:

  ```Java
  public class Main {
      public static void main(String[] args) {
          int a = 1;
          int b = 2;

          if (a == b){
              System.out.printf("'a' é igual à 'b'");
          }
          else if (a > b){
              System.out.printf("'a' é maior do que 'b'");
          }
          else if(a==2 || a==3){
              System.out.printf("'a' é igual a 2 ou igual a 3");
          }
          else if(a==2 && b==3){
              System.out.printf("'a' é igual a 2 e 'b' é igual a 3");
          }
          else{
              System.out.printf("'a' é diferente de 'b'");
          }
      }
  }
  ```

- Saída:
  ```Java
  'a' é diferente de 'b'
  ```

## 4.5 STRINGS

Para comparar se duas strings são iguais não basta apenas utilizar o operar `==`, isso é porque strings são classes, logo o que temos são objetos string e não variáveis. Então para efetuarmos acomparação entre duas strings temos que utilizar o comando `.equals`.

- Exemplo:

  ```Java
  public class Main {
      public static void main(String[] args) {
          String a = "a";
          String b = "b";

          if (a.equals(b)){
              System.out.printf("'a' é igual a 'b'");
          }
          else{
              System.out.printf("'a' é diferente de 'b'");
          }
      }
  }
  ```

- Saída:
  ```Java
  'a' é diferente de 'b'
  ```

## 4.6 UTILIZANDO O SWING

No swing vamos criar a janela mostrada na figura abaixo.

![](https://github.com/LucasFDutra/Minha-Apostila-De-Linguagem-Java/blob/master/Imagens/Figura_02.gif?raw=true)

O objetivo desse programa é fazer a comparação entre o conteúdo das `textField` e mostar se são iguais ou não.

Todo o código vai poder ser visto no [Programa 02](https://github.com/LucasFDutra/Minha-Apostila-De-Linguagem-Java/tree/master/Programas/Programa%2002).

# **5. ESTRUTURAS DE REPETIÇÃO**

## 5.1 FOR

```Java
for(inicialização; condição; incremento){
    // Código...
}
```

- Exemplo:
  ```Java
  public class Main {
      public static void main(String[] args) {
          int i;
          for (i=0; i<10; i++){
              System.out.printf("%d, ", i);
          }
      }
  }
  ```
- Saída:
  ```Java
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
  ```

## 5.2 WHILE

```Java
while(condição){
  // Código...
}
```

- Exemplo:

  ```java
  public class Main {
      public static void main(String[] args) {
          int i = 0;
          while (i<10){
              System.out.printf("%d, ", i);
              i++;
          }
          System.out.printf("\nO valor de i após o while: %d", i);
      }
  }
  ```

- Saída:
  ```Java
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
  O valor de i após o while: 10
  ```

## 5.3 DO WHILE

A diferença entre o `do while` e `while` é que no `do while` o código é executado primeiro e depois que a condição é verificada.

```java
do{
  // Código...
}while(condição)
```

- Exemplo:

  ```java
  public class Main {
      public static void main(String[] args) {
          int i = 0;
          do {
              System.out.printf("%d, ", i);
              i++;
          }while (i<10);
          System.out.printf("\nO valor de i após o do While: %d", i);
      }
  }
  ```

- Saída:
  ```Java
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
  O valor de i após o do While: 10
  ```

## 5.4 BREAK

O comando `break` serve para interromper um loop caso alguma condição especial ocorra.

- Exemplo:
  ```java
  public class Main {
      public static void main(String[] args) {
          int i;
          for (i=0; i<10; i++){
              System.out.printf("%d, ", i);
              if (i==5){
                  break;
              }
          }
      }
  }
  ```
- Saída:
  ```Java
  0, 1, 2, 3, 4, 5,
  ```

# **6. Arrays**

```Java
tipo[] nome = {valores};
tipo[] nome;
tipo nome[] = {valores};
tipo nome[] = new tipo[tamanho];
```

- Exemplo 1:

  ```Java
  public class Main {
      public static void main(String[] args) {
          int[] array = {1,2,3,4};
          for (int i=0; i<array.length; i++){
              System.out.printf("%d, ", array[i]);
          }
      }
  }
  ```

- Saída:

  ```Java
  1, 2, 3, 4,
  ```

- Exemplo 2:

  ```Java
  public class Main {
      public static void main(String[] args) {
          int n[] = new int[4];
          for (int i=0; i<n.length; i++){
              n[i] = i;
          }

          for (int i=0; i<n.length; i++){
              System.out.printf("%d, ", n[i]);
          }
      }
  }
  ```

- Saída:
  ```Java
  0, 1, 2, 3
  ```

## 6.1 LOOP FOR COM UM ARRAY

```java
for (tipo i : array){
  // Código...
}
```

- Exemplo:

  ```Java
  public class Main {
      public static void main(String[] args) {
          int[] array = {1,2,3,4};
          for (int i : array){
              System.out.printf("%d, ", i);
          }
      }
  }
  ```

- Saída:
  ```Java
  1, 2, 3, 4,
  ```

## 6.2 MÉTODO ARRAY

### **6.2.1 Ordenação**

```Java
Arrays.sort(array);
```

- Exemplo:

  ```Java
  import java.util.Arrays;

  public class Main {
      public static void main(String[] args) {
          int n[] = {5, 1, 3, 4};
          Arrays.sort(n);
          for (int i=0; i<4; i++){
              System.out.printf("%d ", n[i]);
          }
      }
  }
  ```

- Saída:
  ```Java
  1 3 4 5
  ```

### **6.2.2 Preenchimento automático**

```Java
Arrays.fill(array, valor);
```

- Exemplo:

  ```Java
  import java.util.Arrays;

  public class Main {
      public static void main(String[] args) {
          int n[] = new int[5];
          Arrays.fill(n, 0);
          for (int i=0; i<5; i++){
              System.out.printf("%d ", n[0]);
          }
      }
  }
  ```

- Saída:
  ```Java
  0 0 0 0 0
  ```

# **7. Array List**

Array list é uma classe do java, um objeto array list permite que não seja necessário defirmos o array ao inicializá-lo, permitindo que adicionemos elementos à ele conforme necessário. Essa capacidade nos da uma margem muito grande para trabalharmos.

## 7.1 DECLARAÇÃO

```Java
ArrayList<tipo> array_name = new ArrayList<tipo>();
```

## 7.2 INSERINDO NOVOS TERMOS

```Java
array.add(valor);
```

## 7.3 ACESSAR UM TERMO

```Java
array.get(posição, valor);
```

## 7.4 MUDANDO UM TERMO

```Java
array.set(posição);
```

## 7.5 EXTENDENDO UM ARRAY

```Java
array_1.addAll(array_2);
```

## 7.6 INSERINDO ELEMENTO EM UMA POSIÇÃO ESPECÍFICA

```Java
array.add(index = posição, element = valor);
```

## 7.7 EXCLUINDO TERMO

```Java
array.remove(posição);
```

## 7.8 LIMPANDO ARRAY

```Java
array.clear();
```

## 7.9 OBTER ÍNDICE DE UM ELEMENTO

```Java
array.indexOf(termo);
```

## 7.10 COPIANDO UM ARRAY

```Java
novo_array.addAll(array); //meio na gambiarra
```

## 7.11 RETORNAR O TAMANHO DE UM ARRAY

```Java
array.size();
```

## 7.12 ORDENAR UM ARRAY

```Java
Collections.sort(array);
```

## 7.13 VERIFICAR A EXISTENCIA DE UM ELEMENTO

```Java
array.contains(termo);
```

> OBS.: Para utilizar o array list com o for, faz-se igual ao array normal.

- Exemplo:

  ```Java
  import java.util.ArrayList;
  import java.util.Collections;

  public class Main {
      public static void main(String[] args) {
          // Declaracão
          ArrayList<Integer> array_1 = new ArrayList<Integer>();
          ArrayList<Integer> array_2 = new ArrayList<Integer>();

          // Adicionando
          for (int i=0; i<10; i++){
              array_1.add(i);
          }

          // Acessando termo
          for (int i=0; i<array_1.size(); i++){
              System.out.printf("%d, ", array_1.get(i));
          }

          System.out.println();

          // Mudando termo
          array_1.set(0, 15);
          System.out.println("array_1: "+array_1);

          // Percorrendo em um for
          for (int i: array_1){
              System.out.printf("%d, ", i);
          }

          System.out.println();

          // Copiando array
          array_2.addAll(array_1);
          System.out.println("array_2: "+array_2);

          // Removendo termo
          array_1.remove(3);
          System.out.println("array_1: "+array_1);

          // Limpando array
          array_1.clear();
          System.out.println("array_1: "+array_1);

          // Obtendo indice de um elemento
          System.out.println("O elemento 3 está na posicão: "+array_2.indexOf(3));

          // Ordenando array
          Collections.sort(array_2);
          System.out.println("array_2: "+array_2);

          // Verificando existencia de um termo
          System.out.println("array_2 contem o elemento 3? "+array_2.contains(2));
      }
  }
  ```

- Saída:
  ```Java
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
  array_1: [15, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  15, 1, 2, 3, 4, 5, 6, 7, 8, 9,
  array_2: [15, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  array_1: [15, 1, 2, 4, 5, 6, 7, 8, 9]
  array_1: []
  O elemento 3 está na posicão: 3
  array_2: [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
  array_2 contem o elemento 3? true
  ```

> OBS.: Veja que não conseguimos acessar um termo de um array list utilizando `array[posição]`.

# **8. MÉTODOS/FUNÇÕES**

```Java
static tipo nome(parametros){
  // Código
}
```

- Exemplo:

  ```Java
  public class Main {
      static int soma(int a, int b){
          int s = a+b;
          return s;
      }
      public static void main(String[] args) {
          int s = soma(3, 4);
          System.out.println("o valor da soma foi: "+ s);
      }
  }
  ```

- Saída:
  ```Java
  o valor da soma foi: 7
  ```

# **9. POO**

Toda a base teorica para POO está na apostila de POO, que também foi escrita por mim. Então todo o conteúdo que colocarei aqui nessa apostila está baseado na teoría da apostila de POO, então abra ela ai também e acompanhe as duas juntas. A mesma está nesse [link](https://github.com/LucasFDutra/Minha-Apostila-De-POO).

## 9.1 CLASSES

Para criar uma classe, seguimos a seguinte estrutura:

```Java
visibilidade Class ClassName{
  // Atributos

  //Métodos
}
```

- Para chamar essa classe e instanciar um objeto a partir dela:

  ```Java
  ClassName objName = new ClassName();
  ```

- Para modificar os atributos desse novo objeto:

  ```Java
  objName.atributo = valor
  ```

  > OBS.: Se o valor for do tipo float, é necessário colocar um `f` na frente. Veja: `objName.atributo = 0.5f`. Ou então utiliza-se o type cast: `objName.atributo = (float) 0.5`

- Para executar um método desse objeto:
  ```Java
  objName.metodo();
  ```

Vamos utilizar de um exemplo para criar uma classe. Vamos criar a classe caneta, sendo que a classe caneta irá conter a seguinte estrutura:

```Java
Classe Caneta
  // Atributos
  modelo: String
  cor: String
  ponta: Real
  carga: Inteiro
  tampada: Lógico

  // Métodos
  Método status()
    Escreva ("Modelo: ", modelo)
    Escreva ("Cor: ", cor)
    Escreva ("Ponta: ", ponta)
    Escreva ("Carga: ", carga)
    Escreva ("Tampada: ", tampada)

  Método rabiscar()
    Se (tampada) então
      Escreva("ERRO")
    senão
      Escreva("Rabisco")

  Método tampar()
    tampada = Verdadeiro

  Método destampada()
    tampada = Falso
```

- Exemplo:

  - Arquivo Main

    ```Java
    public class Main {
        public static void main(String[] args) {
            // Instanciando o objeto caneta
            Caneta c1 = new Caneta();
            c1.cor = "Azul";
            c1.ponta = (float) 0.5;
            c1.tampada = false;

            // Vamos tampar a caneta
            c1.tampar();

            // Vamos rabiscar?? tem que dar erro, pois a caneta está tampada
            c1.rabiscar();

            // Vamos destampar e rabiscar
            c1.destampar();
            c1.rabiscar();

            // Vamos verificar o status da caneta
            c1.status();
        }
    }
    ```

  - Arquivo da classe Caneta

    ```Java
    public class Caneta {
        // Atributos
        String modelo;
        String cor;
        float ponta;
        int carga;
        boolean tampada;

        // Métodos
        void status(){
            System.out.println("------Status------");
            System.out.println("Modelo: "+ this.modelo);
            System.out.println("Cor: "+ this.cor);
            System.out.println("Ponta: "+ this.ponta);
            System.out.println("Carga: "+ this.carga);
            System.out.println("Tampada: "+ this.tampada);
        }

        void rabiscar(){
            if (this.tampada == true){
                System.out.println("ERRO");
            }
            else{
                System.out.println("Rabisco");
            }
        }

        void tampar(){
            this.tampada = true;
        }

        void destampar(){
            this.tampada = false;
        }
    }
    ```

- Saída:
  ```Java
  ERRO
  Rabisco
  ------Status------
  Modelo: null
  Cor: Azul
  Ponta: 0.5
  Carga: 0
  Tampada: false
  ```

> OBS.: Classes com letra maiúscula no inicio de cada palavra. Em Atributos e Métodos a primeira palavra é minúscula e o restante tem a primeira letra maiúscula. Exemplo de classe: `Banana`. Atributo: `corBanana`. Método: `pegarBanana`.

Algo bem importante é observar a existencia do `this` em nossa classe caneta. Ele é necessário pois se tivermos mais de um objeto precisamos saber de qual objeto estamos falando quando olhamos os seus atributos. É só pensar o seguinte, se tivermos uma caneta vermelha e uma azul, quando colocassemos para mostrar a cor da caneta sem falar de qual caneta estamos falando seria meio complicado né?

O `this` vem justamente para resolver esse problema, pois é como se ele fosse substituido pelo nome do objeto que chamou aquele método onde ele se encontra, logo pegaremo o atributo referente àquele objeto. Sendo assim quando lemos `this.cor` estamos lendo `c1.cor`.

## 9.2 VISIBILIDADE

As visibilidades do java são definidas como:

- public;
- private;
- protected.

Por padrão o java define a visibilidade como pública, ou seja, se não colocar nada na frente, ele já entende que é público.

Vamos para o exemplo da caneta, mais uma vez, mas dessa vez vamos definir as visibilidades.

```Java
Classe Caneta
  // Atributos
  Público modelo: String
  Público cor: String
  Privado ponta: Real
  Protegido carga: Inteiro
  Protegido tampada: Lógico

  // Métodos
  Privado Método status()
  Privado Método rabiscar()
  Protegido Método tampar()
  Protegido Método destampar()
```

- Exemplo:

  - Arquivo Main

    ```Java
    public class Main {
        public static void main(String[] args) {
            // Instanciando o objeto caneta
            Caneta c1 = new Caneta();

            // Definindo atributos
            c1.modelo = "Bic";
            c1.cor = "Azul";
            // c1.ponta = (float) 0.5; da erro, pois ponta é privada.
            c1.carga = 90; // permitido pelo java, pois carga é protegida.
            c1.tampada = false; // permitido pelo java, pois tampada é protegida.

            // Utilizando métodos
            c1.status(); // publico, logo funciona
            c1.rabiscar(); // publico, logo funciona
            // c1.tampar(); // privado, logo não funciona
            // c1.destampar(); // privado, logo não funciona
        }
    }
    ```

  - Arquivo da classe Caneta

    ```Java
    public class Caneta {
        // Atributos
        public String modelo;
        public String cor;
        private float ponta;
        protected int carga;
        protected boolean tampada;

        // Métodos
        public void status(){
            System.out.println("------Status------");
            System.out.println("Modelo: "+ this.modelo);
            System.out.println("Cor: "+ this.cor);
            System.out.println("Ponta: "+ this.ponta);
            System.out.println("Carga: "+ this.carga);
            System.out.println("Tampada: "+ this.tampada);
        }

        public void rabiscar(){
            if (this.tampada == true){
                System.out.println("ERRO");
            }
            else{
                System.out.println("Rabisco");
            }
        }

        private void tampar(){
            this.tampada = true;
        }

        private void destampar(){
            this.tampada = false;
        }
    }
    ```

- Saída:
  ```Java
  ------Status------
  Modelo: Bic
  Cor: Azul
  Ponta: 0.0
  Carga: 90
  Tampada: false
  Rabisco
  ```

Porém agora vamos fazer uma modificação no exemplo. Vamos definir que o atributo tampada é privado, ou seja, somente a classe pode utilizá-lo. Porém vamos definir que os métodos tampar e destampar são publicos.

Bem, o que vai acontecer, é que como somente a classe pode modificar um atributo privado, e os métodos em questão estão dentro da classe, eles vão poder modificar o atributo, e ao mesmo tempo eles podem ser acessados fora da classe pois são métodos publicos.

```Java
Classe Caneta
  // Atributos
  Público modelo: String
  Público cor: String
  Privado ponta: Real
  Protegido carga: Inteiro
  Protegido tampada: Lógico

  // Métodos
  Privado Método status()
  Privado Método rabiscar()
  Protegido Método tampada()
```

- Exemplo:

  - Arquivo Main

    ```Java
    public class Main {
        public static void main(String[] args) {
            // Instanciando o objeto caneta
            Caneta c1 = new Caneta();

            // Definindo atributos
            c1.modelo = "Bic";
            c1.cor = "Azul";
            // c1.ponta = (float) 0.5; da erro, pois ponta é privada.
            c1.carga = 90; // permitido pelo java, pois carga é protegida.
            // c1.tampada = false; // da erro, pois tampada é privada.

            // Utilizando métodos
            c1.tampar(); // publico, logo funciona
            c1.status(); // publico, logo funciona
            c1.destampar(); // publico, logo funciona
            c1.status(); // publico, logo funciona
            // c1.tampada(); // privado, logo não funciona
            // c1.destampar(); // privado, logo não funciona
        }
    }
    ```

  - Arquivo da classe Caneta

    ```Java
    public class Caneta {
        // Atributos
        public String modelo;
        public String cor;
        private float ponta;
        protected int carga;
        private boolean tampada;

        // Métodos
        public void status(){
            System.out.println("------Status------");
            System.out.println("Modelo: "+ this.modelo);
            System.out.println("Cor: "+ this.cor);
            System.out.println("Ponta: "+ this.ponta);
            System.out.println("Carga: "+ this.carga);
            System.out.println("Tampada: "+ this.tampada);
        }

        public void rabiscar(){
            if (this.tampada == true){
                System.out.println("ERRO");
            }
            else{
                System.out.println("Rabisco");
            }
        }

        public void tampar(){
            this.tampada = true;
        }

        public void destampar(){
            this.tampada = false;
        }
    }
    ```

- Saída:
  ```Java
  ------Status------
  Modelo: Bic
  Cor: Azul
  Ponta: 0.0
  Carga: 90
  Tampada: true
  ------Status------
  Modelo: Bic
  Cor: Azul
  Ponta: 0.0
  Carga: 90
  Tampada: false
  ```

Veja que da primeira chamada o atributo tampada estava true, e da segunda ele estava false. Ou seja, de forma indireta, através de métodos públicos, conseguimos modificar atributos privados.

De forma mais ilustrada, você é uma pessoa que possui acesso restrito à alguma coisa, porém você conhece alguém que tem acesso, então você pede pra essa pessoa fazer uma determinada tarefa nesse local restrito por você.

## 9.3 MÉTODOS GETTER, SETTERS E CONSTRUCTS

De uma olhada na apostila de POO para entender o que é cada um desses métodos. Mas entenda que eles vão funcionar com a mesma logica aplicada no exemplo anterior, em que modificavamos um atributo privado de forma indireta.

Vamos voltar ao exemplo da caneta, porém vamos torná-lo menor, deixando apenas dois atributos. E vamos definir dois métodos para cada atributo, são eles os métodos get e set de cada um. E obviamente criaremos o método construtor também. Veja a estrutura que teremos:

Uma coisa muito importante de frizar é que o método construtor possui exatamente o mesmo nome da classe. Isso não é obrigado, mas é o costumeiro.

```Java
Classe Caneta
  // Atributos
  Privado modelo: String
  Privado cor: String

  // Métodos
  Privado Método status()
  Público Método getModelo()
    retorna modelo
  Público Método setModelo(m: String)
    modelo = m
  Público Método getCor()
    retorna cor
  Público Método setCor(c: String)
    cor = c
  Público Método Caneta(m: String, c: String) // construtor
    setModelo(m)
    setCor(c)
```

- Exemplo:

  - Arquivo Main

    ```Java
    public class Main {
        public static void main(String[] args) {
            // Instanciando o objeto caneta
            Caneta c1 = new Caneta();

            c1.Caneta("Bic", "Azul"); // constroi o padrão
            c1.status(); // mostra o status

            c1.setModelo("Compactor"); // modifica o padrão
            c1.status(); // mostra o status

            System.out.println("-----Metodo getCor-------");
            System.out.println(c1.getCor()); // mostra o retorno de getCor
        }
    }
    ```

  - Arquivo da classe Caneta

    ```Java
    public class Caneta {
        // Atributos
        private String modelo;
        private String cor;

        // Métodos
        public void status(){
            System.out.println("-------Status------");
            System.out.println("Modelo: "+this.modelo);
            System.out.println("Cor: "+this.cor);
        }

        public String getModelo(){
            return this.modelo;
        }
        public void setModelo(String m){
            this.modelo = m;
        }

        public String getCor(){
            return this.cor;
        }
        public void setCor(String c){
            this.cor = c;
        }

        public void Caneta(String m, String c){
            setModelo(m);
            setCor(c);
        }
    }
    ```

- Saída:
  ```Java
  -------Status------
  Modelo: Bic
  Cor: Azul
  -------Status------
  Modelo: Compactor
  Cor: Azul
  -----Metodo getCor-------
  Azul
  ```

Um outro jeito de definir o contrutor é com ele sendo constante para todos os objetos. Ou seja, não precisamos passar parâmetros para ele. E definindo ele da forma que apresentarei abaixo, ele é executado assim que criamos o objeto, ou seja, não é necessário chamá-lo no main.

- Exemplo:

  - Arquivo Main

    ```Java
    public class Main {
        public static void main(String[] args) {
            // Instanciando o objeto caneta
            Caneta c1 = new Caneta();

            c1.status(); // mostra o status

            c1.setModelo("Compactor"); // modifica o padrão
            c1.status(); // mostra o status

            System.out.println("-----Metodo getCor-------");
            System.out.println(c1.getCor()); // mostra o retorno de getCor
        }
    }
    ```

  - Arquivo da classe Caneta

    ```Java
    public class Caneta {
        // Atributos
        private String modelo;
        private String cor;

        // Métodos
        public void status(){
            System.out.println("-------Status------");
            System.out.println("Modelo: "+this.modelo);
            System.out.println("Cor: "+this.cor);
        }

        public String getModelo(){
            return this.modelo;
        }
        public void setModelo(String m){
            this.modelo = m;
        }

        public String getCor(){
            return this.cor;
        }
        public void setCor(String c){
            this.cor = c;
        }

        public Caneta(){
            setModelo("Bic");
            setCor("Azul");
        }
    }
    ```

- Saída:
  ```Java
  -------Status------
  Modelo: Bic
  Cor: Azul
  -------Status------
  Modelo: Compactor
  Cor: Azul
  -----Metodo getCor-------
  Azul
  ```

> OBS.: **Veja que o método construtor OBRIGATORIAMENTE PRECISA TER O MESMO NOME DA CLASSE E NÃO PODE TER O `VOID`.**

O primeiro método que mostrei, passando os parâmetros para o construtor é bem melhor, pois podemos definir objetos com condições iniciais diferentes.

## 9.4 ENCAPSULAMENTO

Vamos utilizar o exemplo do controle remoto descrito na apostila de POO.

- Exemplo:

  - Arquivo Main

    ```Java
    public class Main {
        public static void main(String[] args) {
            ControleRemoto cr = new ControleRemoto();
            cr.ControleRemoto();

            System.out.println("#------Estado inicial------#");
            cr.abrirMenu();

            System.out.println("#----ligando o controle----#");
            cr.ligar();
            cr.abrirMenu();

            System.out.println("#----desligando controle---#");
            cr.desligar();
            cr.abrirMenu();

            System.out.println("#----ligando o controle----#");
            cr.ligar();
            cr.abrirMenu();

            System.out.println("#------fechando menu-------#");
            cr.fecharMenu();

            System.out.println("#----aumentando volume-----#");
            cr.maisVolume();
            cr.abrirMenu();

            System.out.println("#----diminuindo volume-----#");
            cr.menosVolume();
            cr.abrirMenu();

            System.out.println("#--------ligar mudo--------#");
            cr.ligarMudo();
            cr.abrirMenu();

            System.out.println("#------desligar mudo-------#");
            cr.desligarMudo();
            cr.abrirMenu();

            System.out.println("#--------dando play--------#");
            cr.play();
            cr.abrirMenu();

            System.out.println("#---------pausando---------#");
            cr.pause();
            cr.abrirMenu();
        }
    }
    ```

  - Arquivo Interface
    ```Java
    public interface Controlador {
        public abstract void ligar();
        public abstract void desligar();
        public abstract void abrirMenu();
        public abstract void fecharMenu();
        public abstract void maisVolume();
        public abstract void menosVolume();
        public abstract void ligarMudo();
        public abstract void desligarMudo();
        public abstract void play();
        public abstract void pause();
    }
    ```
  - Arquivo Classe

    ```Java
    public class ControleRemoto implements Controlador {
        // Atributos
        private int volume;
        private boolean ligado;
        private boolean tocando;

        // métodos especiais
        public void ControleRemoto(){
            this.setVolume(50);
            this.setLigado(false);
            this.setTocando(false);
        }

        public void setVolume(int v){
            this.volume = v;
        }
        public int getVolume(){
            return this.volume;
        }
        public void setLigado(boolean l){
          this.ligado = l;
        }
        public boolean getLigado(){
            return this.ligado;
        }
        public void setTocando(boolean t){
            this.tocando = t;
        }
        public boolean getTocando(){
            return this.tocando;
        }

        // Sobrepondo métodos abstratos
        @Override
        public void ligar() {
            this.setLigado(true);
        }

        @Override
        public void desligar() {
            this.setLigado(false);
        }

        @Override
        public void abrirMenu() {
            System.out.println("Está ligado? "+this.getLigado());
            System.out.println("Está tocando? "+getTocando());
            System.out.println("O volume é: "+this.getVolume());
        }

        @Override
        public void fecharMenu() {
            System.out.println("Fechando menu.");
        }

        @Override
        public void maisVolume() {
            if (this.getLigado()){
                this.setVolume(this.getVolume()+1);
            }
        }

        @Override
        public void menosVolume() {
            if (this.getLigado() && this.getVolume()>0){
                this.setVolume(this.getVolume()-1);
            }
        }

        @Override
        public void ligarMudo() {
            if (this.getLigado() && this.getVolume()>0){
                this.setVolume(0);
            }
        }

        @Override
        public void desligarMudo() {
            if (this.getLigado() && this.getVolume()==0){
                this.setVolume(50);
            }
        }

        @Override
        public void play() {
            if (this.getLigado() && !(getTocando())){
                this.setTocando(true);
            }
        }

        @Override
        public void pause() {
            if (this.getLigado() && getTocando()){
                this.setTocando(false);
            }
        }
    }
    ```

- Saída:
  ```Java
  #------Estado inicial------#
  Está ligado? false
  Está tocando? false
  O volume é: 50
  #----ligando o controle----#
  Está ligado? true
  Está tocando? false
  O volume é: 50
  #----desligando controle---#
  Está ligado? false
  Está tocando? false
  O volume é: 50
  #----ligando o controle----#
  Está ligado? true
  Está tocando? false
  O volume é: 50
  #------fechando menu-------#
  Fechando menu.
  #----aumentando volume-----#
  Está ligado? true
  Está tocando? false
  O volume é: 51
  #----diminuindo volume-----#
  Está ligado? true
  Está tocando? false
  O volume é: 50
  #--------ligar mudo--------#
  Está ligado? true
  Está tocando? false
  O volume é: 0
  #------desligar mudo-------#
  Está ligado? true
  Está tocando? false
  O volume é: 50
  #--------dando play--------#
  Está ligado? true
  Está tocando? true
  O volume é: 50
  #---------pausando---------#
  Está ligado? true
  Está tocando? false
  O volume é: 50
  ```

Veja que os getters e setters não precisavam ser publicos, isso porque eu fico mexendo neles pelos métodos abstratos, mas eu preferi manter eles como publicos.

> OBS.: `@Override` é utilizado para indicar que o método abaixo irá sobrepor um método já existente, com o mesmo nome (isso vai ficar melhor apresentado em herança).

## 9.5 RELACIONAMENTO ENTRE CLASSES

Quando temos uma determinada classe em que algum atributo é do tipo de outra classe. Um exemplo disso seria, uma classe Jogador de futebol, em que nossos objetos seriam os jogadores, e uma classe partida, que ocorre entre os jogadores.

No exemplo abaixo temos justamente isso, dois jogadores que possuem atributos, e que podem chutar a gol. E teremos uma partida com 10 chutes para cada, sendo que esses chutes podem resultar em gols. No final vamos obter o resultado da partida.

- Exemplo:

  - Arquivo Main

    ```Java
    public class Main {
        public static void main(String[] args) {
            Jogador jogador1 = new Jogador();
            Jogador jogador2 = new Jogador();

            jogador1.Jogador(1.80f, 75f, "Esquerda");
            jogador2.Jogador(1.90f, 85f, "Direita");

            Partida partida = new Partida();
            partida.jogar(jogador1, jogador2);
            partida.resultado();
        }
    }
    ```

  - Arquivo classe Jogador

    ```Java
    import java.util.Random;

    public class Jogador {
        Random r = new Random();

        // Atributos
        private float altura;
        private float peso;
        private String perna;

        // Métodos Especiais
        public void setAltura(float a){
            this.altura = a;
        }
        public float getAltura(){
            return this.altura;
        }

        public void setPeso(float p){
            this.peso = p;
        }
        public float getPeso(){
            return this.peso;
        }

        public void setPerna(String p){
            this.perna = p;
        }
        public String getPerna(){
            return this.perna;
        }

        public void Jogador(float a, float p, String pe){
            setAltura(a);
            setPeso(p);
            setPerna(pe);
        }

        // Métodos especificos
        public boolean chutar(){
            if (r.nextFloat() < 0.5){
                return false;
            }
            else{
                return true;
            }
        }
    }
    ```

  - Arquivo classe Partida

    ```Java
    public class Partida {
        // Atributos
        private Jogador jogador1;
        private Jogador jogador2;
        private int gols1;
        private int gols2;

        // Métodos especiais
        public void setJogador1(Jogador j1){
            this.jogador1 = j1;
        }
        public Jogador getJogador1(){
            return this.jogador1;
        }

        public void setJogador2(Jogador j2){
            this.jogador2 = j2;
        }
        public Jogador getJogador2(){
            return this.jogador2;
        }

        public void setGols1(int g){
            this.gols1 = g;
        }
        public int getGols1(){
            return this.gols1;
        }

        public void setGols2(int g){
            this.gols2 = g;
        }
        public int getGols2(){
            return this.gols2;
        }

        // Métos especificos
        public void jogar(Jogador j1, Jogador j2){
            this.setJogador1(j1);
            this.setJogador2(j2);

            for (int i=0; i<10; i++){
                if (j1.chutar()){ // chutar é um método do atributo j1
                    this.setGols1(this.getGols1() + 1);
                }
                if (j2.chutar()){
                    this.setGols2(this.getGols2() + 1);
                }
            }
        }

        public void resultado(){
            System.out.println("#-------Jogador 1---------#");
            System.out.println("Altura: "+this.jogador1.getAltura());
            System.out.println("Peso: "+this.jogador1.getPeso());
            System.out.println("Perna: "+this.jogador1.getPerna());

            System.out.println("#-------Jogador 2---------#");
            System.out.println("Altura: "+this.jogador2.getAltura());
            System.out.println("Peso: "+this.jogador2.getPeso());
            System.out.println("Perna: "+this.jogador2.getPerna());

            System.out.println("#--------Resultado--------#");
            System.out.println("Jogador 1 - Gols: "+this.getGols1());
            System.out.println("Jogador 2 - Gols: "+this.getGols2());

            if (this.getGols1() > this.getGols2()){
                System.out.println("Jogador 1 venceu");
            }
            else if (this.getGols1() == this.getGols2()){
                System.out.println("empate");
            }
            else{
                System.out.println("Jogador 2 venceu");
            }
        }

    }
    ```

- Saída
  ```Java
  #-------Jogador 1---------#
  Altura: 1.8
  Peso: 75.0
  Perna: Esquerda
  #-------Jogador 2---------#
  Altura: 1.9
  Peso: 85.0
  Perna: Direita
  #--------Resultado--------#
  Jogador 1 - Gols: 5
  Jogador 2 - Gols: 2
  Jogador 1 venceu
  ```

Veja que por meu atributo ser uma classe, ele possui métodos próprios. Veja que o que fizemos para utilizar os jogadores em uma outra classe, foi exatamente a mesma coisa que fazemos com strings (pois strings são classes).

## 9.6 HERANÇA

A herança permite basear uma nova classe na definição de uma outra classe previamente existente.

No exemplo abaixo teremos as classes aluno e professor sendo filhas da classe pessoa.

- Exemplo:

  - Arquivo Main

    ```Java
    public class Main {
        public static void main(String[] args) {
            // instanciando
            Pessoa pessoa = new Pessoa();
            Aluno aluno = new Aluno();
            Professor professor = new Professor();

            // construindo
            pessoa.Pessoa("João", 20, "Masculino");
            aluno.Aluno(1, "Engenharia", "Carlos", 19, "Masculino");
            professor.Professor("Física", 13000, "Clara", 35, "Feminino");

            // Utilizando métodos para pessoa
            System.out.println("#----------Pessoa-----------#");
            System.out.println("Nome: "+pessoa.getNome());
            System.out.println("Idade: "+pessoa.getIdade());
            System.out.println("Sexo: "+pessoa.getSexo());
            System.out.println("Fez aniversário");
            pessoa.fazerAniversário();
            System.out.println("Idade: "+pessoa.getIdade());
            System.out.println();

            // Utilizando métodos para aluno
            System.out.println("#-----------aluno-----------#");
            System.out.println("Nome: "+aluno.getNome());
            System.out.println("Idade: "+aluno.getIdade());
            System.out.println("Sexo: "+aluno.getSexo());
            System.out.println("Matricula: "+aluno.getMatricula());
            System.out.println("Curso: "+aluno.getCurso());
            System.out.println("Fez aniversário");
            aluno.fazerAniversário();
            System.out.println("Idade de aluno: "+aluno.getIdade());
            System.out.println("fechando matricula");
            aluno.cancelarMatricula();
            System.out.println();

            // utlizando métodos para professor
            System.out.println("#---------Professor---------#");
            System.out.println("Nome: "+professor.getNome());
            System.out.println("Idade: "+professor.getIdade());
            System.out.println("Sexo: "+professor.getSexo());
            System.out.println("Especialidade: "+professor.getEspecialidade());
            System.out.println("Salário: "+professor.getSalario());
            System.out.println("Fez aniversário");
            professor.fazerAniversário();
            System.out.println("Idade de aluno: "+professor.getIdade());
            System.out.println("Aumentoando salário");
            professor.receberAumento(1000);
        }
    }
    ```

  - Arquivo Pessoa

    ```Java
    public class Pessoa {
        // Atributos
        private String nome;
        private int idade;
        private String sexo;

        // métodos especiais
        public void setNome(String n){
            this.nome = n;
        }
        public String getNome(){
            return this.nome;
        }

        public void setIdade(int i){
            this.idade = i;
        }
        public int getIdade(){
            return this.idade;
        }

        public void setSexo(String s){
            this.sexo = s;
        }
        public String getSexo(){
            return this.sexo;
        }

        // método construtor
        public void Pessoa(String n, int i, String s){
            this.setNome(n);
            this.setIdade(i);
            this.setSexo(s);
        }

        // métodos específicos
        public void fazerAniversário(){
            System.out.println("Parabéns para: "+this.getNome());
            this.setIdade(this.getIdade() + 1);
        }
    }
    ```

  - Arquivo Aluno

    ```Java
    public class Aluno extends Pessoa {
        // Atributos
        private int matricula;
        private String curso;

        // Métodos especiais
        public void setMatricula(int m){
            this.matricula = m;
        }
        public int getMatricula(){
            return this.matricula;
        }

        public void setCurso(String c){
            this.curso = c;
        }
        public String getCurso(){
            return this.curso;
        }

        // Método construtor
        public void Aluno(int m, String c, String n, int i, String s){
            this.setCurso(c);
            this.setMatricula(m);
            this.Pessoa(n, i, s);
        }

        // Métodos específicos
        public void cancelarMatricula(){
            System.out.println(this.getNome()+" cancelou a matricula");
        }
    }
    ```

  - Arquivo Professor

    ```Java
    public class Professor extends Pessoa{
        // Atributos
        private String especialidade;
        private float salario;

        // Métodos especiais
        public void setEspecialidade(String e){
            this.especialidade = e;
        }
        public String getEspecialidade(){
            return this.especialidade;
        }

        public void setSalario(float s){
            this.salario = s;
        }
        public float getSalario(){
            return this.salario;
        }

        // Método construtor
        public void Professor(String e, float sa, String n, int i, String s){
            this.setEspecialidade(e);
            this.setSalario(sa);
            this.Pessoa(n, i, s);
        }

        // Métodos específicos
        public void receberAumento(float aumento){
            System.out.println(this.getNome()+" recebeu aumento");
            this.setSalario(this.getSalario() + aumento);
            System.out.println("Seu salário é de: "+this.getSalario());
        }
    }
    ```

- Saída

  ```Java
  #----------Pessoa-----------#
  Nome: João
  Idade: 20
  Sexo: Masculino
  Fez aniversário
  Parabéns para: João
  Idade: 21

  #-----------aluno-----------#
  Nome: Carlos
  Idade: 19
  Sexo: Masculino
  Matricula: 1
  Curso: Engenharia
  Fez aniversário
  Parabéns para: Carlos
  Idade de aluno: 20
  fechando matricula
  Carlos cancelou a matricula

  #---------Professor---------#
  Nome: Clara
  Idade: 35
  Sexo: Feminino
  Especialidade: Física
  Salário: 13000.0
  Fez aniversário
  Parabéns para: Clara
  Idade de aluno: 36
  Aumentoando salário
  Clara recebeu aumento
  Seu salário é de: 14000.0
  ```

### **9.6.1 Tipos de classes e métodos**

- Classe abstrata: Não pode ser instanciada, só pode servir como progenitora (mãe).
  - Ou seja, se tentarmos criar um objeto a partir de uma classe abstrata vai dar ruim.
- Método abstrato: Declarado, mas não implementado na progenitora.
  - Foi exatamente o que fizemos em interface. Nós só dizemos que ele existe e ele será sobreposto na classe filha.
- Classe final: Não pode ser herdada por outra classe.
  - Ou seja, ela é uma folha na árvore de herança. Pois nenhuma outra classe herdará dela.
- Método final: Não pode ser sobreposto pelas suas sub-classes. Obrigatoriamente herdado.
  - Ou seja, ela pode ser herdada por alguém, mas não pode ter sua função alterada.

Vamos manter o exemplo da pessoa, aluno e professor para exemplificar. Vamos definir que a classe pessoa é abstrata, assim não podemos criar pessoas só pessoas, elas tem que fazer alguma coisa. E também vamos dizer que o método fazerAniversário é um método final, afinal de contas não faz sentido mudarmos a forma com que se faz aniversário, acredito que seja igual pra qualquer pessoa. E vamos também acressentar duas classes netas, as duas vindas de aluno, sendo que uma é do aluno bolsista e a outra é do aluno não bolsista. E assim vamos acressentar o atributo mensalidade para o aluno.

- Exemplo:

  - Arquivo Main

    ```Java
    public class Main {
        public static void main(String[] args) {
            // instanciando
            AlunoNaoBolsista aluno_n = new AlunoNaoBolsista();
            AlunoBolsista aluno_b = new AlunoBolsista();
            Professor professor = new Professor();

            // construindo
            aluno_n.Aluno(1, "Engenharia", "Carlos", 19, "Masculino", 1000);
            aluno_b.AlunoBolsista(80, 2, "Engenharia", "Antonio", 21, "Masculino", 1000);
            professor.Professor("Física", 13000, "Clara", 35, "Feminino");

            // Utilizando métodos para aluno não bolsista
            System.out.println("#----aluno não bolsista-----#");
            System.out.println("Nome: "+aluno_n.getNome());
            System.out.println("Idade: "+aluno_n.getIdade());
            System.out.println("Sexo: "+aluno_n.getSexo());
            System.out.println("Matricula: "+aluno_n.getMatricula());
            System.out.println("Curso: "+aluno_n.getCurso());
            System.out.println("Mensalidade: "+aluno_n.getMensalidade());
            System.out.println("Fez aniversário");
            aluno_n.fazerAniversário();
            System.out.println("Idade de aluno: "+aluno_n.getIdade());
            System.out.println("Pagando mensalidade");
            aluno_n.pagarMensalidade();
            System.out.println("fechando matricula");
            aluno_n.cancelarMatricula();
            System.out.println();

            // Utilizando métodos para o aluno bolsista
            System.out.println("#-------aluno bolsista------#");
            System.out.println("Nome: "+aluno_b.getNome());
            System.out.println("Idade: "+aluno_b.getIdade());
            System.out.println("Sexo: "+aluno_b.getSexo());
            System.out.println("Matricula: "+aluno_b.getMatricula());
            System.out.println("Curso: "+aluno_b.getCurso());
            System.out.println("Mensalidade: "+aluno_b.getMensalidade());
            System.out.println("Bolsa: "+aluno_b.getBolsa());
            System.out.println("Fez aniversário");
            aluno_b.fazerAniversário();
            System.out.println("Idade de aluno: "+aluno_b.getIdade());
            System.out.println("Pagando mensalidade");
            aluno_b.pagarMensalidade();
            System.out.println("fechando matricula");
            aluno_b.cancelarMatricula();
            System.out.println();

            // utlizando métodos para professor
            System.out.println("#---------Professor---------#");
            System.out.println("Nome: "+professor.getNome());
            System.out.println("Idade: "+professor.getIdade());
            System.out.println("Sexo: "+professor.getSexo());
            System.out.println("Especialidade: "+professor.getEspecialidade());
            System.out.println("Salário: "+professor.getSalario());
            System.out.println("Fez aniversário");
            professor.fazerAniversário();
            System.out.println("Idade de aluno: "+professor.getIdade());
            System.out.println("Aumentoando salário");
            professor.receberAumento(1000);
        }
    }
    ```

  - Arquivo Pessoa

    ```Java
    public abstract class Pessoa {
        // Atributos
        private String nome;
        private int idade;
        private String sexo;

        // métodos especiais
        public void setNome(String n){
            this.nome = n;
        }
        public String getNome(){
            return this.nome;
        }

        public void setIdade(int i){
            this.idade = i;
        }
        public int getIdade(){
            return this.idade;
        }

        public void setSexo(String s){
            this.sexo = s;
        }
        public String getSexo(){
            return this.sexo;
        }

        // método construtor
        public void Pessoa(String n, int i, String s){
            this.setNome(n);
            this.setIdade(i);
            this.setSexo(s);
        }

        // métodos específicos
        public final void fazerAniversário(){
            System.out.println("Parabéns para: "+this.getNome());
            this.setIdade(this.getIdade() + 1);
        }
    }
    ```

  - Arquivo Aluno
    ```Java
    public class Aluno extends Pessoa {
        // Atributos
        private int matricula;
        private String curso;
        private float mensalidade;
    ```


        // Métodos especiais
        public void setMatricula(int m){
            this.matricula = m;
        }
        public int getMatricula(){
            return this.matricula;
        }

        public void setCurso(String c){
            this.curso = c;
        }
        public String getCurso(){
            return this.curso;
        }

        public void setMensalidade(float m){
            this.mensalidade = m;
        }
        public float getMensalidade(){
            return this.mensalidade;
        }

        // Método construtor
        public void Aluno(int m, String c, String n, int i, String s, float mens){
            this.setCurso(c);
            this.setMatricula(m);
            this.setMensalidade(mens);;
            this.Pessoa(n, i, s);
        }

        // Métodos específicos
        public void cancelarMatricula(){
            System.out.println(this.getNome()+" cancelou a matricula");
        }
        public void pagarMensalidade(){
            System.out.println("mensalidade paga, valor: "+this.getMensalidade());
        }
    }
    ```

- Arquivo Professor

  ```Java
  public class Professor extends Pessoa{
      // Atributos
      private String especialidade;
      private float salario;

      // Métodos especiais
      public void setEspecialidade(String e){
          this.especialidade = e;
      }
      public String getEspecialidade(){
          return this.especialidade;
      }

      public void setSalario(float s){
          this.salario = s;
      }
      public float getSalario(){
          return this.salario;
      }

      // Método construtor
      public void Professor(String e, float sa, String n, int i, String s){
          this.setEspecialidade(e);
          this.setSalario(sa);
          this.Pessoa(n, i, s);
      }

      // Métodos específicos
      public void receberAumento(float aumento){
          System.out.println(this.getNome()+" recebeu aumento");
          this.setSalario(this.getSalario() + aumento);
          System.out.println("Seu salário é de: "+this.getSalario());
      }
  }
  ```

- Arquivo AlunoBolsista

  ```Java
  public class AlunoBolsista extends Aluno{
      private int bolsa;

      // Métodos especiais
      public void setBolsa(int b){
          this.bolsa = b;
      }
      public int getBolsa(){
          return this.bolsa;
      }

      // Método construtor
      public void AlunoBolsista(int b, int m, String c, String n, int i, String s, float mens){
          this.setBolsa(b);
          this.Aluno(m, c, n, i, s, mens);
      }

      // Métodos especificos
      @Override
      public void pagarMensalidade(){
          System.out.println("Desconto de "+this.getBolsa()+"%");
          float desconto = (float) this.getBolsa()/100;
          System.out.println("mensalidade paga, valor: "+(this.getMensalidade()*(1-desconto)));
      }
  }
  ```

- Arquivo AlunoNaoBolsista

  ```Java
  public class AlunoNaoBolsista extends Aluno{
      // Não escreve nada, pois ele apenas herda a classe aluno
      // e não faz nada além do que um aluno normal faz
  }
  ```

- Saída:

  ```Java
  #----aluno não bolsista-----#
  Nome: Carlos
  Idade: 19
  Sexo: Masculino
  Matricula: 1
  Curso: Engenharia
  Mensalidade: 1000.0
  Fez aniversário
  Parabéns para: Carlos
  Idade de aluno: 20
  Pagando mensalidade
  mensalidade paga, valor: 1000.0
  fechando matricula
  Carlos cancelou a matricula

  #-------aluno bolsista------#
  Nome: Antonio
  Idade: 21
  Sexo: Masculino
  Matricula: 2
  Curso: Engenharia
  Mensalidade: 1000.0
  Bolsa: 80
  Fez aniversário
  Parabéns para: Antonio
  Idade de aluno: 22
  Pagando mensalidade
  Desconto de 80%
  mensalidade paga, valor: 199.99998
  fechando matricula
  Antonio cancelou a matricula

  #---------Professor---------#
  Nome: Clara
  Idade: 35
  Sexo: Feminino
  Especialidade: Física
  Salário: 13000.0
  Fez aniversário
  Parabéns para: Clara
  Idade de aluno: 36
  Aumentoando salário
  Clara recebeu aumento
  Seu salário é de: 14000.0
  ```

## 9.7 POLIMORFISMO

O polimorfismo consiste em efetuar a mesma coisa de diversas formas. Isso voltado para orientação a objeto significa que um determinada classe irá executar a sua tarefa de diferentes formas dependendo do objeto que a está usando.

Temos dois tipos principais de polimorfismo, sendo eles, o polimorfismo de sobreposição e sobrecarga.

### **9.7.1 Polimorfismo de sobreposição**

O polimorfismo de sobreposição acontece quando substituimos um método de uma superclasse na sua subclasse, usando a mesma assinatura. Ou seja, nos utilizamos o mesmo nome para o método e os mesmos parâmetros.

> OBS.: A assinatura de uma classe consiste na quantidade de parâmetros e os tipos deles. Se duas classes com o mesmo nome utilizam os mesmos parâmetros e eles são do mesmo tipo, então elas emitem a mesma assinatura. Veja mais disso na apostila de POO.

- Exemplo:

  - Arquivo Main

    ```Java
    public class Main {
        public static void main(String[] args) {
            // Instanciando
            Mamifero mamifero = new Mamifero();
            Reptil reptil = new Reptil();
            Peixe peixe = new Peixe();
            Ave ave = new Ave();

            // Para Mamifero
            System.out.println("#---------Mamifero----------#");
            mamifero.locomover();
            mamifero.alimentar();
            mamifero.emitirSom();
            System.out.println();

            // Para Reptil
            System.out.println("#----------Reptil-----------#");
            reptil.locomover();
            reptil.alimentar();
            reptil.emitirSom();
            System.out.println();

            // Para peixe
            System.out.println("#-----------Peixe-----------#");
            peixe.locomover();
            peixe.alimentar();
            peixe.emitirSom();
            peixe.soltarBolha();
            System.out.println();

            // Para Ave
            System.out.println("#------------Ave------------#");
            ave.locomover();
            ave.alimentar();
            ave.emitirSom();
            ave.fazerNinho();
        }
    }
    ```

  - Arquivo Animal

    ```Java
    public abstract class Animal {
        //Atributos
        protected float peso;
        protected int idade;
        protected int menbros;

        //Métodos
        public abstract void locomover();
        public abstract void alimentar();
        public abstract void emitirSom();
    }
    ```

  - Arquivo Mamifero

    ```Java
    public class Mamifero extends Animal {
        // Atributos
        private String corPelo;

        // Métodos especiais
        public void setCorPelo(String cp){
            this.corPelo = cp;
        }
        public String getCorPelo(){
            return this.corPelo;
        }

        // Métodos proprios
        @Override
        public void locomover(){
          System.out.println("correndo");
        }

        @Override
        public void alimentar(){
          System.out.println("mamando");
        }

        @Override
        public void emitirSom(){
          System.out.println("som de mamífero");
        }
    }
    ```

  - Arquivo Reptil

    ```Java
    public class Reptil extends Animal{
        // Atributos
        private String corEscama;

        // Métodos Especiais
        public void setCorEscama(String ce){
            this.corEscama = ce;
        }
        public String getCorEscama(){
            return this.corEscama;
        }

        // Métodos
        @Override
        public void locomover(){
            System.out.println("rastejando");
        }

        @Override
        public void alimentar(){
            System.out.println("comendo Vegetais");
        }

        @Override
        public void emitirSom(){
            System.out.println("som de reptil");
        }
    }
    ```

  - Arquivo Peixe

    ```Java
    public class Peixe extends Animal {
        // Atributos
        public String corEscama;

        // Métodos especial
        public void setCorEscama(String ce){
            this.corEscama = ce;
        }
        public String getCorEscama(){
            return this.corEscama;
        }

        @Override
        public void locomover(){
            System.out.println("nadando");
        }

        @Override
        public void alimentar(){
            System.out.println("comendo substancias");
        }

        @Override
        public void emitirSom(){
            System.out.println("som de peixe");
        }

        public void soltarBolha(){
            System.out.println("soltou bolhas");
        }
    }
    ```

  - Arquivo Ave

    ```Java
    public class Ave extends Animal {
        // Atributos
        private String corPena;

        // Métodos especial
        public void setCorPena(String cp){
            this.corPena = cp;
        }
        public String petCorPena(){
            return this.corPena;
        }

        // Métodos
        @Override
        public void locomover(){
            System.out.println("voando");
        }

        @Override
        public void alimentar(){
            System.out.println("comando frutas");
        }

        @Override
        public void emitirSom(){
            System.out.println("som de ave");
        }

        public void fazerNinho(){
            System.out.println("construiu um ninho");
        }
    }
    ```

- Saída:

  ```Java
  #---------Mamifero----------#
  correndo
  mamando
  som de mamífero

  #----------Reptil-----------#
  rastejando
  comendo Vegetais
  som de reptil

  #-----------Peixe-----------#
  nadando
  comendo substancias
  som de peixe
  soltou bolhas

  #------------Ave------------#
  voando
  comando frutas
  som de ave
  construiu um ninho
  ```

### **9.7.2 Polimorfismo de sobrecarga**

No caso da sobreposição tinhamos que os métodos sobrepostos tinham a mesma assinatura do método contido na classe mãe, porém na sobrecarga estamos falando de um método da classe filha que se repete dentro da mesma, porém essas versões do método vão ter assinaturas diferentes.

- Exemplo

  - Arquivo Main

    ```Java
    public class Main {
        public static void main(String[] args) {
            Cachorro cachorro = new Cachorro();

            cachorro.alimentar();
            cachorro.reagir("ola");
            cachorro.reagir(15);
            cachorro.reagir(true);
            cachorro.reagir(5, 30);
        }
    }
    ```

  - Arquivo Mamifero

    ```Java
    public abstract class Mamifero {
        public abstract void alimentar();
    }
    ```

  - Arquivo Cachorro

    ```Java
    public class Cachorro extends Mamifero {
        @Override
        public void alimentar(){
            System.out.println("Comendo");
        }

        public void reagir(String frase){
            if (frase.equals("olá")){
                System.out.println("Abana o rabo alegre");
            }
            else{
                System.out.println("Abana o rabo triste");
            }
        }
        public void reagir(int hora){
            if (hora < 12){
                System.out.println("Feliz");
            }
            else{
                System.out.println("Mais feliz");
            }
        }
        public void reagir(boolean dono){ // se é ou não o dono que se aproxima
            if (dono){
                System.out.println("Felizão");
            }
            else{
                System.out.println("triste");
            }
        }
        public void reagir(int idade, int peso){
            if (idade < 10 && peso < 45){
                System.out.println("Feliz");
            }
            else{
                System.out.println("Feliz de mais");
            }
        }
    }
    ```

  - Saída
    ```Java
    Comendo
    Abana o rabo triste
    Mais feliz
    Felizão
    Feliz
    ```
