from flask import Flask, session, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = "chave_secreta"

@app.route("/")
def inicio():
    return redirect(url_for("contador"))

@app.route("/contador")
def contador():
    session['contador'] = session.get('contador', 0) + 1
    return render_template(
        "contador.html",
        contador=session['contador']
    )

@app.route("/zerar", methods=["POST"])
def zerar_contador():
    session.pop('contador', None)
    return redirect(url_for('contador'))

if __name__ == "__main__":
    app.run(debug=True)