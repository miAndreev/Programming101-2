from solution  import nth_fibonacci
import unittest

class MyTestCase(unittest.TestCase):
    
    def test_fibonacci_one(self):
        self.assertEqual(1, nth_fibonacci(1))

    def test_fibonacci_two(self):
        self.assertEqual(1, nth_fibonacci(2))

    def test_fibonacci_tree(self):
        self.assertEqual(2, nth_fibonacci(3))

    def test_fibonacci_ten(self):
        self.assertEqual(55, nth_fibonacci(10))
    
if __name__ == '__main__':
    unittest.main()