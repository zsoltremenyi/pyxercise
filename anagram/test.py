import unittest
from word_length import word_length
from compare import comparing


class TestCases(unittest.TestCase):

    def test_length_one(self):
        actual_output = word_length("maka", "kakaka")
        expected_output = [4, 6]
        self.assertEqual(actual_output, expected_output)

    def test_length_same(self):
        actual_output = word_length("aaaa", "bbbb")
        expected_output = [4, 4]
        self.assertEqual(actual_output, expected_output)

    def test_compare_true(self):
        actual_output = comparing("fafa", "affa")
        expected_output = "fafa and affa are anagrams."
        self.assertEqual(actual_output,expected_output)

    def test_compare_false(self):
        actual_output = comparing("kli", "bab")
        expected_output = "kli and bab are not anagrams."
        self.assertEqual(actual_output,expected_output)


if __name__ == '__main__':
    unittest.main()
