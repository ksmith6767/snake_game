from typing import Tuple

import pygame

from board import Board
from pellet import Pellet
from util.render_util import RenderUtil
from resources.snake_constants import SnakeConstants
from snake import Snake

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Define the initial screen and window title
    screen = pygame.display.set_mode((SnakeConstants.SCREEN_WIDTH, SnakeConstants.SCREEN_HEIGHT))
    background_colour = (0, 0, 0)
    pygame.display.set_caption('snake_game')

    # Initialize initial state values
    running = True
    board: Board = Board(SnakeConstants.BOARD_WIDTH, SnakeConstants.BOARD_HEIGHT)
    snake: Snake = Snake()
    pellet: Pellet = Pellet(snake, board)

    # Game Loop
    speed_factor: int = 0
    while running:
        screen.fill(background_colour)
        RenderUtil.render_snake(screen, snake)
        RenderUtil.render_pellet(screen, pellet)
        pygame.display.update()
        pygame.time.wait(500 - speed_factor)

        # for loop through the event queue
        new_direction: int = snake.direction
        for event in pygame.event.get():
            # Check key-presses
            if event.type == pygame.KEYDOWN:
                # Check quit
                if event.key == pygame.K_ESCAPE:
                    running = False
                    break

                # Check restart
                elif event.key == pygame.K_r:
                    snake = Snake()
                    pellet = Pellet(snake, board)

                # Update direction if applicable
                new_direction = SnakeConstants.KEY_TO_DIRECTION.get(event.key)

            # Check for QUIT event
            if event.type == pygame.QUIT:
                running = False

        # Check for pellet eating or death, update the snake
        snake.update_snake(new_direction)
        if snake.body[0] == pellet.coordinate:
            snake.eat_pellet()
            pellet = Pellet(snake, board)
            if speed_factor < 250:
                speed_factor += 25

        # Check for self touch
        if snake.body[0] in snake.body[1: len(snake.body)]:
            print('body')
            running = False

        # Check for wall touch
        head: Tuple[int, int] = snake.body[0]
        for head_position in head:
            if head_position < 0 or head_position > (SnakeConstants.BOARD_WIDTH - 1):
                print('wall')
                running = False
