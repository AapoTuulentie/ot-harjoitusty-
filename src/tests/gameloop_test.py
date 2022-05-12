import unittest
import pygame

from level import Level
from gameloop import GameLoop


class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key


class StubEventQueue:
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events



class TestGameLoop(unittest.TestCase):

    def setUp(self):

        self.level = Level(pygame.display.set_mode((1000, 800)))

    def test_can_move(self):

        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_UP),
        ]

        gameloop = GameLoop(pygame.display.set_mode((1000, 800)), self.level, StubEventQueue(events))

        gameloop.start()

        self.assertEqual(self.level.direction, "UP")


    