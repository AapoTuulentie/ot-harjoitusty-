import sys
import pygame


class GameLoop:
    
    """Luokka määrittelee pelin valikot sekä pelin kulun ja käärmeen ohjaamisen.
    
    Atribuutit:
        display: peli-ikkunan koko
        clock: kello
        level: toinen luokka level
    """

    def __init__(self, display, level):

        self._display = display
        self._clock = pygame.time.Clock()
        self._level = level

    def start(self):

        """Aloittaa peliloopin"""

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

        """Määrittelee pelin tapahtumat sekä näppäimet käärmeen ohjaamiseen
            Perii funktiot move_snake ja check_food Level-luokasta.
            """

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

        """Päävalikko, jossa on nappi pelin aloittamiselle

            Args:
                font: suurempi fontti
                font2: pienempi fontti
                start_text: otsikko
                button_text: napissa oleva teksti
            """

        font = pygame.font.SysFont('arial', 70)
        font2 = pygame.font.SysFont('arial', 35)
        start_text = font.render("Welcome to Snake Game!", True, (0, 201, 87))
        button_text = font2.render("Start Game", True, (0, 0, 0))

        while True:

            self._display.fill((0, 0, 0))
            self._display.blit(start_text, [110, 300])
            x, y = pygame.mouse.get_pos()

            button_1 = pygame.draw.rect(
                self._display, (0, 201, 87), [400, 420, 200, 50])
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

        """Loppunäyttö, josta voi yrittää peliä uudelleen

            Args:
                font: suurempi fontti
                font2: pienempi fontti
                game_over: otsikko
                button_text: napissa oleva teksti
        """

        font = pygame.font.SysFont('arial', 70)
        font2 = pygame.font.SysFont('arial', 35)
        game_over = font.render("Game Over!", True, (255, 48, 48))
        button_text = font2.render("Restart", True, (0, 0, 0))

        while True:

            self._display.fill((0, 0, 0))
            self._display.blit(game_over, [300, 300])
            x, y = pygame.mouse.get_pos()

            button_1 = pygame.draw.rect(
                self._display, (0, 201, 87), [440, 420, 120, 50])
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
                        self._level.snake_body = [self._level.snake_head,
                                                [self._level.snake_head[0] -
                                                self._level.block, self._level.snake_head[1]],
                                                [self._level.snake_head[0] - 2*self._level.block,
                                                self._level.snake_head[1]]]
                        self._level.direction = "RIGHT"

                        self.start()
