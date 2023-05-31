import unittest
from largestnum import largest_num


class UnitTests(unittest.TestCase):

    def test1(self):
        alist = [2, 4, 10]
        actual_output = largest_num(alist)
        expected_output = 10
        self.assertEqual(actual_output,expected_output)

    def testnegative(self):
        neg_list = [-1, -4, -19]
        actual_output = largest_num(neg_list)
        expected_output = -1
        self.assertEqual(actual_output, expected_output)




if __name__ == '__main__':
    unittest.main()