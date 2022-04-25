import unittest
import pygame
from level import Level
from gameloop import GameLoop


class TestSnake:

    def setUp(self):

        self.level = Level()
        self.gameloop = GameLoop()


    def test_collisions(self):

        self.level.snake_head = [1001, 801]
        self.assertEqual(self.level.check_collisions(), True)