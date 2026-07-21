const API_URL = "http://127.0.0.1:5000";
async function buscarPersonagens() {
    const resposta = await fetch(API_URL +"/personagens/dashboard");
    const personagens = await resposta.json();
    const cards = document.getElementById("cards");
    personagens.forEach(personagem => {
    cards.innerHTML += `
        <div class="col-md-4 mb-4">
            <div class="card">
                <img src="${personagem.image}" class="card-img-top">
                <div class="card-body">
                    <h5 class="card-title">${personagem.name}</h5>
                    <p>Status: ${personagem.status}</p>
                    <p>Espécie: ${personagem.species}</p>
                    <p>Origem: ${personagem.origin}</p>
                    <p>Episódios: ${personagem.total_episodios}</p>
                </div>
            </div>
        </div>
    `;
});
}
buscarPersonagens();