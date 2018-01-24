import unittest

import pepfy


class TestSearches(unittest.TestCase):
    def test_search_function_names(self):
        real = set(map(lambda fn: fn.old_name, pepfy.search_function_names('foo.py')))
        expected = {'foo', 'Bar', 'fooBar', 'dec', 'wrapper'}
        self.assertEqual(real, expected)


if __name__ == '__main__':
    unittest.main()
