from flask import Flask, jsonify, request
from database import db
from models import Todo, User  # Import User model
from validators import check_date, check_date_format
from datetime import datetime
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'your_jwt_secret_key')  # Use environment variable
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600  # 1 hour
app.config['JWT_ERROR_MESSAGE_KEY'] = 'msg'
jwt = JWTManager(app)
db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "To-Do API is running!"

@app.route('/todos', methods=['GET'])
@jwt_required()
def get_todos():
    current_user_id = int(get_jwt_identity())  # Convert string ID back to integer
    todos = Todo.query.filter_by(user_id=current_user_id).all()
    return jsonify([todo.to_dict() for todo in todos])

@app.route('/todos', methods=['POST'])
@jwt_required()
def post_todos():
    current_user_id = int(get_jwt_identity())  # Convert string ID back to integer
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    if not isinstance(data['title'], str):
        return jsonify({'error': 'Title must be a string'}), 400
    if len(data['title']) < 1:
        return jsonify({'error': 'Title cannot be empty'}), 400
    if len(data['title']) > 500:
        return jsonify({'error': f"Title too long (title length: {len(data['title'])}; maximum 500 characters)"}), 400

    due_date = None
    if 'due_date' in data and data['due_date'] is not None:
        if not (check_date_format(data['due_date']) and check_date(data['due_date'])):
            return jsonify({'error': 'Due date is invalid'}), 400
        due_date = datetime.strptime(data['due_date'], '%Y-%m-%d')  # Convert to datetime

    new_todo = Todo(title=data['title'], due_date=due_date, user_id=current_user_id)  # Set user_id here
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(new_todo.to_dict()), 201

@app.route('/todos/<int:id>', methods=['GET'])
@jwt_required()
def get_todo(id):
    current_user_id = int(get_jwt_identity())  # Convert string ID back to integer
    todo = Todo.query.filter_by(id=id, user_id=current_user_id).first_or_404()
    return jsonify(todo.to_dict())

@app.route('/todos/<int:id>', methods=['PUT'])
@jwt_required()
def put_todo(id):
    current_user_id = int(get_jwt_identity())  # Convert string ID back to integer
    todo = Todo.query.filter_by(id=id, user_id=current_user_id).first_or_404()
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

    if 'due_date' in data:
        if data['due_date'] is not None:
            if not (check_date_format(data['due_date']) and check_date(data['due_date'])):
                return jsonify({'error': 'Due date is invalid'}), 400
            todo.due_date = datetime.strptime(data['due_date'], '%Y-%m-%d')  # Convert to datetime
        else:
            todo.due_date = None  # Allow clearing due_date with None

    db.session.commit()
    return jsonify(todo.to_dict())

@app.route('/todos/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_todo(id):
    current_user_id = int(get_jwt_identity())  # Convert string ID back to integer
    todo = Todo.query.filter_by(id=id, user_id=current_user_id).first_or_404()
    db.session.delete(todo)
    db.session.commit()
    return '', 204

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'msg': 'Username and password are required'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'msg': 'User already exists'}), 400

    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'msg': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'msg': 'Username and password are required'}), 400

    user = User.query.filter_by(username=username).first()
    
    if not user or not user.check_password(password):
        return jsonify({'msg': 'Bad username or password'}), 401

    access_token = create_access_token(identity=str(user.id))  # Convert user.id to string
    return jsonify(access_token=access_token), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)