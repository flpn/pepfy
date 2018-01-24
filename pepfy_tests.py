import unittest

import pepfy


class TestSearch(unittest.TestCase):
    def test_search_function_names(self):
        real = set(map(lambda fn: fn.old_name, pepfy.search_names('foo.py', pepfy.FUNCTION_KEYWORD,
                                                                  pepfy.FUNCTION_START_INDEX, pepfy.FunctionName)))
        expected = {'foo', 'Bar', 'fooBar', 'dec', 'wrapper'}
        self.assertEqual(real, expected)

    def test_search_class_names(self):
        real = set(map(lambda fn: fn.old_name, pepfy.search_names('foo.py', pepfy.CLASS_KEYWORD,
                                                                  pepfy.CLASS_START_INDEX, pepfy.ClassName)))
        expected = {'Foo', 'bar'}
        self.assertEqual(real, expected)


class TestFunctionName(unittest.TestCase):
    def test_pepfy_name_correct(self):
        obj = pepfy.FunctionName('h_world')
        self.assertEqual(obj.pepfy_name(), 'h_world')

    def test_pepfy_name_cammel_case(self):
        obj = pepfy.FunctionName('hWorld')
        self.assertEqual(obj.pepfy_name(), 'h_world')

    def test_pepfy_name_class_like(self):
        obj = pepfy.FunctionName('HWorld')
        self.assertEqual(obj.pepfy_name(), 'h_world')

    def test_pepfy_name_constant_like(self):
        obj = pepfy.FunctionName('HWORLD')
        self.assertEqual(obj.pepfy_name(), 'h_w_o_r_l_d')

    def test_pepfy_name_one(self):
        obj = pepfy.FunctionName('H')
        self.assertEqual(obj.pepfy_name(), 'h')


if __name__ == '__main__':
    unittest.main()
