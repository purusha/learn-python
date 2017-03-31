class Game:

    @staticmethod
    def tick(cell):
        if cell.isAlive():
            if len(cell.getNeighbours()) < 2:
                cell.die()

            if len(cell.getNeighbours()) > 3:
                cell.die()
        else:
            if len(cell.getNeighbours()) == 3:
                cell.live()
