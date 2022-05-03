import unittest
import pygame
from level import Level
from gameloop import GameLoop


class TestGameLoop(unittest.TestCase):

    def setUp(self):

        self.level = Level(pygame.display.set_mode((1000, 800)))
        self.gameloop = GameLoop(pygame.display.set_mode((1000, 800)), self.level)

