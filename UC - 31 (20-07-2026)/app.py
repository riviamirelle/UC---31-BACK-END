from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

ARQUIVO = "livros.json"


# -----------------------------
# Funções
# -----------------------------

def carregar_livros():

    # Cria o arquivo automaticamente caso não exista
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
            json.dump([], arquivo)

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return []


def salvar_livros(lista_livros):

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(
            lista_livros,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


# -----------------------------
# Cadastro
# -----------------------------

@app.route("/", methods=["GET", "POST"])
def cadastro():

    mensagem = ""

    if request.method == "POST":

        titulo = request.form["titulo"]
        autor = request.form["autor"]
        ano = request.form["ano"]
        categoria = request.form["categoria"]
        quantidade = request.form["quantidade"]

        # Validações

        if not titulo or not autor or not ano or not categoria or not quantidade:
            mensagem = "Preencha todos os campos."

        elif not ano.isdigit():
            mensagem = "O ano deve conter apenas números."

        elif not quantidade.isdigit() or int(quantidade) <= 0:
            mensagem = "A quantidade deve ser maior que zero."

        else:

            livro = {
                "titulo": titulo,
                "autor": autor,
                "ano": ano,
                "categoria": categoria,
                "quantidade": quantidade
            }

            livros = carregar_livros()
            livros.append(livro)
            salvar_livros(livros)

            return redirect(url_for("listar"))

    return render_template(
        "cadastro.html",
        mensagem=mensagem
    )


# -----------------------------
# Listagem
# -----------------------------

@app.route("/livros")
def listar():

    livros = carregar_livros()

    return render_template(
        "livros.html",
        livros=livros
    )


# -----------------------------
# Buscar
# -----------------------------

@app.route("/buscar", methods=["GET", "POST"])
def buscar():

    livro = None
    mensagem = ""

    if request.method == "POST":

        pesquisa = request.form["titulo"].lower()

        livros = carregar_livros()

        for item in livros:

            if item["titulo"].lower() == pesquisa:
                livro = item
                break

        if livro is None:
            mensagem = "Livro não encontrado."

    return render_template(
        "buscar.html",
        livro=livro,
        mensagem=mensagem
    )


# -----------------------------
# Editar
# -----------------------------

@app.route("/editar/<int:indice>", methods=["GET", "POST"])
def editar(indice):

    livros = carregar_livros()

    if request.method == "POST":

        livros[indice]["titulo"] = request.form["titulo"]
        livros[indice]["autor"] = request.form["autor"]
        livros[indice]["ano"] = request.form["ano"]
        livros[indice]["categoria"] = request.form["categoria"]
        livros[indice]["quantidade"] = request.form["quantidade"]

        salvar_livros(livros)

        return redirect(url_for("listar"))

    return render_template(
        "editar.html",
        livro=livros[indice],
        indice=indice
    )


# -----------------------------
# Excluir
# -----------------------------

@app.route("/excluir/<int:indice>")
def excluir(indice):

    livros = carregar_livros()

    livros.pop(indice)

    salvar_livros(livros)

    return redirect(url_for("listar"))


# -----------------------------
# Executar aplicação
# -----------------------------

if __name__ == "__main__":
    app.run(debug=True)