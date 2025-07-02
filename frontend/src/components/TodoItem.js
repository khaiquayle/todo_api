import React from 'react';
import { ListItem, Checkbox, IconButton, ListItemText } from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';

const TodoItem = ({ todo, onToggle, onDelete }) => (
  <ListItem
    secondaryAction={
      <IconButton edge="end" aria-label="delete" onClick={() => onDelete(todo.id)}>
        <DeleteIcon />
      </IconButton>
    }
    disablePadding
  >
    <Checkbox
      edge="start"
      checked={todo.completed}
      tabIndex={-1}
      onChange={() => onToggle(todo.id, !todo.completed)}
    />
    <ListItemText primary={todo.title} sx={{ textDecoration: todo.completed ? 'line-through' : 'none' }} />
  </ListItem>
);

export default TodoItem; 