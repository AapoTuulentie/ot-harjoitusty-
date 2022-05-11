import pygame
from level import Level
from gameloop import GameLoop
from ui import Ui
from database_connection import get_database_connection


def main():

    display_size_x = 1000
    display_size_y = 800
    display = pygame.display.set_mode((display_size_x, display_size_y))
    pygame.display.set_caption("Snake Game")
    connection = get_database_connection()

    level = Level(display)
    gameloop = GameLoop(display, level)
    ui = Ui(display, level, gameloop, connection)

    pygame.init()
    ui.main_menu()

    while True:

        ui.end_screen()

if __name__ == "__main__":
    main()
