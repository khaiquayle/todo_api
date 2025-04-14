import React from 'react';
import { 
  ListItem, 
  ListItemText, 
  ListItemSecondaryAction,
  IconButton,
  Checkbox,
  Typography
} from '@mui/material';
import { Delete as DeleteIcon, Edit as EditIcon } from '@mui/icons-material';

const TodoItem = ({ todo, onToggle, onDelete, onEdit }) => {
  const formatDate = (dateString) => {
    if (!dateString) return '';
    return new Date(dateString).toLocaleDateString();
  };

  return (
    <ListItem>
      <Checkbox
        edge="start"
        checked={todo.completed}
        onChange={() => onToggle(todo.id, !todo.completed)}
      />
      <ListItemText
        primary={
          <Typography
            style={{
              textDecoration: todo.completed ? 'line-through' : 'none'
            }}
          >
            {todo.title}
          </Typography>
        }
        secondary={todo.due_date ? `Due: ${formatDate(todo.due_date)}` : ''}
      />
      <ListItemSecondaryAction>
        <IconButton edge="end" onClick={() => onEdit(todo)}>
          <EditIcon />
        </IconButton>
        <IconButton edge="end" onClick={() => onDelete(todo.id)}>
          <DeleteIcon />
        </IconButton>
      </ListItemSecondaryAction>
    </ListItem>
  );
};

export default TodoItem; 