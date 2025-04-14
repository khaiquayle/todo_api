import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { CssBaseline, Container } from '@mui/material';

// Import your components here
// import Login from './components/Login';
// import Register from './components/Register';
// import TodoList from './components/TodoList';

function App() {
  return (
    <>
      <CssBaseline />
      <Container>
        <Router>
          <Routes>
            {/* Add your routes here */}
            {/* <Route path="/login" element={<Login />} /> */}
            {/* <Route path="/register" element={<Register />} /> */}
            {/* <Route path="/todos" element={<TodoList />} /> */}
            <Route path="/" element={<div>Welcome to Todo App</div>} />
          </Routes>
        </Router>
      </Container>
    </>
  );
}

export default App;
