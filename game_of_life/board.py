from cell import Cell
from game import Game

class Board:
    def __init__(self, width, height):
        self._board = [[Cell(False) for y in range (0, height)] for x in range(0, width) ]

    def updateAliveCell(self, *cells):
        for cell in cells:
            self._board[cell[0]][cell[1]].live()

        for x in range(0, len(self._board)):
            for y in range(0, len(self._board[x])):
                #do this only one times ... if i call twice updateAliveCell we must have a problems!!
                self._board[x][y].addNeighbours(self._getNeighboursOf(x, y))

    def tick(self):
        for x in range(0, len(self._board)):
            for y in range(0, len(self._board[x])):
                Game.tick(self.cell(x, y))

    def cell(self, x, y):
        return self._board[x][y]

    def _getNeighboursOf(self, x, y):
        print "#" * 42
        print "x {0}, y {1}".format(x, y)

        result = []
        maxWidth = len(self._board) -1
        maxHeight = len(self._board[0]) -1


        for i in range(x-1, x+1):
            for j in range(y-1, y+1):
                if (i < 0 or i > maxWidth or j < 0 or j > maxHeight):
                    print "{0}, {1}, {2}".format(i, j, "NO")
                else:
                    print "{0}, {1}, {2}".format(i, j, "YES")
                    result.append(self.cell(i, j))

        #print "{0}, {1}, {2}".format(x, y, result)
        return tuple(result)
