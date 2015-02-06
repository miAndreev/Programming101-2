from solution import groupby
import unittest

class MyTests(unittest.TestCase):
    def test_one(self):
        self.assertEquals(groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7]), {0: [0, 2, 4, 6], 1: [1, 3, 5, 7]})

    def test_two(self):
        self.assertEquals(groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]), {'even': [2, 8, 10, 12], 'odd': [1, 3, 5, 9]})

    def test_three(self):
        self.assertEquals(groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]), {0: [0, 3, 6], 1: [1, 4, 7], 2: [2, 5]})


if __name__ == '__main__':
    unittest.main()