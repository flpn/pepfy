import unittest

import pepfy


class TestSearches(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
