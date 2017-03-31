from cell import Cell
from game import Game

class Board:
    def __init__(self, width, height, *cells):
        # Todo
        # if width != height throw exception
        # if cell is over this board throw exception

        self._board = [[Cell(False) for y in range (0, height)] for x in range(0, width)]

        for cell in cells:
            self._board[cell[0]][cell[1]].live()

        for x in range(0, self._len()):
            for y in range(0, self._len()):
                self._board[x][y].addNeighbours(self._getNeighboursOf(x, y))

    def tick(self):
        for x in range(0, self._len()):
            for y in range(0, self._len()):
                Game.tick(self.cell(x, y))

    def cell(self, x, y):
        return self._board[x][y]

    def _len(self):
        return len(self._board)

    def _getNeighboursOf(self, x, y):
        result = []
        xy_max = self._len() - 1

        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if ((i == x and j == y) or (i < 0 or i > xy_max or j < 0 or j > xy_max)):
                    pass
                else:
                    result.append(self.cell(i, j))

        return result

    def printOut(self):
        print("board is {0}".format(id(self)))

        s = [[str(e) for e in row] for row in self._board]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print '\n'.join(table)

        print("#" * 25)
