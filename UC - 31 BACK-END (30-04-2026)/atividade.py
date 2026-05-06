from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    return 'OLAAAAAAAAA'

#ATIVIDADE 1

#QUESTÃO 1

@app.route('/arearestrita/<int:id>')
def arearestrita(id):
    if id == 1:
        return "CADEADO FECHADO"
    elif id == 2: 
        return "CADEADO ABERTO" 
    else: 
        return "ID INVALIDO"
    

#QUESTÃO 2 

@app.route('/operacao/<tipo>/<int:n1>/<int:n2>')
def operacao(tipo, n1, n2):
    if tipo == "sum":
        resultado = n1 + n2
    elif tipo == "sub":
        resultado = n1 - n2
    elif tipo == "mult":
        resultado = n1 * n2
    elif tipo == "div":
        if n2 == 0:
            return "ERRO: DIVISÃO POR ZERO"
        resultado = n1 / n2
    else:
        return "TIPO DE OPERAÇÃO INVÁLIDO"

    return str(resultado)

#ATIVIDADE 2

#QUESTÃO 1 

@app.route('/ola/<nome>')
def ola(nome):
    nome= "Rivia"
    return  f"Ola, {nome}! Seja bem-vinda ao sistema"


#QUESTÃO 2 

@app.route('/calculo/<int:n1>/<int:n2>')
def calculo(n1, n2):
    resultado = n1 + n2
    return f"A soma de {n1} +{n2} é {resultado}"

#QUESTÃO 4 

@app.route('/produto/<nome>/<float:preco>')
def produto(nome, preco):
    return f"O produto {nome} custa R$ {preco:.2f}"

if __name__ == "__main__":
    app.run(debug=True)
