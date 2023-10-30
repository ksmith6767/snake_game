from typing import Final, Dict
import pygame


class SnakeConstants:

    # Define movement direction constants
    NORTH: Final[int] = 1
    EAST: Final[int] = 2
    SOUTH: Final[int] = 3
    WEST: Final[int] = 4

    # Define the dimensions of the board
    BOARD_WIDTH: Final[int] = 10
    BOARD_HEIGHT: Final[int] = 10

    # Define the dimensions of the screen in pixels
    SCREEN_WIDTH: Final[int] = 1000
    SCREEN_HEIGHT: Final[int] = 1000

    # Map input keys to their directions
    KEY_TO_DIRECTION = {
        pygame.K_UP: NORTH,
        pygame.K_RIGHT: EAST,
        pygame.K_DOWN: SOUTH,
        pygame.K_LEFT: WEST,
    }
