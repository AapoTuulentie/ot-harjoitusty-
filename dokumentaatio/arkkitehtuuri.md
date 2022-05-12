# Arkkitehtuurikuvaus

#### Rakenne

Ohjelma koostuu pääosin neljästä tiedostosta: App, GameLoop, Ui ja Level.



```mermaid
    classDiagram

        App "1" --> "1" GameLoop
        App "1" --> "1" Level
        GameLoop "1" --> "1" Level
        App "1" --> "1" Ui
        Ui "1" --> "1" GameLoop
        Ui "1" --> "1" Level

        class App{
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
    
```
Sovelluslogikka ja käyttöliittymä on pyritty erottamaan mahdollisimman hyvin. GameLoop tiedosto sisältää itse pelin loopin sekä pelin tapahtumien käsittelyn, kun taas Level sisältää sovelluslogiikan ja Ui käyttöliittymän.

```mermaid
    sequenceDiagram
        
        participant App
        participant GameLoop
        participant Level
        Index ->> GameLoop: Start
        GameLoop -->> App: End
        Index ->> Level: Create level
        Level -->> App: None
        
```
