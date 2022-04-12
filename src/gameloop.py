import pygame

class GameLoop:

    def __init__(self, display, level):
        
        self._display = display
        self._clock = pygame.time.Clock()
        self._level = level


    def start(self):

        while True:

