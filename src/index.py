import pygame
from level import Level
from gameloop import GameLoop


def main():

    display_size_x = 1000
    display_size_y = 800
    display = pygame.display.set_mode((display_size_x, display_size_y))
    pygame.display.set_caption("Snake Game")

    level = Level(display)
    gameloop = GameLoop(display, level)

    pygame.init()
    gameloop.main_menu()


if __name__ == "__main__":
    main()
