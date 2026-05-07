from flask import Flask, render_template

# criando a aplicação Flask
app = Flask(__name__)

# rota principal dos filmes
# o <genero> pega o que for digitado na URL
@app.route('/filme/<genero>')
def filme(genero):

    # verificando qual gênero foi escolhido
    if genero == 'acao':
        return render_template('acao.html')

    elif genero == 'comedia':
        return render_template('comedia.html')

    elif genero == 'romance':
        return render_template('romance.html')

    # caso o gênero não exista
    else:
        return render_template('erro.html')


# executa o servidor
if __name__ == '__main__':
    app.run(debug=True)