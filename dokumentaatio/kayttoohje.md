# Käyttöohje

Ohjelma on tarkoitettu osteoarkeologisten raporttien tarvitsemien taulukoiden, kuvaajien ja laskennan suorittamiseen.

## Käynnistäminen

Asenna riippuvuudet komennolla:

```bash
poetry install
```

Tämän jälkeen ohjelman voi käynnistää komennolla:

```bash
poetry run invoke start
```

## Käyttö

Sovellus käynnistyy näkymään, joka sisältää toimintonappulat ja laatikot syötteitä varten.
Aloitus tapahtuu antamalla käsiteltävän csv-tiedoston nimi ja klikkaamalla syötelaatikon vieressä olevaa painiketta.

Tämän jälkeen tiedostosta voidaan laskea tilastoja ja tuottaa graafeja painamalla haluttuja painikkeita tai antamalla syötteitä. Tulostus tapahtuu konsoliin.
