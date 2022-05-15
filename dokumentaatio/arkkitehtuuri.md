# Arkkitehtuurikuvaus

### Rakenne

Ohjelma koostuu pääosin neljästä tiedostosta: Index, GameLoop, Ui ja Level. EventQueue hakee pelitapahtumat.



```mermaid
    classDiagram

        Index "1" --> "1" GameLoop
        Index "1" --> "1" Level
        GameLoop "1" --> "1" Level
        Index "1" --> "1" Ui
        Ui "1" --> "1" GameLoop
        Ui "1" --> "1" Level
        EventQueue "1" --> "1" GameLoop
        Index "1" --> "1" EventQueue
        

        class Index{
            Level
            GameLoop
            Ui

        }

    class Level{


    }

    class GameLoop{
        Level

    }

    class Ui{
        GameLoop
        Level
    }
    
    class EventQueue{
       
    }
    
```
Sovelluslogikka ja käyttöliittymä on pyritty erottamaan mahdollisimman hyvin. GameLoop tiedosto sisältää itse pelin loopin sekä pelin tapahtumien käsittelyn, kun taas Level sisältää sovelluslogiikan ja Ui käyttöliittymän.

```mermaid
    sequenceDiagram
        
        participant Index
        participant Ui
        participant GameLoop
        participant Level
        Index ->> Ui: Create main menu
        Ui ->> GameLoop: Start game
        GameLoop -->> Ui: End screen
        Ui -->> Index: Quit game
        GameLoop ->> Level: Initialize snake, food and score
        Level -->> GameLoop: None
        
```
### Tietojen tallennus
Pelaajan tulokset tallentuvat SQLite-tietokantaan. Huipputulos ilmoitetaan pelaajalle pelin alku- ja loppunäytöissä.
