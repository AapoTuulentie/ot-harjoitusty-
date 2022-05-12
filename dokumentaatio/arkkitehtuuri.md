# Arkkitehtuurikuvaus

#### Rakenne

Ohjelma koostuu 



```mermaid
    classDiagram

        Index "1" --> "1" GameLoop
        Index "1" --> "1" Level
        GameLoop "1" --> "1" Level
        Index "1" --> "1" Ui
        Ui "1" --> "1" GameLoop
        Ui "1" --> "1" Level

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
    
```
Sovelluslogikka ja käyttöliittymä on pyritty erottamaan mahdollisimman hyvin. GameLoop tiedosto sisältää itse pelin loopin sekä pelin tapahtumien käsittelyn. <br> Level sisältää sovelluslogiikan ja Ui sisältää käyttöliittymän.
```mermaid
    sequenceDiagram
        
        participant Index
        participant GameLoop
        participant Level
        Index ->> GameLoop: Start
        GameLoop -->> Index: End
        Index ->> Level: Create level
        Level -->> Index: None
        
```
