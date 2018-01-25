import unittest

import pepfy


class TestSearch(unittest.TestCase):
    def test_search_function_names(self):
        real = set(map(lambda fn: fn.old_name, pepfy.search_names('foo.py', pepfy.FUNCTION_KEYWORD,
                                                                  pepfy.FUNCTION_START_INDEX, pepfy.FunctionName)))
        expected = {'foo', 'Bar', 'fooBar', 'dec', 'wrapper'}
        self.assertEqual(real, expected)

    def test_search_class_names(self):
        real = set(map(lambda cn: cn.old_name, pepfy.search_names('foo.py', pepfy.CLASS_KEYWORD,
                                                                  pepfy.CLASS_START_INDEX, pepfy.ClassName)))
        expected = {'Foo', 'bar'}
        self.assertEqual(real, expected)

    def test_search_parameter_names(self):
        real = set(map(lambda pn: pn.old_name, pepfy.search_parameters('foo.py')))
        expected = {'TestOne', 'test_Two', 'TEST_THREE', '_Test_four_', 'test_five', 'testsix'}
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


class TestClassName(unittest.TestCase):
    def test_pepfy_name_correct(self):
        obj = pepfy.ClassName('PersonName')
        self.assertEqual(obj.pepfy_name(), 'PersonName')

    def test_pepfy_first_lower(self):
        obj = pepfy.ClassName('personName')
        self.assertEqual(obj.pepfy_name(), 'PersonName')

    def test_pepfy_constant_like(self):
        obj = pepfy.ClassName('PERSON_NAME')
        self.assertEqual(obj.pepfy_name(), 'PersonName')

    def test_pepfy_function_like(self):
        obj = pepfy.ClassName('person_name')
        self.assertEqual(obj.pepfy_name(), 'PersonName')

    def test_pepfy_underline_beginning(self):
        obj = pepfy.ClassName('_person_name')
        self.assertEqual(obj.pepfy_name(), 'PersonName')

    def test_pepfy_underline_end(self):
        obj = pepfy.ClassName('person_name_')
        self.assertEqual(obj.pepfy_name(), 'PersonName')

    def test_pepfy_double_underline(self):
        obj = pepfy.ClassName('person__name')
        self.assertEqual(obj.pepfy_name(), 'PersonName')


class TestParameterName(unittest.TestCase):
    def test_pepfy_name_correct(self):
        obj = pepfy.ParameterName('h_world')
        self.assertEqual(obj.pepfy_name(), 'h_world')

    def test_pepfy_name_cammel_case(self):
        obj = pepfy.ParameterName('hWorld')
        self.assertEqual(obj.pepfy_name(), 'h_world')

    def test_pepfy_name_class_like(self):
        obj = pepfy.ParameterName('HWorld')
        self.assertEqual(obj.pepfy_name(), 'h_world')

    def test_pepfy_name_constant_like(self):
        obj = pepfy.ParameterName('HWORLD')
        self.assertEqual(obj.pepfy_name(), 'h_w_o_r_l_d')

    def test_pepfy_name_one(self):
        obj = pepfy.ParameterName('H')
        self.assertEqual(obj.pepfy_name(), 'h')


if __name__ == '__main__':
    unittest.main()
