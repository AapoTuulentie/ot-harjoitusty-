```mermaid
    classDiagram
        Index "1" --> "1" GameLoop
        Index "1" --> "1" Level
        Level "1" --> "1" GameLoop
        GameLoop "1" --> "1" Level

        class Index{
            Level
            GameLoop

        }

    class Level{


    }

    class GameLoop{

        
    }