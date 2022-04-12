import pygame
green = (0, 201, 87)

class Snake(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.image = pygame.Surface([1, 1])
        self.image.fill(green)
        self.snake_pos = [100, 50]

        
