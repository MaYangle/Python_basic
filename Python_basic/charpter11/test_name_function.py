# test_name_function.py
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    # 方法必须用test_打头 这样它才会在我们运行test_name_function.py时自动运行
    # 这个方法名清楚地指出了它测试的是哪个行为，出现问题可以及时知道受影响的是哪个
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()