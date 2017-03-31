import unittest
from cell import Cell
from game import Game

class TestGame(unittest.TestCase):

    def test_whenCellHaveLessOf2NeighboursThenItDie(self):
        cell = Cell(status = True)
        Game.tick(cell)
        self.assertFalse(cell.isAlive())

        cell = Cell(status = True)
        cell.addNeighbours(Cell(status = True))
        Game.tick(cell)
        self.assertFalse(cell.isAlive())

    def test_whenCellHaveMoreThen3NeighboursThenItDie(self):
        cell = Cell(status = True)
        cell.addNeighbours(Cell(status = True), Cell(status = True), Cell(status = True), Cell(status = True))
        Game.tick(cell)
        self.assertFalse(cell.isAlive())

    def test_whenCellHave3NeighboursThenItResurrects(self):
        cell = Cell(status = False)
        cell.addNeighbours(Cell(status = True), Cell(status = True), Cell(status = True))
        Game.tick(cell)
        self.assertTrue(cell.isAlive())

        cell = Cell(status = False)
        cell.addNeighbours(Cell(status = True), Cell(status = True), Cell(status = False))
        Game.tick(cell)
        self.assertFalse(cell.isAlive())

if __name__ == '__main__':
    unittest.main()
