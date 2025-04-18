
# 💬 API RESTful de Chat com FastAPI

Este projeto consiste em uma API RESTful desenvolvida com **FastAPI** para simular um sistema de chat em tempo real. A aplicação permite o gerenciamento de **usuários**, **salas de chat** e **mensagens** (privadas e em grupo), utilizando armazenamento em memória.

---

## 🚀 Funcionalidades

### 👤 Usuários
- `POST /users` - Registrar novo usuário
- `POST /users/login` - Login do usuário
- `GET /users/{user_id}` - Obter informações de um usuário

### 💬 Salas de Chat
- `POST /rooms` - Criar uma nova sala
- `GET /rooms` - Listar todas as salas
- `DELETE /rooms/{room_id}` - Remover uma sala
- `POST /rooms/{room_id}/enter` - Entrar em uma sala
- `POST /rooms/{room_id}/leave` - Sair de uma sala
- `DELETE /rooms/{room_id}/users/{user_id}` - Remover usuário de uma sala

### ✉️ Mensagens
- `POST /messages/direct/{receiver_id}` - Enviar mensagem direta
- `POST /rooms/{room_id}/messages` - Enviar mensagem para uma sala
- `GET /rooms/{room_id}/messages` - Obter histórico da sala

---



## Acesse:

http://127.0.0.1:8000/docs
Isso deve abrir o Swagger da sua API, com todos os endpoints organizados automaticamente.

http://127.0.0.1:8000/redoc
Outra documentação automática do FastAPI.


