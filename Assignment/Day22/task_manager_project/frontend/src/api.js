import axios from "axios";

const API = "http://localhost:5000";

export const getTasks = (params) =>
  axios.get(`${API}/tasks`, { params });

export const createTask = (data) =>
  axios.post(`${API}/tasks`, data);

export const toggleTask = (id) =>
  axios.put(`${API}/tasks/${id}`);

export const deleteTask = (id) =>
  axios.delete(`${API}/tasks/${id}`);