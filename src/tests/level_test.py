import unittest
from level import Level


class TestSnake(unittest.TestCase):

    def setUp(self):

        self.level = Level()

    def test_collisions(self):

        self.level.snake_head = [1001, 801]
        self.assertEqual(self.level.check_collisions(), True)