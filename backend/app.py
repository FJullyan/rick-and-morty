from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)

CORS(app)

@app.route("/personagens", methods=["GET"])
def lista_personagens():
    resposta = requests.get("https://rickandmortyapi.com/api/character")
    personagens = resposta.json()
    return jsonify(personagens)

@app.route("/personagens/dashboard", methods=["GET"])
def personagens_dashboard():
    nomes = ["rick", "summer", "beth", "morty", "jerry"]
    personagens = []
    for nome in nomes:
        resposta = requests.get(f"https://rickandmortyapi.com/api/character/?name={nome}")
        personagem = resposta.json()["results"][0]
        personagens.append({
        "name": personagem["name"],
        "status": personagem["status"],
        "species": personagem["species"],
        "gender": personagem["gender"],
        "image": personagem["image"],
        "origin": personagem["origin"]["name"],
        "total_episodios": len(personagem["episode"])
    })
    return jsonify(personagens)

if __name__ == "__main__":
    app.run(debug=True)
