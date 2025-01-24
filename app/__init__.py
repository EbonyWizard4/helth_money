from flask import Flask, render_template, flash, redirect, url_for, request
from werkzeug.utils import secure_filename
from pypdf import PdfReader
import random
import os
import re

app = Flask(__name__)
app.secret_key = "mysecretkey"
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    green_bar_height = 0
    orange_bar_height = 0
    barra = [green_bar_height, orange_bar_height]
    for bar in range(2):
        height = random.randint(10, 90)
        barra[bar] = height
    print(barra)
    return render_template("index/home.html", green=barra[0], orange=barra[1])

# Leitura de PDF
def read_pdf(filepath):
    with open(filepath, 'rb') as file:
        reader = PdfReader(file)
        text = ''.join(page.extract_text() for page in reader.pages)
        # text = ''.join(page.extract_text() for page in reader.pages)
    return text

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
        # salva o arquivo selecionado no diretorio de uploads
        filename = secure_filename(file.filename)
        flash(f'{filename} enviado.')
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Captura o texto do arquivo selecionado.
        text = read_pdf(filepath)
  
    return redirect(url_for("upload"))

if __name__=="__main__":
    app.run()