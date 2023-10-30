from typing import Tuple, List

from resources.snake_constants import SnakeConstants


class Snake:
    def __init__(self):
        self.body: List[Tuple[int, int]] = [(4, 4), (4, 5), (4, 6)]
        self.direction: int = SnakeConstants.NORTH
        self.last_tail: Tuple[int, int] = (4, 7)

    def update_snake(self, direction: int):
        # Get the old head and update the last tail and direction
        old_head: Tuple[int, int] = self.body[0]
        self.last_tail = self.body[len(self.body) - 1]
        if direction:
            self.direction = direction

        # Update the head based on direction
        if self.direction == SnakeConstants.NORTH:
            old_x: int = old_head[0]
            old_y: int = old_head[1]
            new_head: Tuple[int, int] = (old_x, old_y - 1)
        elif self.direction == SnakeConstants.EAST:
            old_x: int = old_head[0]
            old_y: int = old_head[1]
            new_head: Tuple[int, int] = (old_x + 1, old_y)
        elif self.direction == SnakeConstants.SOUTH:
            old_x: int = old_head[0]
            old_y: int = old_head[1]
            new_head: Tuple[int, int] = (old_x, old_y + 1)
        elif self.direction == SnakeConstants.WEST:
            old_x: int = old_head[0]
            old_y: int = old_head[1]
            new_head: Tuple[int, int] = (old_x - 1, old_y)

        # Update the rest of the body
        new_body: List[Tuple[int, int]] = [new_head]
        for index in range(len(self.body) - 1):
            new_body.append(self.body[index])
        self.body = new_body

    def eat_pellet(self):
        self.body.append(self.last_tail)
