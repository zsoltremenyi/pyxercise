import unittest
import guessing_module as gm


class TestCases(unittest.TestCase):

    def test_equal(self):
        output = gm.guessing(1, 1)
        expected = None
        self.assertEqual(output,expected)


if __name__ == "__main__":
    unittest.main()