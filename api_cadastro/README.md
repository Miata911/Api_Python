# API de Cadastro de Usuários

Descrição
Esta API foi desenvolvida utilizando o framework FastAPI com o objetivo de realizar operações básicas de cadastro de usuários. O sistema permite criar, listar, atualizar e remover usuários, utilizando uma estrutura simples em memória (listas e dicionários), simulando um banco de dados.

## Tecnologias Utilizadas
- Python
- FastAPI
- Uvicorn
- JSON
- Pydantic

## Estrutura dos Dados

Cada usuário possui a seguinte estrutura:

```json
{
  "id": 1,
  "nome": "Luiz ",
  "idade": 20
}
Endpoints da API
GET /usuarios

Retorna a lista de todos os usuários cadastrados.

POST /usuarios

Cria um novo usuário.

Exemplo de envio:

{
  "nome": "Diogo",
  "idade": 20
}
PUT /usuarios/{id}

Atualiza os dados de um usuário existente com base no ID.

Exemplo de envio:

{
  "nome": "Novo Nome",
  "idade": 30
}
DELETE /usuarios/{id}

Remove um usuário com base no ID informado.

GET /

Endpoint inicial que verifica se a API está em execução.

Execução do Projeto

Instalar dependências:

pip install fastapi uvicorn

Executar a API:

python -m uvicorn main:app --reload

Acessar a documentação interativa:

http://127.0.0.1:8000/docs

Observações

Os dados são armazenados em memória, portanto são perdidos ao reiniciar a aplicação.
A API utiliza estrutura simplificada com listas e dicionários para simulação de banco de dados.
Autores

Luiz felipe pintor 
Diogo de Souza Assis 
