from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", active="home")

@app.route("/quienes_somos")
def quienes_somos():
    return render_template("quienes_somos.html", active="quienes")

@app.route("/que_hacemos")
def que_hacemos():
    return render_template("que_hacemos.html", active="quehacemos")

@app.route("/como_participar")
def como_participar():
    return render_template("como_participar.html", active="participar")

@app.route("/dona")
def dona():
    # MOSTRAR LA MISMA PAGINA QUE COMO PARTICIPAR
    return render_template("como_participar.html", active="participar")

@app.route("/noticias")
def noticias():
    return render_template("noticias.html", active="noticias")

if __name__ == "__main__":
    app.run(debug=True)
