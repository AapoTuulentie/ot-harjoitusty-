import pygame 
from level import Level
from gameloop import GameLoop


def main():

    display_size_x = 1200
    display_size_y = 1000
    display = pygame.display.set_mode((display_size_x, display_size_y))
    pygame.display.set_caption("Matopeli")

    level = Level(display)
    gameloop = GameLoop(display, level)

    pygame.init()
    gameloop.start()
    

if __name__ == "__main__":
    main()