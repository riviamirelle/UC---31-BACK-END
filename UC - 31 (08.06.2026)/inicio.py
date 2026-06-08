from flask import (render_templates, request, make_response, url_for)

app = Flask (__name__)

@app.route('/')
def inicio():

# le comentario 
    tema = request.cookies.get('tema', 'claro')


    return render_template (
        'inicio.html',
        tema=tema

    )  


@app.route('/tema/<escolha>')
def troca_tema(escolha):

    if escolha not in [ 'claro', 'escuro']:
        redirect (url_for('inicio')) 


        reposta.set_cookie(

            'tema',
            escolha,
            max_age=60*60*24*30
        )

        return resposta
    
    if __name__ == '__main__':
        app.run(debug=True)