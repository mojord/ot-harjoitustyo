# Arkkitehtuurikuvaus

## Pakkausrakenne

![rakenne](.kuvat/architecture.png)


Kuvassa esitetään tavoitteena oleva pakkausrakenne, jossa ui sisältää sekä tekstikäyttöliitymän että graafisen käyttöliittymän. Application-pakkaus sisältää sovelluslogiikan ja sen käyttämän luokan. Repositories-pakkaukseen tulee pysyväistallennus. Tällä hetkellä sovelluslogiikka, luokka ja käyttöliittymä ovat vielä src-kansiossa.
