import unittest
from city import city_form

class test_city_country(unittest.TestCase):

    def test_single_city(self):
        """正确处理单个的城市，国家"""
        formatted_city = city_form('santiago','chile',population=10000)
        self.assertEqual(formatted_city,'Santiago,Chile-Population 10000')


if __name__ == '__main__':
    unittest.main()

