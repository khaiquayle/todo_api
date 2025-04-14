# Todo API

A simple RESTful API for managing todo items built with Flask and SQLAlchemy, secured with JWT authentication.

## Features

- User registration and authentication using JWT tokens
- Create, read, update, and delete todo items
- Input validation for title and completed status
- SQLite database for persistence
- RESTful API design
- Secure endpoints with JWT authentication

## Authentication

The API uses JWT (JSON Web Token) authentication to secure endpoints. Here's what you need to know:

### Token Management
- Tokens expire after 1 hour for security
- After token expiration, users need to log in again to get a new token
- All todo operations require a valid JWT token

### Why Tokens Expire
1. **Security**: Limits the window of opportunity if tokens are stolen
2. **Session Control**: Ensures periodic re-authentication
3. **Compliance**: Meets security standards and regulations

## API Endpoints

### Authentication Endpoints
- `POST /register` - Register a new user
- `POST /login` - Login and receive a JWT token

### Todo Endpoints (Requires JWT Authentication)
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
5. Set your JWT secret key (optional):
   ```bash
   export JWT_SECRET_KEY="your-secure-secret-key"
   ```
6. Run the application: `python app.py`

## API Usage

### Register a New User
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"username":"your_username", "password":"your_password"}' \
  http://localhost:5001/register
```

### Login and Get Token
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"username":"your_username", "password":"your_password"}' \
  http://localhost:5001/login
```

### Using JWT Token with Requests
Add the token to the Authorization header for all todo operations:
```bash
curl -H "Authorization: Bearer your_jwt_token" http://localhost:5001/todos
```

### Create a Todo
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_jwt_token" \
  -d '{"title":"Add due_date feature to todo api", "due_date":"2025-04-13"}' \
  http://localhost:5001/todos
```

### Get All Todos
```bash
curl -H "Authorization: Bearer your_jwt_token" http://localhost:5001/todos
```

### Get a Specific Todo
```bash
curl -H "Authorization: Bearer your_jwt_token" http://localhost:5001/todos/1
```

### Update a Todo
```bash
curl -X PUT \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_jwt_token" \
  -d '{"completed":true}' \
  http://localhost:5001/todos/1
```

### Delete a Todo
```bash
curl -X DELETE -H "Authorization: Bearer your_jwt_token" http://localhost:5001/todos/1
```

## Input Validation

- Title must be a string
- Title cannot be empty
- Title cannot exceed 500 characters
- Completed status must be a boolean 
- Due date must follow YYYY-MM-DD format
- Due date must be after 1970
- Due date can be null

## Security Notes

1. JWT tokens expire after 1 hour for security
2. Store your JWT_SECRET_KEY securely using environment variables
3. Never share your JWT tokens
4. Always use HTTPS in production
5. Passwords are securely hashed using pbkdf2:sha256