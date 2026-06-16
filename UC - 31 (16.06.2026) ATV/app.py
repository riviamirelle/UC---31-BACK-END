from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# SECRET_KEY obrigatória para usar sessions
app.secret_key = "segredo_login_flask"

# Credenciais fixas
USUARIO_CORRETO = "admin"
SENHA_CORRETA = "1234"


# Página Inicial
@app.route("/")
def index():
    return render_template("index.html")


# Login
@app.route("/login", methods=["GET", "POST"])
def login():

    mensagem_erro = None

    if request.method == "POST":

        usuario = request.form["usuario"]
        senha = request.form["senha"]

        if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:

            # Armazenando usuário na session
            session["usuario"] = usuario

            return redirect(url_for("dashboard"))

        else:
            mensagem_erro = "Usuário ou senha inválidos."

    return render_template("login.html", erro=mensagem_erro)


# Área Restrita
@app.route("/dashboard")
def dashboard():

    # Proteção da rota
    if "usuario" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        usuario=session["usuario"]
    )


# Logout
@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)