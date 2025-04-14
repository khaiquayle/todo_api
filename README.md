# Todo API

A simple RESTful API for managing todo items built with Flask and SQLAlchemy.

## Features

- Create, read, update, and delete todo items
- Input validation for title and completed status
- SQLite database for persistence
- RESTful API design

## API Endpoints

- `GET /todos` - Get all todos
- `POST /todos` - Create a new todo
- `GET /todos/<id>` - Get a specific todo
- `PUT /todos/<id>` - Update a todo
- `DELETE /todos/<id>` - Delete a todo

## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the application: `python app.py`

## API Usage

### Create a Todo

```bash
curl -X POST -H "Content-Type: application/json" -d '{"title":"Add due_date feature to todo api", "due_date":"2025-04-13"}' http://localhost:5001/todos
```

### Get All Todos

```bash
curl http://localhost:5001/todos
```

### Get a Specific Todo

```bash
curl http://localhost:5001/todos/1
```

### Update a Todo

```bash
curl -X PUT -H "Content-Type: application/json" -d '{"completed":true}' http://localhost:5001/todos/1
```

### Delete a Todo

```bash
curl -X DELETE http://localhost:5001/todos/1
```

## Input Validation

- Title must be a string
- Title cannot be empty
- Title cannot exceed 500 characters
- Completed status must be a boolean 
- Due date must follow ____-__-__
- Due date must be after 1970
- Due date can be null