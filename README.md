# Boneator

Sovelluksella voidaan tuottaa tilastoja ja kuvaajia osteoarkeologista raporttia varten.

## Dokumentaatio
[Tuntikirjanpito](https://github.com/mojord/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Vaatimusmäärittely](https://github.com/mojord/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuurikuvaus](https://github.com/mojord/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Käyttöohje](https://github.com/mojord/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Testausdokumentti](https://github.com/mojord/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)

## Sovelluksen käyttäminen komentorivillä

### Riippuvuuksien asentaminen:
```bash
poetry install
```

### Ohjelman voi suorittaa komennolla:
```bash
poetry run invoke start
```

### Testaaminen
```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuus kerätään komennolla:
```bash
poetry run invoke coverage
```

Testikattavuusraportin saa generoitua komennolla:
```bash
poetry run invoke coverage-report
```

Raportti generoituu hmtlcov-hakemistoon. Raporttia voi tarkastella selaimessa avaamalla index.html-tiedoston. 

### Pylint

Tiedostossa .pylintrc määritellyn koodintarkastuksen voi suorittaa komennolla:
```bash
poetry run invoke lint
```

Pylintin huomautukset liittyvät yksinomaan Bone-luokan attribuuttien määrään, joka on sovellukselle välttämätön. Koska ei saatu vastausta kysymykseen, voiko tarkistuksen kytkeä pois päältä näissä kohdissa, sitä ei tehty.
