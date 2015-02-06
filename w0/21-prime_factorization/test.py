from solution import prime_factorization
import unittest

class MyTests(unittest.TestCase):
    def test_10(self):
       self.assertEquals(prime_factorization(10), [(2, 1), (5, 1)])

    def test_14(self):
       self.assertEquals(prime_factorization(14), [(2, 1), (7, 1)])

    def test_356(self):
       self.assertEquals(prime_factorization(356), [(2, 2), (89, 1)])

    def test_89(self):
       self.assertEquals(prime_factorization(89), [(89, 1)])

    def test_1000(self):
       self.assertEquals(prime_factorization(1000), [(2, 3), (5, 3)])



if __name__ == '__main__':
    unittest.main()