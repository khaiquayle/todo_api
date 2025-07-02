# TODO App

A full-stack Todo application with React frontend and Flask backend.

## Project Structure

```
TODO_APP/
├── backend/         # Flask backend
│   ├── app.py       # Main Flask application
│   ├── database.py  # Database configuration
│   ├── models.py    # SQLAlchemy models
│   └── validators.py # Input validation
│
└── frontend/        # React frontend
    ├── public/      # Static files
    ├── src/         # React source code
    │   ├── components/  # React components
    │   ├── services/    # API services
    │   └── ...
    └── package.json # Frontend dependencies
```

## Backend Setup

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

4. Install dependencies:
   ```
   pip install flask flask-sqlalchemy flask-jwt-extended flask-cors
   ```

5. Run the backend server:
   ```
   python app.py
   ```

## Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Remove node_modules and package-lock.json:
   ```
   rm -rf node_modules package-lock.json
   ```

3. Install dependencies:
   ```
   npm install
   ```

4. Start the development server:
   ```
   npm start
   ```

## Features

- User authentication (register/login)
- Create, read, update, and delete todos
- Set due dates for todos
- Mark todos as complete/incomplete 