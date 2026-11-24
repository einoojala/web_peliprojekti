from flask import Flask, render_template
import random
import json

app = Flask(__name__)
data = "game_data.json"
# Tallentaa pelin tiedot
def tallenna_peli(peli):
    with open(data, "w", encoding="utf-8") as tiedosto:
        json.dump(peli, tiedosto, ensure_ascii=False, indent=4)

# Lukee pelin tiedot
def hae_peli():
    with open(data, "r", encoding="utf-8") as tiedosto:
        peli = json.load(tiedosto)
    return peli

# Luo kaikki pelin 50 korttia ja sekoittaa 
def luo_kortit():
    kortit = []
    # 12 kolikkokorttia
    for i in range(12):
        kortit.append({
            "id": len(kortit),
            "nimi": "Kolikko",
            "tyyppi": "kolikko",
            "naytetty": False
        })
    # 1 kultaharkkokortti
    kortit.append({
        "id": len(kortit),
        "nimi": "Kultaharkko",
        "tyyppi": "kulta",
        "naytetty": False
    })
    # 23 tyhjää korttia
    for i in range(23):
        kortit.append({
            "id": len(kortit),
            "nimi": "Huti",
            "tyyppi": "huti",
            "naytetty": False
        })
    # 7 rosvokorttia
    for i in range(7):
        kortit.append({
            "id": len(kortit),
            "nimi": "Rosvo",
            "tyyppi": "rosvo",
            "naytetty": False
        })
    # 7 ryöstöretkikorttia
    for i in range(7):
        kortit.append({
            "id": len(kortit),
            "nimi": "Ryöstöretki",
            "tyyppi": "ryosto",
            "naytetty": False
        })
    random.shuffle(kortit)
    return kortit

# Muodostaa pelistä tiedot, jotka voidaan lähettää JavaScriptille
def pelin_naytettavat_tiedot(peli):
    kortit = []
    for kortti in peli["kortit"]:
        if kortti["naytetty"]:
            # Näytetään kortin kaikki tiedot, jos se on jo valittu
            kortit.append(kortti)
        else:
            # Piilotetaan kortin nimi, jos sitä ei ole vielä valittu
            kortit.append({
                "id": kortti["id"],
                "naytetty": False
            })
    tiedot = {
        "pelaajat": peli["pelaajat"],
        "vuoro": peli["vuoro"],
        "kortit": kortit,
        "peli_loppu": peli["peli_loppu"],
        "voittaja": peli["voittaja"],
        "viesti": peli["viesti"]
    }
    return tiedot

@app.route("/aarrejahti/etusivu")
def etusivu():
    return render_template("index.html")

@app.route("/aarrejahti/peli")
def pelisivu():
    return render_template("game.html")

@app.route("/aarrejahti/ohjeet")
def ohjesivu():
    return render_template("instructions.html")
