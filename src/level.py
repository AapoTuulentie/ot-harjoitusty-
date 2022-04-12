import pygame
from sprites.snake import Snake
from sprites.food import Food

class Level:

    def __init__(self):

        self.snake = Snake()
        self.food = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        