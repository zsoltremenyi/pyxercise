import unittest
from calculations import Calculations

class TestCases(unittest.TestCase):

    def test_mean(self):
        calc = Calculations([100,200,1000,300])
        actual = calc.mean()
        expected = 400
        self.assertEqual(actual,expected)

    def test_standev(self):
        calc = Calculations([100, 200, 1000, 300])
        actual = round(calc.standard_dev(), 2)
        expected = 353.55
        self.assertEqual(actual,expected)


if __name__ == "__main__":
    unittest.main()