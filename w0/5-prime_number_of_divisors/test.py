from solution import prime_number_of_divisors
import unittest

class MyTests(unittest.TestCase):
    def test_one(self):
        self.assertEqual(True, prime_number_of_divisors(7))

    def test_two(self):
        self.assertEqual(False, prime_number_of_divisors(8))
    
    def test_tree(self):
        self.assertEqual(True, prime_number_of_divisors(9))

if __name__ == '__main__':
    unittest.main()