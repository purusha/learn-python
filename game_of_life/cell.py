import itertools

class Cell:
    def __init__(self, status):
        self._status = status
        self._neighbours = list()

#       list2d = [[1,2,3],[4,5,6], [7], [8,9]]
#       list(itertools.chain(*list2d))
#       [1, 2, 3, 4, 5, 6, 7, 8, 9]
    def addNeighbours(self, *cell):
        self._neighbours.extend(itertools.chain(*cell))

    def isAlive(self):
        return self._status

    def getNeighbours(self):
        return [x for x in self._neighbours if x.isAlive()]

    def die(self):
        self._status = False

    def live(self):
        self._status = True

    def __str__(self):
        return "V" if self.isAlive() else "X"
