import unittest
import Board


class MyTestCase(unittest.TestCase):
    def test1(self):
        t = Board.Tile(color='red', number=7)
        self.assertEqual(str(t), 'red 7')

    def test2(self):
        b = Board.Board(1)



if __name__ == '__main__':
    unittest.main()
