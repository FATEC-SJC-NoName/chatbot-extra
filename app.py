from chatbot import chatbotfatecano
from flask import Flask, render_template, request


app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_resposta():
    mensagemUsuario = request.args.get("msg")
    return str(chatbotfatecano.get_response(mensagemUsuario))

if __name__ == "__main__":
    app.run()