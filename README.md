# Taskify - RESTful API for Task Management

## Description

Taskify is a simple API for managing tasks, built with Flask. It allows creating, listing, updating, completing, and deleting tasks, with data stored in a JSON file.

## Features

- Create, update, delete, and list tasks.
- Mark tasks as completed.
- Data stored in `tasks.json`.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Joullie/taskify.git
   cd taskify
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   ```

   - On **Linux/Mac**:
     ```bash
     source venv/bin/activate
     ```
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Start the server:

```bash
python run.py
```

The server will be available at `http://127.0.0.1:5000`. To stop, press `Ctrl+C`.

## API Endpoints

| Method | Endpoint                  | Description        | Request Body (JSON)                                 | Response (JSON)                                                  |
|--------|---------------------------|--------------------|-----------------------------------------------------|------------------------------------------------------------------|
| POST   | `/api/tasks`              | Create a new task  | `{ "title": "string" }`                             | `{ "id": int, "title": "string", "completed": bool, "created_at": "string" }` |
| GET    | `/api/tasks`              | List all tasks     | -                                                   | `[ {...}, {...} ]`                                               |
| PUT    | `/api/tasks/<id>`         | Update a task      | `{ "title": "string", "completed": bool }`          | `{ "id": int, "title": "string", "completed": bool, "created_at": "string" }` |
| POST   | `/api/tasks/<id>/complete`| Mark as completed  | -                                                   | `{ "id": int, "title": "string", "completed": true, "created_at": "string" }`  |
| DELETE | `/api/tasks/<id>`         | Delete a task      | -                                                   | `{ "message": "Task deleted" }`                                  |

## Request Examples (PowerShell)

- **Create a task:**

  ```powershell
  Invoke-WebRequest -Uri "http://127.0.0.1:5000/api/tasks" -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"title":"Study Python"}'
  ```

- **List tasks:**

  ```powershell
  (Invoke-WebRequest -Uri "http://127.0.0.1:5000/api/tasks" -Method GET).Content
  ```

- **Update a task:**

  ```powershell
  (Invoke-WebRequest -Uri "http://127.0.0.1:5000/api/tasks/1" -Method PUT -Headers @{"Content-Type"="application/json"} -Body '{"title":"Study Flask","completed":true}').Content
  ```

- **Mark as completed:**

  ```powershell
  (Invoke-WebRequest -Uri "http://127.0.0.1:5000/api/tasks/1/complete" -Method POST).Content
  ```

- **Delete a task:**

  ```powershell
  (Invoke-WebRequest -Uri "http://127.0.0.1:5000/api/tasks/1" -Method DELETE).Content
  ```

## Testing

Run Unit Tests:

```bash
pytest app/tests/test_routes.py -v
```

## Troubleshooting

- **Encoding Error:** If a 'utf-8' codec error occurs, recreate `tasks.json`:

  ```bash
  del tasks.json
  echo "[]" > tasks.json
  ```

- **Tasks not persisting:** Ensure `tasks.json` is in the root directory and has write permissions.

## Contribution

1. Fork the repository.
2. Create a branch for your feature:

   ```bash
   git checkout -b feature/new-feature
   ```

3. Commit your changes:

   ```bash
   git commit -m "Added new feature"
   ```

4. Push to the remote repository:

   ```bash
   git push origin feature/new-feature
   ```

5. Open a Pull Request on GitHub.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
