import unittest
from largestnum import largest_num


class UnitTests(unittest.TestCase):

    def test1(self):
        alist = [2, 4, 10]
        actual_output1 = largest_num(alist)
        expected_output = "\nThe largest number in list is: 10"
        self.assertEqual(actual_output1, expected_output)

    def testnegative(self):
        neg_list = [-1, -4, -19]
        actual_output2 = largest_num(neg_list)
        expected_output = "\nThe largest number in list is: -1"
        self.assertEqual(actual_output2, expected_output)

    def test_for_zero(self):
        list_with_zero = [-4, -2, 0]
        actual_output3 = largest_num(list_with_zero)
        expected_output = "\nThe largest number in list is: 0"
        self.assertEqual(actual_output3,expected_output)


if __name__ == '__main__':
    unittest.main()