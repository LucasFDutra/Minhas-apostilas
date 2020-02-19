# Apostila de oracle SQL

- Links úteis
    - [TechOnTheNet](https://www.techonthenet.com/oracle/index.php)
    [Oracle](https://docs.oracle.com/en/database/oracle/oracle-database/20/cncpt/sql.html#GUID-AF25E66F-965C-44B8-91B8-1A9F95FCF99D)

## Introdução
Vamos começar instalando as ferramentas que utilizaremos.

Primeiramente instale o oracle database express, que é uma versão gratuita do banco. Para isso, utilize o link abaixo e escolha a opção de acordo com sua plataforma:

- [Instalador do oracle XE](https://www.oracle.com/database/technologies/xe-downloads.html)

Agora instale o oracle Sql Developer, que nos permitirá executar ações em nosso banco de dados.

- [Instalador do Sql Developer](https://www.oracle.com/tools/downloads/sqldev-v192-downloads.html)

Após instalar as ferramentas, vá até o sql developer e inicie uma nova conexão. Para isso siga os passos a seguir:


# CREATE
Esse comando serve para criar coisas em sql. Mas primeiramente vamos utilizar ele para criar uma tabela.

- comando: 
    ```sql
    CREATE TABLE nome_da_tabela (
        nome_da_coluna_1 tipo,
        nome_da_coluna_2 tipo,
    );
    ```

vamos criar três tabelas para podermos efetuar operações de relacionamentos entre elas.

- products
- companies
- products_companies

vejamos a estrutura de cada uma das nossas tabelas:

## products
---
|coluna|tipo|
|-|-|
|id_product_pk|NUMBER|
|productName|VARCHAR|

## companies
---
|coluna|tipo|
|-|-|
|id_company_pk|NUMBER|
|companyName|VARCHAR|

## products_companies
---
|coluna|tipo|
|-|-|
|id_product_fk|NUMBER|
|id_company_fk|NUMBER|

vou explicar cada item dessas tabelas. 

As colunas de `id` são para utilizarmos identificadores para cada um de nossos itens. Os `id_pk` são aqueles que são chaves primárias, sendo que em cada tabela temos uma, e essas chaves primárias devem ser unicas, pois assim conseguiremos de forma fácil encontrar um item na nossa tabela. Já uma chave `id_fk`, é uma chave estrangeira, que serve para fazermos conexões entre tabelas. Exemplo: `id_product_fk` faz referência ao produto da tabela `products` dentro da tabela `products_companies`, sendo assim podemos relacionar os produtos com as companhias.

Para criar essa tabela podemos fazer o seguinte (ainda não copie os comando eles irão mudar).

- criando exemplo:
    ```sql
    CREATE TABLE products(
        id_product_pk NUMBER,
        productName VARCHAR,
    );

    CREATE TABLE companies(
        id_company_pk NUMBER,
        companyName VARCHAR,
    );

    CREATE TABLE products_companies(
        id_product_fk NUMBER,
        id_company_fk NUMBER,
    );
    ```

Dessa forma já teremos as nossas tabelas, porém dessa forma o banco de dados não sabe quem é chave primária, e nem quem é chave estrangeira, então precisamos identificá-las. Para isso precisamos utilizar o comando `CONSTRAINT`.

- comando para definir chave primária: 
    ```sql
    CREATE TABLE nome_da_tabela (
        coluna_pk tipo,
        coluna_2 tipo,
        CONSTRAINT constraint_name PRIMARY KEY (coluna_pk)
    );
    ```
- comando para definir chave estrangeira: 
    ```sql
    CREATE TABLE nome_da_tabela (
        coluna_1_fk tipo,
        coluna_2_fk tipo,
        coluna2 tipo,
        CONSTRAINT constraint_name_1 
            FOREING KEY (coluna_1_fk) REFERENCES tabela_pai_1 (coluna_1_pk),
        CONSTRAINT constraint_name_2 
            FOREING KEY (coluna_2_fk) REFERENCES tabela_pai_2 (coluna_2_pk),
    );
    ```

- Ajustando exemplo:
    ```sql
    CREATE TABLE products(
        id_product_pk NUMBER,
        productName VARCHAR,
        CONSTRAINT constraint_product PRIMARY KEY (id_product_pk),
    );

    CREATE TABLE companies(
        id_company_pk NUMBER,
        companyName VARCHAR,
        CONSTRAINT constraint_companies PRIMARY KEY (id_companies_pk),
    );

    CREATE TABLE products_companies(
        id_product_fk NUMBER,
        id_company_fk NUMBER,
        CONSTRAINT constraint_pc_product REFERENCES products (id_product_pk),
        CONSTRAINT constraint_pc_companies REFERENCES companies (id_company_pk),
    );
    ```