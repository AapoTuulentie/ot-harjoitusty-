import pygame

class GameLoop:

    def __init__(self, display, level):
        
        self._display = display
        self._clock = pygame.time.Clock()
        self._level = level
        self.direction = "RIGHT"


    def start(self):

        while True:

            if self._events == False:
                break
            
            if self._player_inputs() is False:
                break

            if self.check_collisions is True:
                break
            
            pygame.display.update()
            self._display.fill((0, 0, 0))

            self._clock.tick(20)
            self._level.render()
            self._events()

            
    
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

        self.move_snake()
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


    def check_collisions(self):

        if self._level.snake_head[0] > 720 - self._level.block or self._level.snake_head[1] > 480 - self._level.block or self._level.snake_head[0] < 0 or self._level.snake_head[1] < 0:
            return True
        
        if self._level.snake_head in self._level.snake_body[1:]:
            return True

        return False


    def _player_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

