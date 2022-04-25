import pygame

class GameLoop:

    def __init__(self, display, level):
        
        self._display = display
        self._clock = pygame.time.Clock()
        self.fps = 18
        self._level = level
        

    def start(self):

        while True:

            self._display.fill((0, 0, 0))

            if self.events() is False:
                break

            if self._level.check_collisions() is True:
                self._level.game_over()

            self._clock.tick(self.fps)
            self._level.render()
            pygame.display.update()
            
    
    def events(self):

        previous_direction = self._level.direction

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                return False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP and previous_direction != "DOWN":

                    self._level.direction = "UP"

                elif event.key == pygame.K_DOWN and previous_direction != "UP":

                    self._level.direction = "DOWN"

                elif event.key == pygame.K_RIGHT and previous_direction != "LEFT":

                    self._level.direction = "RIGHT"

                elif event.key == pygame.K_LEFT and previous_direction != "RIGHT":

                    self._level.direction = "LEFT"


        self._level.move_snake()
        self._level.check_food()







    



