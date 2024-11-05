from flask import Flask
 

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Flask configurado com sucesso</h1>'

@app.route('api/eventos/')
def listar_eventos():
    return 'abc'


if __name__ == "__name__":
    app.run()