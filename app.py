from flask import Flask
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