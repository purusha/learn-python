from cell import Cell
from game import Game

class Board:
    def __init__(self, width, height, *cells):
        self._board = [[Cell(False) for y in range (0, height)] for x in range(0, width) ]

        for cell in cells:
            self._board[cell[0]][cell[1]].live()

        for x in range(0, len(self._board)):
            for y in range(0, len(self._board[x])):
                self._board[x][y].addNeighbours(self._getNeighboursOf(x, y))

    def tick(self):
        for x in range(0, len(self._board)):
            for y in range(0, len(self._board[x])):
                Game.tick(self.cell(x, y))

    def cell(self, x, y):
        return self._board[x][y]

    def _getNeighboursOf(self, x, y):
        result = []
        xy_max = len(self._board) - 1

        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if ((i == x and j == y) or (i < 0 or i > xy_max or j < 0 or j > xy_max)):
                    pass
                else:
                    result.append(self.cell(i, j))

        return result
