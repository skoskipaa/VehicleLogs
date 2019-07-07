# VehicleLogs (Python & Flask)

Pieni ajopäiväkirjasovellus ([ot-harjoitustyö](https://github.com/skoskipaa/ot-harjoitustyo) Javalla) toteutettuna harjoituksen vuoksi ja omaksi iloksi myös Pythonilla ja Flaskilla.

## Tämänhetkiset toiminnallisuudet

* Käyttäjätilin luominen
* Kirjautuminen
* Ajoneuvon lisäys
* Ajoneuvojen listaus
* Tapahtuman lisäys ajoneuvolle
* Ajoneuvon tapahtumien listaus
* Kaikkien tapahtumien listaus
* Käyttäjien listaus

## Suunnitellut toiminnallisuudet

### Kirjautunut käyttäjä (USER) voi 
    * Muuttaa salasanansa
    * Lisätä ajoneuvolle tapahtuman
    * Listata omat kirjauksensa
    * Kirjautua ulos
    
### Kirjautunut ylläpitäjä (ADMIN) voi
    * Lisätä, poistaa ja muokata käyttäjiä
    * Lisätä, poistaa ja muokata ajoneuvoja
    * Lisätä, poistaa ja muokata tapahtumia
    * Listata kaikki tapahtumat
    * Listata tietyn ajoneuvon tapahtumat
    * Tulostaa tilastotietoja
    * Kirjautua ulos
    
## Bugit

Lomakkeiden syötteet on validoitu, mutta kilometrisyöttöön on vielä mahdollista syöttää edellistä lukemaa pienempi luku.
