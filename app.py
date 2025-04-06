from flask import Flask, jsonify, request
from database import db
from models import Todo  # Import Todo model first

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "To-Do API is running!"

@app.route('/todos', methods=['GET'])
def get_todos():
    print("Getting all todos...")  # Debug print
    todos = Todo.query.all()
    print(f"Found {len(todos)} todos")  # Debug print
    return jsonify([todo.to_dict() for todo in todos])

@app.route('/todos', methods=['POST'])
def post_todos():
    print("Creating new todo...")  # Debug print
    data = request.get_json()
    print(f"Received data: {data}")  # Debug print
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    if not isinstance(data['title'], str):
        return jsonify({'error': 'Title must be a string'}), 400
    if len(data['title']) < 1:
        return jsonify({'error': 'Title cannot be empty'}), 400
    if len(data['title']) > 500:
        return jsonify({'error': f"Title too long (title length: {len(data['title'])}; maximum 500 characters)"}), 400
    new_todo = Todo(title=data['title'])
    db.session.add(new_todo)
    db.session.commit()
    print(f"Created todo: {new_todo.to_dict()}")  # Debug print
    return jsonify(new_todo.to_dict()), 201

@app.route('/todos/<int:id>', methods=['GET'])
def get_todo(id):
    todo = Todo.query.get_or_404(id)
    return jsonify(todo.to_dict())

@app.route('/todos/<int:id>', methods=['PUT'])
def put_todo(id):
    todo = Todo.query.get_or_404(id)
    data = request.get_json()
    
    if 'title' in data:
        if not isinstance(data['title'], str):
            return jsonify({'error': 'Title must be a string'}), 400
        if len(data['title']) < 1:
            return jsonify({'error': 'Title cannot be empty'}), 400
        if len(data['title']) > 500:
            return jsonify({'error': f"Title too long (title length: {len(data['title'])}; maximum 500 characters)"}), 400
        todo.title = data['title']
    
    if 'completed' in data:
        if not isinstance(data['completed'], bool):
            return jsonify({'error': 'Completed must be a boolean'}), 400
        todo.completed = data['completed']

    db.session.commit()
    return jsonify(todo.to_dict())

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, port=5001)