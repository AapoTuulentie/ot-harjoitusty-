from platform import java_ver
import pygame 
from level import Level
from gameloop import GameLoop


def main():

    pygame.init()

    display_size_x = 720
    display_size_y = 480
    snake_speed = 10
    display = pygame.display.set_mode((display_size_x, display_size_y))
    pygame.display.set_caption("Snake game")

    level = Level()
    

