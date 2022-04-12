import pygame
from random import randint
red = (220, 20, 60)

class Food(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.image = pygame.Surface([1, 1])
        self.image.fill(red)
        self.food_pos = [randint(1, 720), randint(1, 480)]
        
