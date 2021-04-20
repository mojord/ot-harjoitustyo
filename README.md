
## Dokumentaatio
[Tuntikirjanpito](https://github.com/mojord/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Vaatimusmäärittely](https://github.com/mojord/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuurikuvaus](https://github.com/mojord/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Sovelluksen käyttäminen komentorivillä

### Ohjelman voi suorittaa komennolla:
```bash
poetry run invoke start
```

### Testaaminen
```bash
poetry run invoke test
```

### Testikattavuus
Testikattavuusraportin saa komennolla:
```bash
poetry run invoke coverage-report
```

Raportti generoituu hmtlcov-hakemistoon. Raporttia voi tarkastella selaimessa avaamalla index.html-tiedoston. 

