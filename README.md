# Taskify API

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

Taskify é uma API simples para gerenciar uma lista de tarefas (to-do list), escrita em Python com Flask. Permite criar, listar, atualizar, marcar como concluídas e deletar tarefas, com persistência em um arquivo JSON.

## Funcionalidades

- **Criar Tarefa:** Adicione novas tarefas com título e timestamp de criação automático.
- **Listar Tarefas:** Veja todas as tarefas salvas.
- **Atualizar Tarefa:** Modifique o título ou status de conclusão.
- **Marcar como Concluída:** Atualize o status de uma tarefa para concluída.
- **Deletar Tarefa:** Remova tarefas específicas.
- **Persistência:** Dados salvos em `tasks.json` com codificação UTF-8.

## Pré-requisitos

- **Python 3.10 ou superior**  
- **pip** (gerenciador de pacotes do Python)

## Instalação

1. **Clone o Repositório:**
   ```bash
   git clone https://github.com/Joullie/taskify.git
   cd taskify
   ```

2. **Crie um Ambiente Virtual:**
   ```bash
   python -m venv venv
   ```

3. **Ative o Ambiente:**
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
   - Windows:
     ```powershell
     venv\Scripts\activate
     ```

4. **Instale as Dependências:**
   ```bash
   pip install -r requirements.txt
   ```

## Uso

### Inicie o Servidor:
   ```bash
   python run.py
   ```
O servidor estará disponível em `http://127.0.0.1:5000`. Para parar, pressione `Ctrl+C`.

## Endpoints da API

| Método | Endpoint               | Descrição                | Corpo da Requisição (JSON)          | Resposta (JSON) |
|---------|------------------------|----------------------------|--------------------------------|----------------|
| POST    | `/api/tasks`           | Criar uma nova tarefa      | `{ "title": "string" }`        | `{ "id": int, "title": "string", "completed": bool, "created_at": "string" }` |
| GET     | `/api/tasks`           | Listar todas as tarefas    | `-`                            | `[{...}, {...}]` |
| PUT     | `/api/tasks/<id>`      | Atualizar uma tarefa       | `{ "title": "string", "completed": bool }` | `{ "id": int, "title": "string", "completed": bool, "created_at": "string" }` |
| POST    | `/api/tasks/<id>/complete` | Marcar como concluída  | `-`                            | `{ "id": int, "title": "string", "completed": true, "created_at": "string" }` |
| DELETE  | `/api/tasks/<id>`      | Deletar uma tarefa         | `-`                            | `{ "message": "Task deleted" }` |

## Exemplos de Requisições (PowerShell)

### Criar uma Tarefa:
```powershell
Invoke-WebRequest -Uri "http://127.0.0.1:5000/api/tasks" -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"title":"Estudar Python"}'
```

### Listar Tarefas:
```powershell
(Invoke-WebRequest -Uri "http://127.0.0.1:5000/api/tasks" -Method GET).Content
```

### Atualizar uma Tarefa:
```powershell
(Invoke-WebRequest -Uri "http://127.0.0.1:5000/api/tasks/1" -Method PUT -Headers @{"Content-Type"="application/json"} -Body '{"title":"Estudar Flask","completed":true}').Content
```

### Marcar como Concluída:
```powershell
(Invoke-WebRequest -Uri "http://127.0.0.1:5000/api/tasks/1/complete" -Method POST).Content
```

### Deletar uma Tarefa:
```powershell
(Invoke-WebRequest -Uri "http://127.0.0.1:5000/api/tasks/1" -Method DELETE).Content
```

## Teste com Outras Ferramentas

Use **Postman**, **curl**, ou outro cliente HTTP para interagir com a API.

## Testes

Execute os Testes Unitários:
```bash
pytest app/tests/test_routes.py -v
```

Os testes verificam todas as rotas da API, garantindo que criação, listagem, atualização, marcação como concluída e exclusão funcionem corretamente.

## Resolução de Problemas

- **Erro de Codificação:** Se ocorrer `'utf-8' codec can't decode`, recrie o `tasks.json`:
  ```powershell
  del tasks.json
  echo "[]" > tasks.json
  ```
  Reinicie o servidor após isso.

- **Tarefas Não Persistem:** Verifique se o `tasks.json` está no diretório raiz e tem permissões de escrita.

## Contribuição

1. Faça um fork do repositório.
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b feature/nova-funcionalidade
   ```
3. Commit suas mudanças:
   ```bash
   git commit -m "Adicionada nova funcionalidade"
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin feature/nova-funcionalidade
   ```
5. Abra um Pull Request no GitHub.

## Licença

Este projeto está licenciado sob a **MIT License**. Veja o arquivo `LICENSE` para mais detalhes.

