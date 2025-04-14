import axios from 'axios';

const API_URL = 'http://localhost:5001';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add token to requests if it exists
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Add response interceptor for better error handling
api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('API Error:', error.response?.data || error.message);
    return Promise.reject(error.response?.data || error);
  }
);

// Example API functions - implement these yourself
export const login = async (username, password) => {
  // Implement login API call
};

export const register = async (username, password) => {
  // Implement register API call
};

export const getTodos = async () => {
  // Implement get todos API call
};

export const createTodo = async (todo) => {
  // Implement create todo API call
};

export const updateTodo = async (id, todo) => {
  // Implement update todo API call
};

export const deleteTodo = async (id) => {
  // Implement delete todo API call
};

export default api; 