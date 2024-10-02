from flask import Flask, jsonify, request

app = Flask(__name__)
musicas = [
    {
        "titulo": "goodbye",
        "autor": "arezra",
        'genero': 'house'
    },
    {
        "titulo": 'night drive',
        "autor": "arezra",
        'genero': 'house'
    },
    {
        "titulo": "run to the hills",
        "autor": "iron maiden",
        'genero': 'rock'
    },
]

@app.route('/')
def push():
    return jsonify(musicas)

@app.route('/musica/<int:index>', methods=['GET'])
def obter_musicas(index):
    return jsonify(musicas[index], 200)

@app.route('/musica', methods=['POST'])
def inserir_musica():
    musica = request.get_json()
    musicas.append(musica)
    return jsonify(musica,200)

@app.route('/musica/<int:index>', methods=['PUT'])
def alterar_musica(index):
    musica = request.get_json()
    musicas[index].update(musica)
    return jsonify(musicas[index])

@app.route('/musica/<int:index>', methods=['DELETE'])
def deletar_musica(index):
    if musicas[index] is not None:
        del musicas[index]
        return jsonify(f'deletado com sucesso', 200)
    return jsonify('ocorreu um problema nao existe essa musica', 404)

    

app.run(port=5000,host='localhost',debug=True)
