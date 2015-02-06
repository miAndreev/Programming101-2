from solution import nth_fib_lists
import unittest

class MyTests(unittest.TestCase):
    def test_one(self):
        self.assertEquals(nth_fib_lists([1], [2], 1), [1])
    
    def test_two(self):
        self.assertEquals(nth_fib_lists([1], [2], 2), [2])
    
    def test_three(self):
        self.assertEquals(nth_fib_lists([1, 2], [1, 3], 3), [1, 2, 1, 3])
    
    def test_foure(self):
        self.assertEquals( nth_fib_lists([], [1, 2, 3], 4), [1, 2, 3, 1, 2, 3])
    
    def test_five(self):
        self.assertEquals(nth_fib_lists([], [], 100), [])

if __name__ == '__main__':
    unittest.main()