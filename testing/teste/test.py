#pylint
#pyflakes

# pep 8 

import unittest

import script 


class TestMain(unittest.TestCase):
    def testDoStuff(self):
        testParam = 10 
        result = script.doStuff(testParam)
        self.assertEqual(result, 15)

    def testDoStuff2(self):
        testParam = 'dfsdfs' 
        result = script.doStuff(testParam)
        self.assertIsInstance(result, ValueError)

    def testDoStuff3(self):
        testParam = None 
        result = script.doStuff(testParam)
        self.assertEqual(result, 'please enter number')
    
    def testDoStuff4(self):
        testParam = '' 
        result = script.doStuff(testParam)
        self.assertEqual(result, 'please enter number')


if __name__ == '__main__':
    unittest.main()