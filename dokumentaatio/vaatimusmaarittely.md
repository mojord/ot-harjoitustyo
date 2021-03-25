# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on tarkoitettu arkeologisen luuanalyysin työkaluksi, joka tuottaa osteologisiin
raportteihin ja tutkimusartikkeleihin tarvittavia tilastoja kuvaajineen.


## Taustatietoa

Arkeologisilla kaivauksilla löytyvä luuaineisto annetaan osteoarkeologin tutkittavaksi.
Osteoarkeologi selvittää luufragmenteista niin paljon kuin morfologian perusteella voi.
Fragmentin ominaisuuksista riippuen voidaan määrittää usein eläimen luokka, sen jälkeen
mahdollisesti anatominen osa ja parhaassa tapauksessa eläinlaji. Analyysi kirjataan 
tyypillisesti Excel-taulukkoon, jonka formaatti on melko homogeeninen osteologista riippumatta. 
Tietokantoja ei yleensä käytetä, mutta ominaisuus olisi kätevä. Samaa kohdetta
saatetaan kaivaa esim. 8 vuotta, ja kohteen mukaan luodusta tietokannasta olisi nykyistä 
näppärämpi tarkistaa esim. montako ketun sormiluuta on kohteesta Saarenoja2 vuosilta
1999-2006. Jos tietokanta annettaisiin esim. kaivauksenjohtajan käyttöön, olisi tarpeen
luoda käyttäjähierarkia. Erityinen metodinen ongelma on määrien laskeminen. Esim. 
pohditaan, oliko kala vai lehmä tärkeämpi ruuan lähde, kun on 1000 fragmenttia = 30 grammaa 
kalanluita eri yksilöistä, elopaino 200kg, 1000 fragmenttia = 300 grammaa lehmänluita,
jotka voivat olla yhdestä tai kymmenestä yksilöstä, elopaino 500-5000kg.

## Käyttäjät

Sovelluksen käyttäjät ovat osteoarkeologeja. Ainakaan alkuvaiheessa ei ole tarpeen luoda
käyttäjähierarkiaa.

## Suunnittellut toiminnallisuudet

- yksinkertainen graafinen käyttöliittymä
- sovellukselle annetaan syötteeksi csv-tiedosto, jonka sovellus lukee tiedostoon ja 
tuottaa pyydettyjä tilastoja ja kuvaajia

## Jatkokehitysideoita

Käytettävissä olevan ajan puitteissa perusversioon voidaan lisätä toiminnallisuuksia:

- voidaan laajentaa tuotettavien kuvaajien ja tilastojen tarjontaa monipuolisemmaksi,
 ja erityisesti kehittää määrien laskemisen metodeja
- voidaan lisätä tietokantaominaisuus
- voidaan lisätä käyttäjähierarkia (tätä ei ole tarkoitus toteuttaa vielä)	 
