from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'FOSW3$2dIO98%W'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///musicas.db'

db = SQLAlchemy(app)
db:SQLAlchemy

class Musicas(db.Model):
    __tablename__ = 'musicas'
    id_musica = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))

class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    musicas = db.relationship('musicas')

db.drop_all()
db.create_all()
autor = Autor(nome='AREZRA',email='arezra@gmail.com',senha='1234', admin=True)


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

@app.route('/musica', methods=['GET'])
def push():
    return jsonify(musicas)

@app.route('/musica/<int:index>', methods=['GET'])
def obter_musicas(index):
    return jsonify(musicas[index]), 200

@app.route('/musica', methods=['POST'])
def inserir_musica():
    musica = request.get_json()
    musicas.append(musica)
    return jsonify(musica), 201

@app.route('/musica/<int:index>', methods=['PUT'])
def alterar_musica(index):
    musica = request.get_json()
    musicas[index].update(musica)
    return jsonify(musicas[index])

@app.route('/musica/<int:index>', methods=['DELETE'])
def deletar_musica(index):
    try:
        del musicas[index]
        return jsonify(f'deletado com sucesso'), 200
    except:
        return jsonify('ocorreu um problema nao existe essa musica'), 404

    
if __name__ == '__main__':
    app.run(port=5000,host='localhost',debug=True)
