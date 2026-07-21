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

@app.route("/personagens/buscar", methods=["GET"])
def personagens_busca():
    nome = request.args.get("nome")
    resposta = requests.get(f"https://rickandmortyapi.com/api/character/?name={nome}")
    return jsonify(resposta.json())



if __name__ == "__main__":
    app.run(host="0.0.0.0", pot=5000, debug=False)
