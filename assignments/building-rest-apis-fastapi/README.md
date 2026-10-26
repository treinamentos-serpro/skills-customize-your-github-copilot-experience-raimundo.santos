# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para gerenciar tarefas usando FastAPI. Pratique rotas HTTP, modelos de dados com Pydantic e operações CRUD com respostas e códigos de status apropriados.

## 📝 Tasks

### 🛠️ Create the API and list tasks

#### Descrição
Complete o aplicativo FastAPI no arquivo `starter-code.py` para expor uma rota inicial e uma rota que liste as tarefas armazenadas em memória.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI.
- Implementar `GET /` com uma mensagem de boas-vindas.
- Implementar `GET /tasks` para retornar a lista de tarefas.
- Permitir iniciar a aplicação com Uvicorn e acessar a documentação interativa em `/docs`.

### 🛠️ Create and retrieve tasks

#### Descrição
Use um modelo Pydantic para validar os dados de uma tarefa. Implemente as rotas para criar uma tarefa e consultar uma tarefa pelo identificador.

#### Requisitos
O programa concluído deve:

- Definir os campos `title` e `completed` no modelo de entrada, com `completed` iniciando como `false` por padrão.
- Implementar `POST /tasks` para criar uma tarefa e atribuir a ela um identificador único.
- Implementar `GET /tasks/{task_id}` para retornar a tarefa correspondente.
- Retornar o código HTTP `404` quando o identificador não corresponder a uma tarefa existente.

### 🛠️ Update and delete tasks

#### Descrição
Complete as operações de atualização e exclusão para que clientes possam gerenciar tarefas existentes pelo identificador.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /tasks/{task_id}` para atualizar o título e o estado de conclusão de uma tarefa.
- Implementar `DELETE /tasks/{task_id}` para excluir uma tarefa existente.
- Retornar o código HTTP `404` quando a tarefa solicitada não existir.
- Retornar o código HTTP `204` após excluir uma tarefa com sucesso.

Para executar o projeto, instale FastAPI com Uvicorn usando `python -m pip install "fastapi[standard]"`. Renomeie uma cópia de `starter-code.py` para `main.py` e execute `uvicorn main:app --reload` no diretório do arquivo.
