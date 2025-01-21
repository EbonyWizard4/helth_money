from flask import Flask, render_template
import random

app = Flask(__name__)

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

if __name__=="__main__":
    app.run()