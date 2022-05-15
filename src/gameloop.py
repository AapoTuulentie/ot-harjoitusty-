import sys
import pygame


class GameLoop:

    """Luokka määrittelee pelin valikot sekä pelin kulun ja käärmeen ohjaamisen.

    Attributes:
        display: peli-ikkunan koko
        clock: kello
        level: toinen luokka level
    """

    def __init__(self, display, level, event_queue):

        self._display = display
        self._clock = pygame.time.Clock()
        self._level = level
        self._event_queue = event_queue

    def start(self):

        """Aloittaa peliloopin"""

        while True:

            self._display.fill((0, 0, 0))

            if self.events() is False:
                break

            if self._level.check_collisions() is True:
                break

            self._clock.tick(self._level.fps)
            self._level.render()
            pygame.display.update()

    def events(self):

        """Määrittelee pelin tapahtumat sekä näppäimet käärmeen ohjaamiseen
            Perii funktiot move_snake ja check_food Level-luokasta.
            """

        previous_direction = self._level.direction

        for event in self._event_queue.get():

            if event.type == pygame.QUIT:

                return False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:

                    self.pause()

                elif event.key == pygame.K_UP and previous_direction != "DOWN":

                    self._level.direction = "UP"

                elif event.key == pygame.K_DOWN and previous_direction != "UP":

                    self._level.direction = "DOWN"

                elif event.key == pygame.K_RIGHT and previous_direction != "LEFT":

                    self._level.direction = "RIGHT"

                elif event.key == pygame.K_LEFT and previous_direction != "RIGHT":

                    self._level.direction = "LEFT"

        self._level.move_snake()
        self._level.check_food()

    def pause(self):

        font = pygame.font.SysFont('arial', 40)
        text = font.render("Game paused - press 'ESC' to continue", True, (255, 255, 255))
        self._display.fill((0, 0, 0))
        self._display.blit(text, [150, 350])
        pygame.display.update()

        while True:

            for event in self._event_queue.get():

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        return

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()