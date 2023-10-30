from typing import List, Tuple


class Board:
    def __init__(self, width, height):
        self.table: List[List[Tuple[int, int]]] = []
        for i in range(width):
            row: List[Tuple[int, int]] = []
            for j in range(height):
                row.append((i, j))
            self.table.append(row)
