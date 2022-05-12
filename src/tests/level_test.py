import unittest
import pygame
from level import Level



class TestLevel(unittest.TestCase):

    def setUp(self):

        self.level = Level(pygame.display.set_mode((1000, 800)))


    def test_wall_collisions(self):

        self.level.snake_head = [2000, 500]
        self.assertEqual(self.level.check_collisions(), True)


    def test_snake_eat(self):

        self.level.snake_body = [[500, 400], [480, 400], [460, 400]]
        self.level.food = [500, 400]
        self.level.check_food()

        self.assertEqual(len(self.level.snake_body), 4)


    def test_body_collisions(self):

        self.level.snake_head = [500, 400]
        self.level.snake_body = [[500, 400], [480, 400], [500, 400]]

        self.assertEqual(self.level.check_collisions(), True)

    
    def test_snake_move_up(self):

        self.level.snake_head = [500, 400]
        self.level.direction =  "UP"
        self.level.move_snake()

        self.assertEqual(self.level.snake_head, [500, 380])


    def test_snake_move_down(self):

        self.level.snake_head = [500, 400]
        self.level.direction =  "DOWN"
        self.level.move_snake()

        self.assertEqual(self.level.snake_head, [500, 420])


    def test_snake_move_right(self):

        self.level.snake_head = [500, 400]
        self.level.direction =  "RIGHT"
        self.level.move_snake()

        self.assertEqual(self.level.snake_head, [520, 400])


    def test_snake_move_left(self):

        self.level.snake_head = [500, 400]
        self.level.direction = "LEFT"
        self.level.move_snake()

        self.assertEqual(self.level.snake_head, [480, 400])


    def test_snake_body_pop(self):

        self.level.snake_body = [[500, 400], [520, 400], [540, 400]]
        self.level.food = [500, 300]
        self.level.check_food()

        self.assertEqual(self.level.snake_body[-1], [520, 400])

    
    def test_check_collision_return_false(self):

        self.level.snake_head = [500, 400]
        self.level.snake_body = [[500, 400], [520, 400], [540, 400]]

        self.assertEqual(self.level.check_collisions(), False)