import React, { useState } from 'react';
import { TextField, Button, Box } from '@mui/material';

const TodoForm = ({ onAdd }) => {
  const [title, setTitle] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!title.trim()) return;
    onAdd(title);
    setTitle('');
  };

  return (
    <Box component="form" onSubmit={handleSubmit} sx={{ display: 'flex', mb: 2 }}>
      <TextField
        label="New Todo"
        value={title}
        onChange={e => setTitle(e.target.value)}
        fullWidth
        size="small"
      />
      <Button type="submit" variant="contained" sx={{ ml: 2 }}>
        Add
      </Button>
    </Box>
  );
};

export default TodoForm; 