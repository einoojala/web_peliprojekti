from flask import Flask, render_template
import random
import json

app = Flask(__name__)
data = "game_data.json"

# tallennetaan pelin tiedot
def tallenna_peli(peli):
    with open(data, "w", encoding="utf-8") as tiedosto:
        json.dump(peli, tiedosto, ensure_ascii=False, indent=4)

# Haetaan pelin tiedot
def hae_peli():
    with open(data, "r", encoding="utf-8") as tiedosto:
        return json.load(tiedosto)

# Aloitussivu
@app.route("/")
def etusivu():
    return render_template("index.html")

# Pelisivu
@app.route("/game")
def pelisivu():
    return render_template("game.html")

# Ohjesivu
@app.route("/instructions")
def ohjesivu():
    return render_template("instructions.html")