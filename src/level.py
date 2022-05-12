from random import randint
import pygame


class Level:

    """Luokka, jossa on kaikki yksityiskohtaisemmat pelin toiminnot
    
        Attributes:
            snake_head: lähtökoordinaatti käärmeen päälle
            snake_body: lähtökoordinaatti käärmeen koko vartalolle
            display: peli-ikkunan koko
            block: yhden käärmeen osan (neliön) koko
            food: ruoan sijainti. Funktio spawn_food antaa sille ensimmäisen arvon
            fps: pelin frames per second alussa
            score: pelaajan pisteet
            direction: käärmeen suunta pelin alussa
        """


    def __init__(self, display):

        self.snake_head = [1000/2, 800/2]
        self._display = display
        self.block = 20
        self.snake_body = [self.snake_head, [self.snake_head[0] - self.block,
                                             self.snake_head[1]], [self.snake_head[0]
                                             - 2*self.block, self.snake_head[1]]]
        self.food = None
        self.fps = 16
        self.score = 0
        self.direction = "RIGHT"
        self.spawn_food()


    def spawn_food(self):

        """Spawnaa uuden ruoan pelikentälle. Jos randomilla otettu koordinaatti sijaitsee käärmeen sisässä,
        funktiota kutsutaan uudelleen.
        
            Args:
                x: ruoan x-koordinaatti
                y: ruoan y-koordinaatti
            """

        x = randint(0, (1000 - self.block) // self.block) * self.block
        y = randint(0, (800 - self.block) // self.block) * self.block
        self.food = [x, y]

        if self.food in self.snake_body:

            self.spawn_food()


    def render(self):

        """Muodostaa käärmeen vartalon ja ruoan pelikentälle. Lisää myös pistelaskurin yläkulmaan.
        
            Args:
                font: fontti pistelaskurille 
                text: teksti pistelaskurille
            """
        pygame.init()
        for block in self.snake_body:

            pygame.draw.rect(self._display, (0, 201, 87), pygame.Rect(
                block[0], block[1], self.block, self.block))

        pygame.draw.rect(self._display, (220, 20, 60), pygame.Rect(
            self.food[0], self.food[1], self.block, self.block))

        font = pygame.font.SysFont('arial', 25)
        text = font.render(f"Score: {self.score}", True, (240, 255, 255))
        self._display.blit(text, [0, 0])

        pygame.display.update()


    def check_food(self):

        """Liikuttaa käärmettä ja lisää pisteitä, jos ruoka on käärmeen sisässä.
        """

        self.snake_body.insert(0, self.snake_head)

        if self.snake_head == self.food:

            self.score += 1
            
            if self.score % 5 == 0:

                self.fps += 1
            
            self.spawn_food()

        else:

            self.snake_body.pop()


    def check_collisions(self):

        """Tarkistaa törmäykset pelikentän reunan ja käärmeen itsensä kanssa.

            Returns:
                Arvo True, jos käärme törmää reunaan tai itseensä. Muuten
        """

        if self.snake_head[0] > 1000 - self.block or self.snake_head[1] > 800 - self.block or self.snake_head[0] < 0 or self.snake_head[1] < 0:
            return True

        if self.snake_head in self.snake_body[1:]:
            return True

        return False


    def move_snake(self):

        """Liikuttaa käärmettä x- ja y-suunnassa 
        """
        
        x = self.snake_head[0]
        y = self.snake_head[1]

        if self.direction == "UP":

            y -= self.block

        elif self.direction == "DOWN":

            y += self.block

        elif self.direction == "RIGHT":

            x += self.block

        elif self.direction == "LEFT":

            x -= self.block

        self.snake_head = [x, y]

    
    