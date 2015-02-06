from solution import prepare_meal
import unittest

class MyTests(unittest.TestCase):
    def test_one(self):
        self.assertEquals(prepare_meal(3), 'spam')

    def test_two(self):
        self.assertEquals(prepare_meal(27),'spam spam spam')

    def test_three(self):
        self.assertEquals( prepare_meal(7), '')

    def test_foure(self):
        self.assertEquals(prepare_meal(5), "eggs")

    def test_five(self):
        self.assertEquals(prepare_meal(15), "spam and eggs")

    def test_six(self):
        self.assertEquals(prepare_meal(45), "spam spam and eggs")


if __name__ == '__main__':
    unittest.main()