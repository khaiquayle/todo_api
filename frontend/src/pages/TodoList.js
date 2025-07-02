import React, { useEffect, useState } from 'react';
import { List, Paper, Typography, Box } from '@mui/material';
import TodoForm from '../components/TodoForm';
import TodoItem from '../components/TodoItem';
import { fetchTodos, addTodo, updateTodo, deleteTodo } from '../services/api';
import { useAuth } from '../context/AuthContext';
import { useNavigate } from 'react-router-dom';

const TodoList = () => {
    const [todos, setTodos] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');
    const { token, logout } = useAuth();
    const navigate = useNavigate();

    const loadTodos = async () => {
        setLoading(true);
        try {
            const data = await fetchTodos(token);
            setTodos(Array.isArray(data) ? data : (data.todos || []));
        } catch (err) {
            if (err.message && (err.message.includes('401') || err.message.includes('403'))) {
                logout();
                navigate('/login');
            } else {
                setError('Failed to fetch todos');
            }
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        loadTodos();
        // eslint-disable-next-line
    }, []);

    const handleAdd = async (title) => {
        try {
            await addTodo(token, title);
            loadTodos();
        } catch (err) {
            setError('Failed to add todo');
        }
    };

    const handleToggle = async (id, completed) => {
        try {
            await updateTodo(token, id, { completed });
            setTodos(todos => todos.map(todo => todo.id === id ? { ...todo, completed } : todo));
        } catch (err) {
            setError('Failed to update todo');
        }
    };

    const handleDelete = async (id) => {
        try {
            await deleteTodo(token, id);
            loadTodos();
        } catch (err) {
            setError('Failed to delete todo');
        }
    };

    if (loading) return <div>Loading...</div>;
    if (error) return <div>{error}</div>;

    return (
        <Box sx={{ maxWidth: 600, mx: 'auto', mt: 4 }}>
            <Paper sx={{ p: 3 }}>
                <Typography variant="h4" gutterBottom>My Todos</Typography>
                <TodoForm onAdd={handleAdd} />
                <List>
                    {todos.length === 0 ? (
                        <Typography color="text.secondary">No todos found.</Typography>
                    ) : (
                        todos.map(todo => (
                            <TodoItem
                                key={todo.id}
                                todo={todo}
                                onToggle={handleToggle}
                                onDelete={handleDelete}
                            />
                        ))
                    )}
                </List>
            </Paper>
        </Box>
    );
};

export default TodoList;