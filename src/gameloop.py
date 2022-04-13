import pygame

class GameLoop:

    def __init__(self, display, level):
        
        self._display = display
        self._clock = pygame.time.Clock()
        self._level = level
        self.direction = "right"


    def start(self):

        while True:

            if self._events == False:
                break

            self._clock.tick(20)

            
    
    def _events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                return False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP or event.key == ord("w"):

                    self.direction = "UP"

                elif event.key == pygame.K_DOWN or event.key == ord("s"):

                    self.direction = "DOWN"

                elif event.key == pygame.K_RIGHT or event.key == ord("d"):

                    self.direction = "RIGHT"

                elif event.key == pygame.K_LEFT or event.key == ord("a"):

                    self.direction = "LEFT"

        self.move_snake(self.direction)
        self._level.snake_body.insert(0, self._level.snake_head)


    def move_snake(self):

        x = self._level.snake_head[0]
        y = self._level.snake_head[1]

        if self.direction == "UP":

            y -= self._level.block

        elif self.direction == "DOWN":

            y += self._level.block

        elif self.direction == "RIGHT":

            x += self._level.block

        elif self.direction == "LEFT":

            x += self._level.block

        self._level.snake_head = [x, y]
