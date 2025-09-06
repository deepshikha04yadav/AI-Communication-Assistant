import axios from 'axios';

export const getEmails = () => axios.get('/api/emails');
export const refreshEmails = () => axios.post('/api/refresh');
