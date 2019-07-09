# VehicleLogs (Python & Flask)

Pieni ajopäiväkirjasovellus (kuten [ot-harjoitustyö](https://github.com/skoskipaa/ot-harjoitustyo) Javalla) toteutettuna harjoituksen vuoksi ja omaksi iloksi myös Pythonilla ja Flaskilla. Sovellukseen voi syöttää ajoneuvoja ja lisätä niille tapahtumia.

## Tämänhetkiset toiminnallisuudet

### Käyttäjä (USER) voi

      * Kirjautua sisään
      * Hakea ajoneuvojen listauksen
      * Luoda uuden tapahtuman ajoneuvolle
      * Kirjautua ulos
      
### Ylläpitäjä (ADMIN) voi näiden toiminnallisuuksien lisäksi

      * Luoda uuden käyttäjän
      * Luoda uuden ajoneuvon
      * Listata kaikki käyttäjät
      * Listata kaikki tapahtumat
      
## Suunnitellut toiminnallisuudet

### Kirjautunut käyttäjä (USER) voi 

    * Muuttaa salasanansa
    * Listata omat kirjauksensa
    
### Kirjautunut ylläpitäjä (ADMIN) voi

    * Poistaa ja muokata käyttäjiä
    * Poistaa ja muokata ajoneuvoja
    * Poistaa ja muokata tapahtumia
    * Listata tietyn ajoneuvon tapahtumat
    * Tulostaa tilastotietoja ja raportteja
    
## Bugit ja heikkoudet/kehitysideat

* Lomakkeiden syötteet on validoitu, mutta kilometrisyöttöön on vielä mahdollista syöttää edellistä lukemaa pienempi luku. 
* Flask-Loginin käyttö lienee turhaa kirjautumisten hallinnassa, koska samat toiminnallisuudet olisi voitu toteuttaa myös pelkällä Flask-Userilla, jonka myös otin käyttöön käyttäjäroolien hallintaa varten.

