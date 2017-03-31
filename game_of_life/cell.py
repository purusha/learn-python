class Cell:
    def __init__(self, status):
        self._status = status
        self._neighbours = list()

    def addNeighbours(self, *cell):
        self._neighbours.extend(list(cell))

    def isAlive(self):
        return self._status

    def getNeighbours(self):
        return [x for x in self._neighbours if x.isAlive()]

    def die(self):
        self._status = False

    def live(self):
        self._status = True
