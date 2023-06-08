import unittest
from employee import Employee


class TestCases(unittest.TestCase):

    def setUp(self):
        self.emp1 = Employee("df3", "2344", "lkj", "assdfa")
        self.emp2 = Employee("lkk-234", "2344", "lkj", "assdfa")
        self.emp3 = Employee("lk-2341", "k", "lkj", "lkj")
        self.emp4 = Employee("lk-2341", "234", "3l", "lkj")

    def test_shortid(self):
        actual_output = self.emp1.employee_id()
        expected_output = False
        self.assertEqual(actual_output, expected_output)

    def test_wrongid(self):
        wrong_id = self.emp2.employee_id()
        self.assertFalse(wrong_id)

    def test_wrongzip(self):
        wrong_zip = self.emp3.zipcode()
        self.assertFalse(wrong_zip)

    def test_incorrect_name(self):
        inc_name = self.emp4.first_name()
        self.assertFalse(inc_name)


if __name__ == "__main__":
    unittest.main()