## Matopeli

Sovellus on perinteinen matopeli, jossa mato kerää ruokaa kentältä ja kasvaa aina syödessään. Peli loppuu jos pelaaja osuu kentän reunaan tai itseensä.

### Dokumentaatio

###### [Vaatimusmäärittely](https://github.com/AapoTuulentie/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
###### [Tuntikirjanpito](https://github.com/AapoTuulentie/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
###### [Changelog](https://github.com/AapoTuulentie/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
###### [Arkkitehtuuri](https://github.com/AapoTuulentie/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
###### [Käyttöohje](https://github.com/AapoTuulentie/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
###### [Viikko 5 release](https://github.com/AapoTuulentie/ot-harjoitustyo/releases/tag/viikko5)
###### [Viikko 6 release](https://github.com/AapoTuulentie/ot-harjoitustyo/releases/tag/viikko6)
###### [Final release](

### Asennus
1. Asenna riippuvuudet komennolla <b>poetry install</b>
2. Alusta tietokannat komennolla <b>poetry run invoke build</b>
3. Käynnistä peli komennolla <b>poetry run invoke start</b>

### Komentorivi
- Testit voidaan suorittaa komennolla <b>poetry run invoke test</b>
- Testikattavuuden saa komennolla <b>poetry run invoke coverage-report</b>
- Koodin laadun tarkistus suoritetaan komennolla <b>poetry run invoke lint</b>
