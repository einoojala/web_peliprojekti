from flask import Flask, render_template, jsonify, request
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

# Aloitta uuden pelin
@app.route("/api/start", methods=["POST"])
def aloita_peli():
    tiedot = request.get_json()
    # Tarkistetaan, että nimet on annettu
    if not tiedot or "player1" not in tiedot or "player2" not in tiedot:
        return jsonify({"error": "Kirjoita molempien pelaajien nimet."}), 400
    nimi1 = tiedot["player1"].strip()
    nimi2 = tiedot["player2"].strip()

    if nimi1 == "" or nimi2 == "":
        return jsonify({"error": "Kirjoita molempien pelaajien nimet."}), 400
    if nimi1.lower() == nimi2.lower():
        return jsonify({"error": "Pelaajilla pitää olla eri nimet."}), 400

    #luodaan uusi korttipakka
    kortit = luo_kortit()
    #luodaan uuden pelin tiedot
    peli = {
        "pelaajat": [
            {"nimi": nimi1, "kolikot": 0},
            {"nimi": nimi2, "kolikot": 0}
        ],
        "vuoro": 0,
        "kortit": luo_kortit,
        "peli_loppu": False,
        "voittaja": "",
        "viesti": "Peli alkaa!"
    }
    #tallennetaan uusi peli tiedoston
    tallenna_peli(peli)
    return jsonify(pelin_naytettavat_tiedot(peli))

#hakee käynnissä olevan pelin tiedot
@app.route("/api/select", methods=["POST"])
def valitse_kortit():
    try:
        peli = hae_peli()
    except (FileNotFoundError, json.JSONDecodeError):
        return jsonify({"error": "Peliä ei ole vielä aloitettu."}), 400
    return jsonify(pelin_naytettavat_tiedot(peli))

#Käsittelee pelaajan valitseman kortin
@app.route("/api/select", methods=["POST"])
def valitse_kortti():
    try:
        peli = hae_peli()
    except (FileNotFoundError, json.JSONDecodeError):
        return jsonify({"error": "Peliä ei ole vielä aloitettu."}), 400
    # Tarkistetaan, onko peli jo päättynyt
    if peli["peli_loppu"]:
        return jsonify({"error": "Peli on jo päättynyt."}), 400
    tiedot = request.get_json()

    #tarkistetaan että pyynnössö oi korti tunnisdte
    if not tiedot or "card_id" not in tiedot:
        return jsonify({"error": "Kortin tietoja ei saatu."}), 400
    kortin_id = tiedot["card_id"]
    # Etsitään kortti sen tunnisteen perusteella
    valittu_kortti = None

    for kortti in peli["kortit"]:
        if kortti["id"] == kortin_id:
            valittu_kortti = kortti
            break

    # Tarkistetaan, löytyikö kortti
    if valittu_kortti is None:
        return jsonify({"error": "Korttia ei löytynyt."}), 400
    #rkistetaan, onko kortti jo käännetty
    if valittu_kortti["naytetty"]:
        return jsonify({"error": "Tämä kortti on jo valittu."}), 400

    # kenen vuoro on
    pelaaja = peli["pelaajat"][peli["vuoro"]]
    # Selvitetään toinen pelaaja
    vastustaja = peli["pelaajat"][1 - peli["vuoro"]]
    #äännetään valittu kortti näkyviin
    valittu_kortti["naytetty"] = True

    # tarkastetaan, mitä valittu kortti tekee
    if valittu_kortti["tyyppi"] == "kolikko":
        pelaaja["kolikot"] += 1
        viesti = pelaaja["nimi"] + " sai yhden kolikon!"

    elif valittu_kortti["tyyppi"] == "kulta":
        peli["peli_loppu"] = True
        peli["voittaja"] = pelaaja["nimi"]
        viesti = pelaaja["nimi"] + " löysi kultaharkon ja voitti!"
    elif valittu_kortti["tyyppi"] == "rosvo":
        if pelaaja["kolikot"] > 0:
            pelaaja["kolikot"] -= 1
            viesti = "Rosvo vei yhden kolikon!"
        else:
            viesti = "Rosvo ei löytänyt kolikkoa."
    elif valittu_kortti["tyyppi"] == "ryosto":
        if vastustaja["kolikot"] > 0:
            vastustaja["kolikot"] -= 1
            pelaaja["kolikot"] += 1
            viesti = "Sait yhden kolikon vastustajalta!"
        else:
            viesti = "Ryöstöretki ei onnistunut."
    








if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, use_reloader=True)