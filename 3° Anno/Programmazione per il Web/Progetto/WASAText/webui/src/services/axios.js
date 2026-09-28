import axios from "axios";

const backendUrl = `http://${window.location.hostname}:3000`;
const instance = axios.create({
	baseURL: backendUrl,
	timeout: 1000 * 5
});

// Recuperiamo il token/ID se l'utente aveva già fatto login in passato
const savedId = localStorage.getItem('userId');
if (savedId) {
    // CORREZIONE: Aggiungiamo il prefisso "Bearer "
    instance.defaults.headers.common['Authorization'] = 'Bearer ' + savedId;
}

export default instance;