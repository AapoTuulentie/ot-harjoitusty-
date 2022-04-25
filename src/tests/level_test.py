import unittest
from level import Level
import pygame


class TestSnake(unittest.TestCase):

    def setUp(self):

        self.level = Level()
        pygame.init()

    def test_collisions(self):

        self.level.snake_head = [1001, 801]
        self.assertEqual(self.level.check_collisions(), True)

        

