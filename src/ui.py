import sys
import pygame


class Ui:

    def __init__(self, display, level, gameloop, connection):

        self._display = display
        self._level = level
        self._gameloop = gameloop
        self._connection = connection

    
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
        button_text = font2.render("Start Game", True, (255, 255, 255))
        self._display.fill((0, 0, 0))

        while True:

            cursor = self._connection.cursor()
            cursor.execute("INSERT INTO highscores (score) VALUES (?)", (self._level.score,))
            self._connection.commit()
            score = self.get_highscore()
            highscore = font2.render(f"Your Highscore: {score}", True, (255, 255, 255))
            self._display.blit(start_text, [110, 300])
            x, y = pygame.mouse.get_pos()

            button_1 = pygame.draw.rect(
                self._display, (220, 20, 60), [400, 420, 200, 50])
            self._display.blit(button_text, button_1)
            self._display.blit(highscore, [0, 0])

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

                        return self._gameloop.start()

            

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
        button_text = font2.render("Restart", True, (255, 255, 255))
        button2_text = font2.render("Quit Game", True, (255, 255, 255))
        self._display.fill((0, 0, 0))

        while True:

            cursor = self._connection.cursor()
            cursor.execute("INSERT INTO highscores (score) VALUES (?)", (self._level.score,))
            self._connection.commit()
            score = self.get_highscore()
            highscore = font2.render(f"Your Highscore: {score}", True, (255, 255, 255))
            self._display.blit(game_over, [310, 300])
            x, y = pygame.mouse.get_pos()

            button_1 = pygame.draw.rect(self._display, (128, 138, 135), [340, 420, 120, 50])
            button_2 = pygame.draw.rect(self._display, (128, 138, 135), [490, 420, 180, 50])
            self._display.blit(button_text, button_1)
            self._display.blit(button2_text, button_2)
            self._display.blit(highscore, [0, 0])
            

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
                        self._level.fps = 16
                        self._level.score = 0
                        click = False

                        self._gameloop.start()

                if button_2.collidepoint((x, y)):

                    if click:

                        pygame.quit()
                        sys.exit()


    def get_highscore(self):

        cursor = self._connection.cursor()
        cursor.execute("SELECT MAX(score) FROM highscores")
        highscore = cursor.fetchone()[0]
        return highscore