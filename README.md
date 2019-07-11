# VehicleLogs (Python & Flask)

Pieni ajopäiväkirjasovellus (kuten [ot-harjoitustyö](https://github.com/skoskipaa/ot-harjoitustyo) Javalla) toteutettuna harjoituksen vuoksi ja omaksi iloksi myös Pythonilla ja Flaskilla. Sovellukseen voi syöttää ajoneuvoja ja lisätä niille tapahtumia (ajo, huolto, tankkaus).

## Tämänhetkiset toiminnallisuudet

### Käyttäjä (USER) voi

      * Kirjautua sisään
      * Hakea ajoneuvojen listauksen
      * Luoda uuden tapahtuman ajoneuvolle
      * Listata omat merkintänsä
      * Kirjautua ulos
      
### Ylläpitäjä (ADMIN) voi näiden toiminnallisuuksien lisäksi

      * Luoda uuden käyttäjän
      * Luoda uuden ajoneuvon
      * Listata kaikki käyttäjät
      * Listata kaikki tapahtumat
      * Listata tietyn ajoneuvon tapahtumat
      
## Suunnitellut toiminnallisuudet

### Kirjautunut käyttäjä (USER) voi 

    * Muuttaa salasanansa
    
### Kirjautunut ylläpitäjä (ADMIN) voi

    * Poistaa ja muokata käyttäjiä
    * Poistaa ja muokata ajoneuvoja
    * Poistaa ja muokata tapahtumia
    * Tulostaa tilastotietoja ja raportteja
    
## Bugit ja heikkoudet/kehitysideat

* Flask-Loginin käyttö lienee turhaa kirjautumisten hallinnassa, koska samat toiminnallisuudet olisi voitu toteuttaa myös pelkällä Flask-Userilla, jonka myös otin käyttöön käyttäjäroolien hallintaa varten.
* Tapahtumalistauksessa näkyvät nyt kuljettajan id ja ajoneuvon id. Ne voisivat näkyä listauksessa oikeina niminä. Tietokantaa voisi denormalisoida ja lisätä tiedot logikirjaukseen, jotta niiden haku onnistuisi yhdestä taulusta.


