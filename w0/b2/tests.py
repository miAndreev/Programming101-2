from magic_string import magic_string
import unittest


class MagicStringTest(unittest.TestCase):
    """Testing magic_string - 250 problem from TC SRM 609 Div 2"""
    def test_problem_statement_cases(self):
        self.assertEqual(2, magic_string(">><<><"))
        self.assertEqual(0, magic_string(">>>><<<<"))
        self.assertEqual(4, magic_string("<<>>"))
        self.assertEqual(20,
                         magic_string(
                         "<><<<>>>>><<>>>>><>><<<>><><><><<><<<<<><<>>><><><"))

if __name__ == '__main__':
    unittest.main()