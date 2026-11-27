# Aarrejahti

## Tiimin jäsenet

- Eino Ojala, Aapo Hannikainen, Usman Ahmad ja Liul Getachew

## Peli-idea ja tavoite

**Aarrejahti** 
- Peli on kahden pelaajan korttipeli. Sen tavoitteena on saada kolme pistettä keräämällä kolikoita, varastamalla niitä muilta tai löytämällä kultaharkon.

**Pelin kulku**
- Peli aloitetaan niin, että pelaajat kirjoittavat nimensä etusivulla oleviin syöttökenttiin. 
- Tämän jälkeen painetaan Aloita peli painiketta. 
- Pelaajat kääntävät vuorotellen kortteja. 
- Kortin vaikutus toteutuu heti nostamisen jälkeen.

**Eri kortit:**
- Kolikko: Saat yhden pisteen.
- Kultaharkko: Voitat pelin heti.
- Huti: Mitään ei tapahdu.
- Rosvo: Menetät yhden pisteet, jos on pisteitä.
- Ryöstöretki: Saat vastustajalta yhden pisteet, jos hänellä on pisteitä.

**Voittaminen**
- Pelin voittaa saamalla kolme pistettä, joko löytämällä kolikkoja tai varastamalla kolikoita toiselta pelaajalta.
- Jos löytää kultaharkon voittaa heti. Kultaharkkoja on pelissä vain yksi kappale.

**Kestävän kehtyksen tavoite**
- Peli liittyy kestävän kehityksen tavoitteeseen 1.Ei köyhyyttä (poistaa köyhyys kaikissa sen muodoissa). Pelin kolikot kuvaavat taloudellisia resursseja, joita tarvitaan ihmisten toimeentuloon. Pelissä on kolikoita, joita kerätään ja menetetään, mikä kuvastaa taloudellisen tilanteen vaihtelua ja rahan merkitystä.

## Tärkeimmät ominaisuudet ja toiminnallisuus
- Pelissä on kaksi pelaajaa, jotka antavat itselleen nimet pelin etusivulla ennen kuin peli aloitetaan.
- Pelissä on yhteensä 50 korttia, jotka sekoitetaan satunnaiseen järjestykseen. Pelaajat kääntävät kortteja vuorotellen.
- Pelissä näytetään viestejä, jotka kertovat, mitä kortin nostamisesta tapahtui.
- Korttien vaikutukset päivittävät pelaajien pisteitä pelin aikana.
- Pelaajien nimet, pisteet ja pelin vuoro näytetään pelisivulla.
- Pelaaja voittaa, kun hän saa kolme pistettä tai löytää kultaharkon.
- Pelin tiedot tallennetaan game_data.json-tiedostoon.

## Käytetyt teknologiat
- Python: Pelin toiminnallisuus ja pelin tietojen käsittely.
- Flask: Verkkosovelluksen toteuttaminen ja eri sivujen välillä liikkuminen.
- HTML: Verkkosivujen rakenteen luominen.
- CSS: Verkkosivujen ulkoasun ja tyylien muokkaaminen.
- JavaScript: Pelin toiminnallisuus selaimessa, esim. korttien valitseminen ja tietojen näyttäminen.
- JSON: Pelin tiedot tallennetaan game_data.json-tiedostoon.

## Ohjeet sovelluksen käynnistämiseen


## Lyhyt kuvaus työnjaosta
Työnjako peliprojektissa:
- Liul keskittyi index.html ja main.js tiedostoihin.
- Usman keskittyi instructions.html ja main.js tiedostoihin.
- Aapo keskittyi game.html ja game.js tiedostoihin.
- Eino keskittyi app.py, style.css ja game_data.json tiedostoihin.
- Jokaisella oli myös mahdollisuus muokata jokaisen tiedostoja, jos huomasi niissä jotain paranneltavaa tai jos keksi tavan tehdä koodin paremmalla/helpommalla tavalla.