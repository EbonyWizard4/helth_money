from flask import Flask, render_template, flash, redirect, url_for, request
from werkzeug.utils import secure_filename
import random

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route("/")
def home():
    green_bar_height = 0
    orange_bar_height = 0
    barra = [green_bar_height, orange_bar_height]
    for bar in range(2):
        height = random.randint(10, 90)
        barra[bar] = height
    print(barra)
    return render_template("index.html", green=barra[0], orange=barra[1])

@app.route("/upload")
def upload():
    return render_template("uploade/upload.html")

@app.route("/sobe", methods=['POST'])
def sobe_arquivo():
    if 'file' not in request.files:
        print("\nSobe Arquivo\n")
        flash('Nenhum arquivo selecionado')
        return redirect(url_for("upload"))
    file = request.files['file']
    if file.filename == "":
        print("\nSobe Arquivo\n")
        flash('Nenhum arquivo foi enviado.')
        return redirect(url_for("upload"))
    if file:
        filename = secure_filename(file.filename)
        flash(f'{filename} enviado.')
    return redirect(url_for("home"))

if __name__=="__main__":
    app.run()