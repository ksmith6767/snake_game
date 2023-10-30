import pygame

from resources.snake_constants import SnakeConstants


class RenderUtil:

    @staticmethod
    def render_snake(screen, snake):

        # Iterate over the segments and render, darken shade progressively from head to tail
        segment_counter: int = 0
        for segment in snake.body:
            pygame.draw.rect(screen,
                             (255 - (segment_counter * 10),
                              255 - (segment_counter * 10),
                              255 - (segment_counter * 10)),
                             pygame.Rect(segment[0] * 100, segment[1] * 100,
                                         SnakeConstants.SCREEN_WIDTH / SnakeConstants.BOARD_WIDTH,
                                         SnakeConstants.SCREEN_HEIGHT / SnakeConstants.BOARD_HEIGHT))
            if segment_counter * 10 < 175:
                segment_counter += 1

    @staticmethod
    def render_pellet(screen, pellet):

        # Draw red pellet
        pygame.draw.rect(screen,
                         (255, 0, 0),
                         pygame.Rect(pellet.coordinate[0] * 100, pellet.coordinate[1] * 100,
                                     SnakeConstants.SCREEN_WIDTH / SnakeConstants.BOARD_WIDTH,
                                     SnakeConstants.SCREEN_HEIGHT / SnakeConstants.BOARD_HEIGHT))
