from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Olá FIAP - Este é o Lab07 de Cloud rodando na AWS</h1>\nMBA! o/"
