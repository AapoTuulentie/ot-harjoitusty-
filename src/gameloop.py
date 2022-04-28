import pygame
import sys


class GameLoop:

    def __init__(self, display, level):

        self._display = display
        self._clock = pygame.time.Clock()
        self._level = level


    def start(self):

        while True:
         
            self._display.fill((0, 0, 0))

            if self.events() is False:
                break

            if self._level.check_collisions() is True:
                self.end_screen()

            self._clock.tick(self._level.fps)
            self._level.render()
            pygame.display.update()


    def events(self):

        previous_direction = self._level.direction

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                return False

            if event.type == pygame.KEYDOWN:

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


    def main_menu(self): 

        font = pygame.font.SysFont('arial', 70)
        font2 = pygame.font.SysFont('arial', 35)
        start_text = font.render("Welcome to Snake Game!", True, (0, 201, 87))
        button_text = font2.render("Start Game", True, (0, 0, 0))

        while True:

            self._display.fill((0, 0, 0))
            self._display.blit(start_text, [110, 300])
            x, y = pygame.mouse.get_pos()

            button_1 = pygame.draw.rect(self._display, (0, 201, 87), [400, 420, 200, 50])
            self._display.blit(button_text, button_1)

            pygame.display.update()
    
            click = False

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if event.button == 1:

                        click = True

                if button_1.collidepoint((x, y)):
                
                    if click:
                
                        self.start()


    def end_screen(self):  

        font = pygame.font.SysFont('arial', 70)
        font2 = pygame.font.SysFont('arial', 35)
        game_over = font.render("Game Over!", True, (255, 48, 48))
        button_text = font2.render("Restart", True, (0, 0, 0))

        while True:

            self._display.fill((0, 0, 0))
            self._display.blit(game_over, [300, 300])
            x, y = pygame.mouse.get_pos()

            button_1 = pygame.draw.rect(self._display, (0, 201, 87), [440, 420, 120, 50])
            self._display.blit(button_text, button_1)
        

            pygame.display.update()

            click = False

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if event.button == 1:

                        click = True

                if button_1.collidepoint((x, y)):
                
                    if click:
                        
                        self._level.snake_head = [1000/2, 800/2]
                        self._level.snake_body = [self._level.snake_head, [self._level.snake_head[0] - self._level.block,
                                             self._level.snake_head[1]], [self._level.snake_head[0] - 2*self._level.block, self._level.snake_head[1]]]
                        self._level.direction = "RIGHT"

                        self.start()
