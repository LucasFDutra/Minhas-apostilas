# Apostila de PROGRAMAÇÃO ORIENTADA A OBJETO - CONCEITOS BÁSICOS

Autor: Lucas Felipe Dutra

**ANTES DE QUALQUER COISA, VEJA ESSE VIDEO [AQUI](https://www.youtube.com/watch?v=9w3o9NHXqu0&list=PLMdYygf53DP5Sc6yFYs6ZmjsuuA2fu0TK) PARA APRENDER MAIS SOBRE CLEAN CODE**

O objetivo desse material é servir de suporte para qualquer linguagem orientada a objeto. Então ele é apenas teórico, então escolha alguma linguagem e utilize esse material para te guiar na teoria.

> OBS.: Apenas a linguagem java foi feita leguindo a risca esse material, mas a ideia e modificar o restante para que eles se adequem a esse material.

- [Sobre POO](https://www.youtube.com/watch?v=QY0Kdg83orY&list=PLVc5bWuiFQ8GgKm5m0cZE6E02amJho94o&index=38)

## Material para consulta

- [Curso de POO Java (Programação Orientada a Objetos) - Curso em Video](https://www.youtube.com/playlist?list=PLHz_AreHm4dkqe2aR0tQK74m8SFe-aGsY)

# SUMÁRIO

- [**1 DEFINIÇÕES BÁSICAS**](#1-definições-básicas)
- [**2. CLASSES**](#2-classes)
- [**3. ABSTRAÇÃO**](#3-abstração)
- [**4. VISIBILIDADE**](#4-visibilidade)
- [**5. MÉTODOS ESPECIAIS**](#5-métodos-especiais)
- [**6. ENCAPSULAMENTO**](#6-encapsulamento)
  - [6.1 INTERFACE](#61-interface)
- [**7. RELACIONAMENTO ENTRE CLASSES**](#7-relacionamento-entre-classes)
- [**8. HERANÇA**](#8-herança)
  - [8.1 TIPOS DE CLASSES E MÉTODOS](#81-tipos-de-classes-e-métodos)
- [**9. POLIMORFISMO**](#9-polimorfismo)
  - [9.1 POLIMORFISMO DE SOBREPOSIÇÃO](#91-polimorfismo-de-sobreposição)
  - [9.2 POLIMORFISMO DE SOBRECARGA](#92-polimorfismo-de-sobrecarga)

# **1 DEFINIÇÕES BÁSICAS**

Um objeto é tuda coisa material ou abstrata que pode ser percebida pelos sentidos e descrita por meio das suas características, comportamentos e estado atual.

Todo objeto tem um molde, e caso um dado objeto se enquadre nesse molde ele pode ser classificado como sendo um objeto pertensente aquela classe. Dai o nome classe.

Quando criamos um objeto utilizando o molde de uma dada classe nós podemos dizer que estamos instanciando aquela dada classe.

# **2. CLASSES**

Classes precisão responder a 3 coisas basicas:

- Coisas que eu tenho;
- Coisas que eu faço;
- Como eu estou agora.

Um exemplo, seria uma caneta. Vamos ver:

- Coisas que eu tenho:
  - Modelo;
  - Cor;
  - Ponta;
  - Tampa.
- Coisas que eu faço.
  - Escreve;
  - Rabisca;
  - Pinta.
- Como eu estou agora.
  - Ser do modelo bic alguma coisa.
  - Ser azul;
  - Ter uma ponta fina;
  - Tampada;

> OBS.: O estado da caneta é analizado de acordo com os atributos momentaneos.

Cada uma dessas 3 perguntas têm um nome específico, são eles:

- Atributos;
- Métodos;
- Estado.

# **3. ABSTRAÇÃO**

Abstração é a capacidade de visualizar um objeto no mundo real e conseguir separar quais são seus atributos e métodos importantes para uma dada tarefa.

Um exemplo disso seria o objeto cavalo. Se estivermos falando de um cavalo para:

- Passeio:

  - Atributos:
    - Altura;
    - Obediência.
  - Métodos:
    - Andar.

- Corrida:
  - Atributos:
    - Idade;
    - Velocidade;
    - Obediência;
    - Altura.
  - Métodos:
    - Correr;
    - Saltar;

Veja que mesmo sendo o mesmo objeto, nós consideramos coisas diferentes para funções diferentes. Nisso nós fizemos a abstração do objeto cavalo levando em conta o cenário em que eles está sendo colocado.

# **4. VISIBILIDADE**

A visibilidade indica o nível de acesso aos componentes internos de uma classe.

Existem três níveis de visibilidade, são eles:

- público (+)
  - Uma classe pública pode ser utilizada por ela mesma e por todas as outras classes.
- privado (-)
  - Uma classe privada pode ser utilizada somente por ela mesma.
- protegido (#)
  - Uma classe protegida pode ser utilizada por ela mesma e todas as suas sub-classes. Ou seja, somente a classe mãe e classes filhas podem utilizar essa classe (isso aqui vai ficar mais claro quando formos utilizar herança).

> OBS.: os simbulos `+`, `-` e `#`, são os simbulos que representam cada um dos níveis.

> OBS.: Atributos e métodos também recebem visibilidade, ou seja, eles podem ser vistos ou somente pela propria classe (-), ou por ela e por todas as outras (+), ou somente por ela e pelas sub-classes (#).

Vamos ver como isso funciona na prática. Vamos para um exemplo que temos a classe caneta, como no exemplo anterior, e vamos colocá-la da seguinte forma:

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
  Público Método rabiscar()
  Protegido Método tampada()
```

Agora vamos supor que temos o objeto c1, que é uma caneta. E queremos atribuir valores ao atributos dessa caneta. Porém isso não é uma tarefa tão simples, pois agora temos que nos perguntar se podemos fazer isso. E o motivo para tal é que agora temos atributos que não podem serem utilizados fora da classe. Veja no exemplo:

```Java
c1 = nova Caneta
c1.modelo = "Bic"; // permitido, pois modelo é público.
c1.cor = "Azul" // permitido, pois cor é público.
c1.ponta = 0.5 // não permitido, pois ponta é privado, logo não é utilizável fora da classe
c1.carga = 90 // não permitido, pois c1 é apenas uma chamada de caneta, logo não é mãe nem filha (no java funciona, mas php não, então essa parte é variada de linguagem pra linguagem).
```

Já deu para notar que quando criamos um objeto (fazemos uma chamada da classe), podemos utilizar apenas o que é definido como publico.

> OBS.: Para os métodos é igual.

Vamos entender o porque de definir certas coisas como públicas e outras como privadas. Para isso vou utilizar o exemplo da caneta.

O corpo da caneta é totalmente acessível ao usuário, pois assim ele consegue utilizar a caneta e escrever com ela. Porém o tubo contendo a tinta não é acessível (finge que não da pra abrir a caneta ok?!), e o motivo disso é para que a tinta da caneta não seja retirata, ou qualquer outra coisa que possa estragar a caneta. Logo o que é público em um objeto é a sua parte utilizável e o que é privado é aquilo que somente o "fabricante" pode tocar, e que é de extrema importância para o funcionamento do objeto, logo não pode ser modificado por qualquer um.

# **5. MÉTODOS ESPECIAIS**

Métodos especiais são métodos meio que padronizados de todas as linguagens orientadas a objeto. São eles:

- Métodos Acessores (Getters): São métodos que pegam determinadas informações sem dar acesso direto a essas informações para quem está chamando.
  - Exemplo:
    - Descobrir quanto de dinheiro dentro de um caixa é meu; Eu não posso ir lá no caixa e ver o quanto de dinhero tem no total, ou seja, quanto é meu e quanto é seu; Eu preciso pedir para o atendente do banco ir lá e ver para mim quanto daquele dinheiro é meu, assim eu só tenho acesso a informação que me pertence.
- Métodos Modificadores (Setters): São métodos que executam ações em dados especificos sem dar a visão geral para quem o está chamando.
  - Exemplo:
    - Assim como eu só posso saber quanto de dinheiro eu tenho e não quanto você tem, eu só posso adicionar ou retirar dinheiro da minha parcela (minha conta). E para garantir que não vou retirar da parcela de outra pessoa, ou que outra pessoa retire da minha parcela, devemos utilizar um intemédio do atendente do banco (método setter).

Vamos voltar ao exemplo da caneta, porém vamos torná-lo menor, deixando apenas dois atributos. E vamos definir dois métodos para cada atributo, são eles os métodos get e set de cada um.

```Java
Classe Caneta
  // Atributos
  Privado modelo: String
  Privado cor: String

  // Métodos
  Público Método getModelo()
    retorna modelo
  Público Método setModelo(m: String)
    modelo = m
  Público Método getCor()
    retorna cor
  Público Método setCor(c: String)
    cor = c
```

Então agora ao em vez de modificarmos diretamente os atributos, vamos utilizar os métodos getters e setters para isso. Assim estamos tornando nosso código mais seguro e organizado.

Veja que como os métodos são públicos, eles podem ser acessádos por todo o nosso código, porém os atributos são todos privados, o que impede que os modifiquemos fora da classe. Porém os métodos get e set são pertencentes a classe, logo eles podem modificar os atributos. Ou seja, nós temos acesso aos gets e sets e eles tem acesso aos atributos. Logo a modificação dos atributos acontece apenas de forma indireta.

Entendido esses dois métodos, vamos para mais um método especial, que é o:

- Método Construtor (Construct): O método construtor tem por função definir o estado inicial do objeto, ou seja, ele constroi o objeto para que depois disso ele seja modificado (ou não).
  - Exemplo:
    - O modelo padrão de um bolo é que ele venha sem cobertura e sabor de chocolate. Porém depois dele instanciado posso simplesmente continuar com ele assim ou então começar a mudá-lo, ou seja, posso colocar cobertura, mudar ou mudar o sabor.

Usando o exemplo da caneta, vamos colocar o método construtor que cria canetas bic de cor azul.

- Arquivo classe

  ```Java
  Classe Caneta
    // Atributos
    Privado modelo: String
    Privado cor: String

    // Métodos
    Público Método getModelo()
      retorna modelo
    Público Método setModelo(m: String)
      modelo = m
    Público Método getCor()
      retorna cor
    Público Método setCor(c: String)
      cor = c
    Público Método construtor(m: String, c: String)
      setModelo(m)
      setCor(c)
  ```

- Arquivo Main
  ```Java
  c1 = nova Caneta()
  c1.construtor("Bic", "Azul")
  ```

Veja que de inicio o objeto foi construido como sendo da modelo bic e azul, porém nada me impede de modificar isso tudo a partir dos sets. Ou seja, com o método construtor nos instanciamos o objeto em seu estado inicial.

# **6. ENCAPSULAMENTO**

Encapsular é ocultar partes independentes da implementação, permitindo construir partes invisíveis ao mundo exterior.

Ou seja, você cria um bloco de código que executa uma dada ação, mas não precisa saber como exatamente ele à executa.

Porém é possível nos "comunicar" com essa capsula, e ela irá nos retornar alguma resposta, ou seja, nós podemos trocar mensagens com a capsula.

Toda capsula deve estar contida dentro de uma interface. Sendo que uma interface é uma lista de serviços fornecidos por um componente. É o contato com o mundo exterior, que define o que pode ser feito com um objeto dessa classe.

- Vantagens de se encapsular um código:
  - Tornar mudanças invisíveis. Ou seja, eu posso mudar todo um bloco de código, mas se ele fizer a mesma funçar do que estava ali antes ninguém vai nem notar. Isso facilita otimizar uma dada função sem que afete o restante do programa.
  - Facilita a reutilização de código.
  - Reduz efeitos colaterais. Ou seja, fica mais dificil alguém quebrar o programa mexendo em capsulas. E ao mesmo tempo fica mais fácil corrigir problemas.

Vamos para um exemplo diferente da caneta (ela ficou simples de mais), vamos utilizar um controle remoto.

O controle é todo fechado, ele tem uma capsula externa que é o que nós utilizamos, e a interface dele seria a descrição dos seus botões, e sua função seria controlar uma TV. Assim, se mantivermos a interface (a disposição dos botões, os nomes,..) e mantivermos a função do controle, não importa muito o que tem dentro dele, não importa o circuito que foi utilizado no projeto do mesmo.

> OBS.: Veja que a interface facilita a nossa utilização, pois imagina utilizar um controle remoto sem saber o que cada botão faz.

Vamos agora criar uma capsula passo a passo utilizando o controle remoto.

## 6.1 INTERFACE

Uma interface é parecida com uma classe, porém ela não tem atributos, ela possui apenas métodos. Então vamos criar métodos que o nosso controle faz.

```Java
Interface Controlador
  Público abstrato Método ligar()
  Público abstrato Método desligar()
  Público abstrato Método abrirMenu()
  Público abstrato Método fecharMenu()
  Público abstrato Método maisVolume()
  Público abstrato Método menosVolume()
  Público abstrato Método ligarMudo()
  Público abstrato Método desligarMudo()
  Público abstrato Método play()
  Público abstrato Método pause()
```

Porém os métodos que estão na interface são métodos abstratos, ou seja, eles não são desenvolvidos na interface (o código não está lá). Esses métodos apenas executam uma ação, sendo que o como essa ação é executada está em outro lugar.

Colocando no exemplo do controle, nos sabemos que ao apertar o botão de ligar a tv vai ligar, mas o como é feito o processo de ligar é responsabilidade do circuito interno. Assim, se trocarmos o circuito interno mas mantivermos a interface, e apertarmos o mesmo botão, ele vai chamar o método ligar do circuito interno e executará a mesma função.

Colocando de um jeito mais simples. Você troca o motor do carro sem trocar a carcaça, e ao apertar o acelerador o carro continua andando.

Um detalhe muito importante, é que todos os métodos da interface precisão ser públicos, afinal não existe nenhum botão no seu controle remoto que esteja escondido né?!

Agora, após definida a interface vamos definir a classe. E isso já sabemos muito bem como fazer. Mas tem um detalhe, todos os atributos devem ser ou privados ou protegidos (o que é bem obvio, já que a ideia é proteger as partes internas do objeto).

```Java
Classe ControleRemoto implementa Controlador
  // Atributos
  Privado volume: Inteiro
  Privado ligado: Lógico
  Privado tocando: Lógico

  // Métodos
  Público Método construtor()
    // Código...
  Público Método ligar()
    // Código...
  Público Método desligar()
    // Código...
  Público Método abrirMenu()
    // Código...
  Público Método fecharMenu()
    // Código...
  Público Método maisVolume()
    // Código...
  Público Método menosVolume()
    // Código...
  Público Método ligarMudo()
    // Código...
  Público Método desligarMudo()
    // Código...
  Público Método play()
    // Código...
  Público Método pause()
    // Código...
  Público Método setVolume()
    // Código...
  Público Método getVolume()
    // Código...
  Público Método setLigado()
    // Código...
  Público Método getLigado()
    // Código...
  Público Método setTocando()
    // Código...
  Público Método getTocando()
    // Código...
```

Veja que todos os métodos que estavam na interface forma sobrepostos na classe. Ou seja, nós chamamos/utilizamos a interface e ela chama/usa a classe.

# **7. RELACIONAMENTO ENTRE CLASSES**

Quando temos uma determinada classe em que algum atributo é do tipo de outra classe. Um exemplo disso seria, uma classe Jogador de futebol, em que nossos objetos seriam os jogadores, e uma classe partida, que ocorre entre os jogadores.

```Java
Classe Jogador
  // Atributos
  Privado altura: float
  Privado peso: float
  Privado perna: String

  // Métodos
  Público Método chutar()
```

```Java
Classe Partida
  // Atributos
  Privado jogador1: Jogador
  Privado jogador2: Jogador
  Privado gols1: Inteiro
  Privado gols2: Inteiro

  // Métodos
  Público Método jogar()
  Público Método resultado()
```

# **8. HERANÇA**

Herança é quando uma classe puxa informações de uma classe previamente existente. De forma mais simplificada, uma classe filha pode herdar os atributos e métodos da classe mãe e utilizá-los também.

Ou seja, a herança permite basear uma nova classe na definição de uma outra classe previamente existente.

Isso faz ficar mais fácil criar classes. Pois como as classes filhas já possuem as coisas da classe mãe, não é necessário implementar tudo do zero na classe filha.

Um exemplo para isso seria criarmos uma classe mãe chamada pessoa, que possui tudo aquilo que uma pessoa genérica deve ter, e depois criamos uma classe aluno e uma classe professor. Veja que aluno e professor são pessoas, logo essas duas classes podem herdar a classe pessoa e depois adicionar informações especificas de suas ocupações.

Veja abaixo como ficaria sem utilizarmos herança. Ou seja, criaremos a classe aluno e professor sozinhas.

```Java
Classe Aluno
  // Atributos
  Privado nome: String
  Privado idade: Inteiro
  Privado sexo: String
  Privado matrícula: Inteiro
  Privado curso: String

  // Métodos
  Público Método fazerAniversário()
  Publico Método cancelarMatricula()
```

```Java
Classe Professor
  // Atributos
  Privado nome: String
  Privado idade: Inteiro
  Privado sexo: String
  Privado especialidade: String
  Privado salario: float

  // Métodos
  Público Método fazerAniversário()
  Público Método receberAumento()
```

Veja que as duas classes possuem atributos e métodos em comum. Sendo assim vamos criar a classe mãe com esses atributos e métodos que as classes filhas possuem em comum e depois extendemos as suas funções e atributos para que elas fiquem específicas para cada filha.

```Java
Classe Pessoa
  // Atributos
  Privado nome: String
  Privado idade: Inteiro
  Privado sexo: String

  // Métodos
  Público Método fazerAniversário()
```

```Java
Classe Aluno estender Pessoa
  // Atributos
  Privado matrícula: Inteiro
  Privado curso: String

  // Métodos
  Publico Método cancelarMatricula()
```

```Java
Classe Professor estender Pessoa
  // Atributos
  Privado especialidade: String
  Privado salario: float

  // Métodos
  Público Método receberAumento()
```

Agora as classes filhas possuem tudo que a mãe possui, fazem tudo que a mãe faz e ainda têm suas próprias funções e atributos.

Vamos colocar agora os que cada um desses objetos pode fazer.

```Java
Pessoa pessoa = nova Pessoa()
Aluno aluno = nova Aluno()
Professor professor = nova Professor()
```

Como pessoa, aluno e professor possuem em comum:

- nome;
- idade;
- sexo;
- fazerAniversário().

Todos eles podem fazer essas coisas. logo podemos fazer:

```Java
pessoa.setNome()
aluno.setNome()
professor.setNome()

pessoa.fazerAniversário()
aluno.fazerAniversário()
professor.fazerAniversário()
```

Veja que esses métodos são todos da classe mãe, e as filhas podem utilizar.

> OBS.: Utilizei apenas setNome e fazerAniversário, mas poderia utilizar getNome, setIdade, getIdade, setSexo e getSexo.

E agora cada classe filha pode também executar seus métodos proprios.

```Java
aluno.cancelarMatricula()
aluno.setMatricula()
aluno.setCurso()

professor.receberAumento()
professor.setEspecialidade()
professor.setSalario()
```

> OBS.: O que não pode ser feito é uma classe filha tentar utilizar métodos e atributos de outra classe filha, e nem uma classe mãe tentar utilizar coisas que pertencem apenas às classes filhas. Por exemplo: `pessoa.cancelarMatricula()`, `pessoa.receberAumento()`, `professor.cancelarMatricula()`.

> OBS.: Uma classe filha pode gerar filhas também. Assim sendo uma classe filha é uma subclasse de sua mãe e uma superclasse de sua filha. E como a classe filha tem tudo que a mãe tem, já é de se imaginar que a classe neta vai ter tudo que a mãe dela e a avó tem.

## 8.1 TIPOS DE CLASSES E MÉTODOS

Antes vamos só explicar o conceito de árvores de herança.

Como já dito antes, podemos fazer uma cadeia de heranças, onde a classe A é herdada por AA, que é herdada por AAA, e assim por diante.

Nesse exemplo, a classe A é a raiz da árvore, e a classe AAA é a folha (supondo que ela seja a ultima classe na cadeia).

- Classe abstrata: Não pode ser instanciada, só pode servir como progenitora (mãe).
  - Ou seja, se tentarmos criar um objeto a partir de uma classe abstrata vai dar ruim.
- Método abstrato: Declarado, mas não implementado na progenitora.
  - Foi exatamente o que fizemos em interface. Nós só dizemos que ele existe e ele será sobreposto na classe filha.
- Classe final: Não pode ser herdada por outra classe.
  - Ou seja, ela é uma folha na árvore de herança. Pois nenhuma outra classe herdará dela.
- Método final: Não pode ser sobreposto pelas suas sub-classes. Obrigatoriamente herdado.
  - Ou seja, ela pode ser herdada por alguém, mas não pode ter sua função alterada.

Vamos manter o exemplo da pessoa, aluno e professor para exemplificar. Vamos definir que a classe pessoa é abstrata, assim não podemos criar pessoas só pessoas, elas tem que fazer alguma coisa. E também vamos dizer que o método fazerAniversário é um método final, afinal de contas não faz sentido mudarmos a forma com que se faz aniversário, acredito que seja igual pra qualquer pessoa. E vamos também acressentar duas classes netas, as duas vindas de aluno, sendo que uma é do aluno bolsista e a outra é do aluno não bolsista. E assim vamos acressentar o atributo mensalidade para o aluno.

```Java
Classe abstrata Pessoa
  // Atributos
  Privado nome: String
  Privado idade: Inteiro
  Privado sexo: String

  // Métodos
  Público Método final fazerAniversário()
```

- Se eu tentasse criar um objeto pessoa (`pessoa = nova Pessoa()`) teriamos um erro.

- Se tentarmos sobrepor fazerAniversário (`sobrepor fazerAniversário()`) teriamos um erro.

```Java
Classe Aluno estender Pessoa
  // Atributos
  Privado matrícula: Inteiro
  Privado curso: String
  Privado mensalidade: float

  // Métodos
  Publico Método cancelarMatricula()
  Publico Método pagarMensalidade()
```

- Essa classe `Aluno` pode ser instanciada e utilizada normalmente.

```Java
Classe Professor estender Pessoa
  // Atributos
  Privado especialidade: String
  Privado salario: float

  // Métodos
  Público Método receberAumento()
```

- Essa classe `Professor` pode ser instanciada e utilizada normalmente.

```Java
Classe AlunoBolsista estender Aluno
  // Atributos
  Privado bolsa: Inteiro

  // Métodos
  @Sobrepor
  Público Método pagarMensalidade()
```

```Java
Classe AlunoNaoBolsista estender Aluno
```

Veja que a o aluno bolsista precisa mudar o comportamento do pagamento da mensalidade, pois não à paga integralmente. Já o aluno não bolsista paga a mensalidade integral, isso faz dele um aluno "normal", logo não é necessário modificarmos nada classe anterior e nem acressentar.

> OBS.: Quando não efetuamos nenhuma mudança na classe mãe para a filha e nem acressentamos nada, falamos que fizemos uma herança pobre, onde somente pegamos o que já tinhamos pronto e não contribuimos com nada.

# **9. POLIMORFISMO**

- Poli: Muitas
- Morfo: Formas
- Polimorfismo: Várias formas

Polimorfismo permite que o mesmo nome represente vários comportamentos diferentes.

Um exemplo disso seria o como você anda.

- Quando está atrasado: Anda mais rápido.
- Quando está com muito tempo: Anda mais devagar.
- Qaundo está passeando: Anda muito lento admirando a paisagem

E por ai vai.

Mas seja lá como for, tudo isso é o ato de andar, e você pode executá-lo de diversas formas.

Então ai surge um problema, como identificar quando executar essa tarefa de um jeito ou de outro?

Basicamente cada método irá ter uma assinatura, que vai nos permitir efetuar essa identificação.

Uma assinatura do método consistem na quantidade e os tipos dos parâmetros. Ou seja, dependendo da quantidade e do tipos dos parâmetros que passamos parar um parâmetro nos conseguimos saber qual método é.

Um exemplo disso seria o método andar.
Se em um cenário não precisamos passar como parâmetro o tipo de calçado que iremos utilizar, quer dizer que não iremos andar rápido, afinal se precisarmos andar rápido vamos obrigatoriamente utilizar um tênis (eu sei, a realidade não é tão perfeita assim, as vezes a gente esquece disso e acaba arrebentando o chinelo).

Vamos olhar isso pela otica de um exemplo em algoritmo.

```Java
Público Método calcularMédia(n1: Real, n2: Real)
  retorna media: Real

Público Método calcularMédia(n1: Real, n2: Real)
  retorna media: Inteiro
```

Nesse exemplo os dois métodos possuem a mesma assinatura, pois possuem a mesma quantidade de parâmetros e eles possuem os mesmos tipos, mesmo retornando coisas diferentes. Afinal na definição não é colocado que o que acontece dentro desses métodos deve ser igual para eles terem a mesma assinatura, o que conta é apenas o nome, quantidade e tipo dos parâmetros.

Agora no exemplo seguinte, vamos ter dois métodos com o mesmo nome, porém com assinaturas diferentes, pois o primeiro precisa de 3 parâmetros e o segundo somente 2.

```Java
Público Método calcularMédia(n1: Real, n2: Real, n3: Real)
  retorna media: Real

Público Método calcularMédia(n1: Real, n2: Real)
  retorna media: Inteiro
```

## 9.1 POLIMORFISMO DE SOBREPOSIÇÃO

O polimorfismo de sobreposição acontece quando substituimos um método de uma superclasse na sua subclasse, usando a mesma assinatura. Ou seja, nos utilizamos o mesmo nome para o método e os mesmos parâmetros.

Logo podemos dizer que quando queremos sobrepor um dado método estamos dizendo que queremos recriar o como aquele método se comporta. Um exemplo disso seria que a sua mãe corta cebolas na horizontal, mas você corta na vertical. Então essa função que sua mãe possui (cortar cebolas) é executada de um jeito por ela, mas por você é executada de outra forma.

Vamos mostrar o seguinte exemplo:

- Uma classe abstrata mãe animal
  - Atributos:
    - peso
    - idade
    - membros
  - Métodos abstratos:
    - locomover
    - alimentar
    - emitir Som
- Uma classe filha mamifero:
  - Atributos
    - Cor do pelo
- Uma classe filha réptil:
  - Atributos
    - cor das escamas
- Uma classe filha peixe:
  - Atributos
    - cor da escama
  - Métodos
    - soltar Bolhas
- Uma classe filha ave
  - Atributos
    - cor da pena
  - Métodos
    - fazer Ninho

Em algoritmo teriamos

```Java
Classe abstrata Animal
  //Atributos
  Protegido peso: Real
  protegido idade: Inteiro
  protegido menbros: Inteiro

  //Métodos
  Público Método abstrato locomover()
  Público Método abstrato alimentar()
  Público Método abstrato emitirSom()
```

```Java
Classe Mamifero estende Animal
  // Atributos
  Privado corPelo: String

  // Métodos
  @Sobrepor
  Público Método locomover()
    Escreva("correndo")

  @Sobrepor
  Público Método alimentar()
    Escreva("mamando")

  @Sobrepor
  Público Método emitirSom()
    Escreva("som de mamífero")
```

```Java
Classe Réptil estende Animal
  // Atributos
  Privado corEscama: String

  // Métodos
  @Sobrepor
  Público Método locomover()
    Escreva("rastejando")

  @Sobrepor
  Público Método alimentar()
    Escreva("comendo Vegetais")

  @Sobrepor
  Público Método emitirSom()
    Escreva("som de reptil")
```

```Java
Classe Peixe estende Animal
  // Atributos
  Privado corEscama: String

  // Métodos
  @Sobrepor
  Público Método locomover()
    Escreva("nadando")

  @Sobrepor
  Público Método alimentar()
    Escreva("comendo substancias")

  @Sobrepor
  Público Método emitirSom()
    Escreva("som de peixe")

  Público Método soltarBolha()
    Escreva("soltou bolhas")
```

```Java
Classe Ave estende Animal
  // Atributos
  Privado corPena: String

  // Métodos
  @Sobrepor
  Público Método locomover()
    Escreva("voando")

  @Sobrepor
  Público Método alimentar()
    Escreva("comando frutas")

  @Sobrepor
  Público Método emitirSom()
    Escreva("som de ave")

  Público Método fazerNinho()
    Escreva("construiu um ninho")
```

Se chamarmos o mesmo método pra essas diferente objetos (animais) vamos obter diferentes resultados. Exemplo:

```Java
mamifero = novo Mamifero()
reptil = novo Reptil()
peixe = novo Peixe()
ave = novo Ave()

mamifero.locomover() // resposta: correndo
reptil.locomover() // resposta: rastejando
peixe.locomover() // resposta: nadando
ave.locomover() // resposta: voando
```

Essa capacidade de mostrar diferentes resultados (executar coisas diferentes) que um mesmo método possui é o polimorfismo.

## 9.2 POLIMORFISMO DE SOBRECARGA

No caso da sobreposição tinhamos que os métodos sobrepostos tinham a mesma assinatura do método contido na classe mãe, porém na sobrecarga estamos falando de um método da classe filha que se repete dentro da mesma, porém essas versões do método vão ter assinaturas diferentes.

Vamos definir o seguinte exemplo: Uma classe mamifero gerará a classe filha cachorro que pode agir de modos diferentes para determinadas situações.

```Java
Classe abstrata Mamifero
  Público Método abstrato alimentar()
```

```Java
Classe Cachorro estende Mamifero
  Público Método reagir(frase: String)
  Público Método reagir(hora: Inteiro)
  Público Método reagir(dono: Logico) // se é ou não o dono que se aproxima
  Público Método reagir(idade: Inteiro, peso: Inteiro)
```

Veja que agora ele sobrecarrega o método, e não mantém mais a assinatura dele.

> OBS.: **_E um detalhe de extrema importância, note que podemos sobrecarregar o mesmo método diversas vezes dentro da mesma classe. Já a sobreposição ocorre apenas uma vez por classe._**

Agora vamos utilizar esses métodos. E isso pode ser um pouco confuso, porque no final das contas temos que fazer `cachorro.reagir()`, e ai fica a duvida "Qual dos 4 métodos a linguagem vai escolher executar?", bem, ele vai executar aquele que tiver exatamente a mesa assinatura que passarmos. Isso é, se mandarmos para ele como parâmetros uma string ele vai encaixar no primeiro método reagir, se mandarmos um inteiro ele vai encaixar no segundo método reagir, e assim em diante.

```Java
cachorro = novo Cachorro()
cachorro.reagir("olá") // String, primeiro reagir
cachorro.reagir(15) // inteiro, segundo reagir
cachorro.reagir(true) // logico, terceiro reagir
cachorro.reagir(6, 45) // dois inteiros, quarto reagir
```

Ai você pode estar se perguntando. Mas e se dois métodos reagir tiverem os mesmos tipos de parâmetro, porém parâmetros com nomes diferentes?

Por exemplo

```Java
Público Método reagir(idade: Inteiro)
Público Método reagir(peso: Inteiro)
```

bem, não importa, pois para a assinatura o que é relevante é a quantidade e o tipo dos parâmetros, não os nomes. Então a linguagem não consegue diferenciar entre esses dois métodos.
