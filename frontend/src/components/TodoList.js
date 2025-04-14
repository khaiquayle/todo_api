import React, { useState, useEffect } from 'react';
import { 
  List, 
  ListItem, 
  ListItemText, 
  ListItemSecondaryAction,
  IconButton,
  Checkbox,
  Typography,
  Box,
  Paper
} from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';
import EditIcon from '@mui/icons-material/Edit';

const TodoList = () => {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    // Fetch todos from API
  }, []);

  const handleToggle = async (id) => {
    // Implement toggle completion logic
  };

  const handleDelete = async (id) => {
    // Implement delete logic
  };

  const handleEdit = (id) => {
    // Implement edit logic
  };

  return (
    <Box sx={{ maxWidth: 600, margin: '0 auto', mt: 4 }}>
      <Paper elevation={3} sx={{ p: 3 }}>
        <Typography variant="h5" component="h1" gutterBottom>
          Todo List
        </Typography>
        <List>
          {todos.map((todo) => (
            <ListItem key={todo.id} divider>
              <Checkbox
                edge="start"
                checked={todo.completed}
                onChange={() => handleToggle(todo.id)}
              />
              <ListItemText
                primary={todo.title}
                secondary={todo.due_date}
                style={{ textDecoration: todo.completed ? 'line-through' : 'none' }}
              />
              <ListItemSecondaryAction>
                <IconButton edge="end" onClick={() => handleEdit(todo.id)}>
                  <EditIcon />
                </IconButton>
                <IconButton edge="end" onClick={() => handleDelete(todo.id)}>
                  <DeleteIcon />
                </IconButton>
              </ListItemSecondaryAction>
            </ListItem>
          ))}
        </List>
      </Paper>
    </Box>
  );
};

export default TodoList; 