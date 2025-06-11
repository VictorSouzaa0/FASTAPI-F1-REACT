import axios from "axios";

const API_BASE_URL = "http://localhost:8000";

export const getTeams = () => axios.get(`${API_BASE_URL}/teams`);
export const getTeam = (id) => axios.get(`${API_BASE_URL}/teams/${id}`);
export const createTeam = (data) => axios.post(`${API_BASE_URL}/teams`, data);
export const updateTeam = (id, data) => axios.put(`${API_BASE_URL}/teams/${id}`, data);
export const deleteTeam = (id) => axios.delete(`${API_BASE_URL}/teams/${id}`);

export const getDrivers = () => axios.get(`${API_BASE_URL}/drivers`);
export const getDriver = (id) => axios.get(`${API_BASE_URL}/drivers/${id}`);
export const createDriver = (data) => axios.post(`${API_BASE_URL}/drivers`, data);
export const updateDriver = (id, data) => axios.put(`${API_BASE_URL}/drivers/${id}`, data);
export const deleteDriver = (id) => axios.delete(`${API_BASE_URL}/drivers/${id}`);

export const getDriversByTeam = (teamId) => axios.get(`${API_BASE_URL}/teams/${teamId}/drivers`);