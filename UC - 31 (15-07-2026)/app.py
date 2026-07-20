from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Variáveis globais (permitidas para esta atividade)
usuario_cadastrado = ""
senha_hash = ""


# Página de cadastro
@app.route("/", methods=["GET", "POST"])
def cadastro():

    global usuario_cadastrado
    global senha_hash

    if request.method == "POST":

        usuario_cadastrado = request.form["nome"]
        senha = request.form["senha"]

        # Gera o hash da senha
        senha_hash = generate_password_hash(senha)

        return redirect(url_for("login"))

    return render_template("cadastro.html")


# Página de login
@app.route("/login", methods=["GET", "POST"])
def login():

    mensagem = ""

    if request.method == "POST":

        nome = request.form["nome"]
        senha = request.form["senha"]

        # Verifica usuário
        if nome != usuario_cadastrado:
            mensagem = "Usuário não encontrado."

        # Verifica senha
        elif not check_password_hash(senha_hash, senha):
            mensagem = "Senha inválida."

        else:
            return redirect(url_for("inicio"))

    return render_template("login.html", mensagem=mensagem)


# Página inicial
@app.route("/inicio")
def inicio():

    return render_template("inicio.html", nome=usuario_cadastrado)


if __name__ == "__main__":
    app.run(debug=True)
