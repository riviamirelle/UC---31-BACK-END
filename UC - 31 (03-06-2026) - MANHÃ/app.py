from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cadastro", methods=["POST"])
def cadastro():

    nome = request.form["nome"].strip().title()
    email = request.form["email"].strip().lower()
    telefone = request.form["telefone"].strip()
    cpf = request.form["cpf"].strip()
    cidade = request.form["cidade"].strip().title()
    estado = request.form["estado"].strip().upper()
    curso = request.form["curso"].strip()
    idade = request.form["idade"].strip()
    senha = request.form["senha"].strip()

    # telefone
    telefone = telefone.replace("(", "")
    telefone = telefone.replace(")", "")
    telefone = telefone.replace("-", "")
    telefone = telefone.replace(" ", "")

    # cpf
    cpf = cpf.replace(".", "")
    cpf = cpf.replace("-", "")

    # campos obrigatórios
    if not all([nome, email, telefone, cpf,
                cidade, estado, curso,
                idade, senha]):

        return render_template(
            "resultado.html",
            mensagem="Preencha todos os campos obrigatórios.",
            sucesso=False
        )

    if len(estado) != 2 or not estado.isalpha():
        return render_template(
        "resultado.html",
        mensagem="Estado inválido.",
        sucesso=False
    )

    if "@" not in email or ".com" not in email:
        return render_template(
            "resultado.html",
            mensagem="E-mail inválido.",
            sucesso=False
        )

    if len(telefone) != 11 or not telefone.isdigit():
        return render_template(
            "resultado.html",
            mensagem="Telefone inválido.",
            sucesso=False
        )

    if len(cpf) != 11 or not cpf.isdigit():
        return render_template(
            "resultado.html",
            mensagem="CPF inválido.",
            sucesso=False
        )

    if len(cidade) < 3:
        return render_template(
            "resultado.html",
            mensagem="Cidade inválida.",
            sucesso=False
        )

    if len(estado) != 2 or not estado.isalpha():
        return render_template(
            "resultado.html",
            mensagem="Estado inválido.",
            sucesso=False
        )

    if not idade.isdigit():
        return render_template(
            "resultado.html",
            mensagem="Idade inválida.",
            sucesso=False
        )

    if int(idade) < 16:
        return render_template(
        "resultado.html",
        mensagem="Idade inválida.",
        sucesso=False
        )

    if len(senha) < 8 or not any(car.isdigit() for car in senha):
        return render_template(
            "resultado.html",
            mensagem="Senha muito fraca.",
            sucesso=False
        )

    return render_template(
        "resultado.html",
        mensagem="Cadastro realizado com sucesso!",
        sucesso=True,
        nome=nome,
        email=email,
        telefone=telefone,
        cpf=cpf,
        cidade=cidade,
        estado=estado,
        curso=curso,
        idade=idade
    )


if __name__ == "__main__":
    app.run(debug=True)