import unittest
import randomgame


class TestGame(unittest.TestCase):
    def testInput(self):

        result = randomgame.runGuess(5,5)
        self.assertTrue(result)

    def testInputWrongGuess(self):
        result = randomgame.runGuess(5,0)
        self.assertFalse(result)

    def testInputWrongNumber(self):
        result = randomgame.runGuess(5,11)
        self.assertFalse(result)

    def testInputWrongType(self):
        result = randomgame.runGuess(5,'11')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()