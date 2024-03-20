# Desafio API REST em Python

Este projeto foi proposto por nosso mentor [Rafael Fino](https://github.com/RafaelFino) para testar nossas habilidades na criação de uma API REST em Python.

## Bibliotecas utilizadas

- Flask: Utilizado para criar a aplicação web e as rotas da API.
- env: Utilizado para gerenciar as variáveis de ambiente da aplicação.
- sqlite3: Utilizado como banco de dados para armazenar os dados da aplicação.

## Estrutura do projeto

O projeto segue boas práticas de separação de responsabilidades, com a estruturação em áreas distintas:

### Model

Nesta área são definidos os modelos de dados utilizados pela aplicação, como as classes que representam os objetos manipulados pela API.

### Storage

A área de armazenamento (`Storage`) é responsável por toda a interação com o banco de dados. Aqui são definidos os métodos para inserção, atualização, exclusão e consulta de dados.

### Service

Na área de serviço (`Service`), são implementadas as regras de negócio da aplicação. Aqui ocorre a lógica de manipulação dos dados antes de serem persistidos no banco de dados. Esta camada é responsável por validar os dados, executar operações complexas e orquestrar a interação entre os modelos e a área de armazenamento.
