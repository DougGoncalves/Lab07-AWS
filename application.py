from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Olá FIAP - Este é o Lab06 Rodando na Azure</h1>\nMBA! o/"
