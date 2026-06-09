from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)

@app.route("/")
def inicio():
    nome = request.cookies.get("nome")
    tema = request.cookies.get("tema", "claro")

    return render_template(
        "inicio.html",
        nome=nome,
        tema=tema
    )


@app.route("/salvar_nome", methods=["POST"])
def salvar_nome():
    nome = request.form["nome"].strip().title()

    resposta = make_response(redirect(url_for("inicio")))
    resposta.set_cookie("nome", nome, max_age=60 * 60 * 24 * 30)

    return resposta


@app.route("/tema/<modo>")
def mudar_tema(modo):

    if modo not in ["claro", "escuro"]:
        return redirect(url_for("inicio"))

    resposta = make_response(redirect(url_for("inicio")))
    resposta.set_cookie("tema", modo, max_age=60 * 60 * 24 * 30)

    return resposta


if __name__ == "__main__":
    app.run(debug=True)