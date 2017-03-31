import unittest
from board import Board

class TestGame(unittest.TestCase):

    def test_firstTick(self):
        board = Board(3, 3, (0, 0), (1, 1), (2, 2))
        board.tick()

        for x in range(0, 3):
            for y in range(0, 3):
                self.assertFalse(board.cell(x, y).isAlive(), "fail on ({0}, {1})".format(x, y))

        board.printOut()

    def test_whenDiedCellHave3NeighboursThenItResurrects(self):
        board = Board(3, 3, (0, 1), (1,0), (1,1))
        board.tick()

        self.assertTrue(board.cell(0, 0).isAlive())

        board.printOut()

if __name__ == '__main__':
    unittest.main()
