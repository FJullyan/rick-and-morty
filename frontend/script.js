const API_URL = "http://127.0.0.1:5000";
async function buscarPersonagens() {
    const resposta = await fetch(API_URL +"/personagens/dashboard");
    const personagens = await resposta.json();
}