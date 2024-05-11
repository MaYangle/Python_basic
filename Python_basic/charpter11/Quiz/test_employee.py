import unittest
from employee import Employee
class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.my_employee = Employee("Rita","Li",20000)
    def test_give_default_raise(self):
        self.my_employee.give_raise(raise1=5000)
        self.assertEqual(25000,self.my_employee.salary)

if "__name__" == "__main__":
    unittest.main()
