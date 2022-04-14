import pygame

class GameLoop:

    def __init__(self, display, level):
        
        self._display = display
        self._clock = pygame.time.Clock()
        self.fps = 18
        self._level = level
        self.direction = "RIGHT"

    def start(self):

        while True:

            self._display.fill((0, 0, 0))

            if self.events() is False:
                break

            if self._level.check_collisions() is True:
                break

            self._clock.tick(self.fps)
            self._level.render()
            pygame.display.update()
            
    
    def events(self):

        previous_direction = self.direction

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                return False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP or event.key == ord("w") and previous_direction != "DOWN":

                    self.direction = "UP"

                elif event.key == pygame.K_DOWN or event.key == ord("s") and previous_direction != "UP":

                    self.direction = "DOWN"

                elif event.key == pygame.K_RIGHT or event.key == ord("d") and previous_direction != "LEFT":

                    self.direction = "RIGHT"

                elif event.key == pygame.K_LEFT or event.key == ord("a") and previous_direction != "RIGHT":

                    self.direction = "LEFT"


        self.move_snake()
        self._level.check_food()


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

            x -= self._level.block
        
        self._level.snake_head = [x, y]




    



