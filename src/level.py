import pygame
from collections import namedtuple
from random import randint

class Level:

    def __init__(self, display):

        self.snake_head = [1000/2, 800/2]
        self._display = display
        self.block = 20
        self.snake_body = [self.snake_head, [self.snake_head[0] - self.block, self.snake_head[1]], [self.snake_head[0] - 2*self.block, self.snake_head[1]]]
        self.food = None
        self.spawn_food()

    def spawn_food(self):   
        
        x = randint(0, (1000 - self.block) // self.block) * self.block
        y = randint(0, (800 - self.block) // self.block) * self.block
        self.food = [x, y]
        if self.food in self.snake_body:
            self.spawn_food()


    def render(self):

        for block in self.snake_body:

            pygame.draw.rect(self._display, (0,201,87), pygame.Rect(block[0], block[1], self.block, self.block))

        pygame.draw.rect(self._display, (220,20,60), pygame.Rect(self.food[0], self.food[1], self.block, self.block))

        pygame.display.update()

    def check_food(self):

        if self.snake_head == self.food:
                self.spawn_food()

        else:
            self.snake_body.pop()


    


    

        