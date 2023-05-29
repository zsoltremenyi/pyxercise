import unittest
from translated_output import Translation


class TestTranslation(unittest.TestCase):
    def setUp(self):
        self.translation = Translation('french')

    def test_trans_input(self):
        # test trans_input() method
        actual_output = self.translation.trans_input()
        expected_output = '3'
        self.assertEqual(actual_output, expected_output)

    def test_trans_output(self):
        # test the trans_output method with a valid number
        number = '5'
        expected_output = 'Le nom du mois est Mai.'
        self.assertEqual(self.translation.trans_output(number), expected_output)

        invalid_number = '13'
        expected_error_message = f"{invalid_number} is not a valid number (1-12)."
        with self.assertRaises(ValueError) as context:
            self.translation.trans_output(invalid_number)
        self.assertEqual(str(context.exception), expected_error_message)


if __name__ == '__main__':
    unittest.main()