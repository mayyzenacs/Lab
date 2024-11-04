from flask import Flask
 

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Flask configurado com sucesso</h1>'


if __name__ == "__name__":
    app.run()