import random
from typing import Tuple, List

from board import Board
from snake import Snake


class Pellet:

    def __init__(self, snake: Snake, board: Board):
        # Get a list of all open positions on the board
        all_available_positions: List[Tuple[int, int]] = []
        for row in board.table:
            for position in row:
                if position not in snake.body:
                    all_available_positions.append(position)

        # Set the coordinate for the pellet to a random unoccupied position
        self.coordinate: Tuple[int, int] =\
            all_available_positions[random.randint(0, len(all_available_positions) - 1)]