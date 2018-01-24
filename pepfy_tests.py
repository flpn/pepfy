import unittest

import pepfy


class TestFunctions(unittest.TestCase):
    def test_beauty_header(self):
        inp = 'def hello_world(person_name):'
        self.assertEqual(pepfy.pep_function_header(inp), inp)

    def test_ugly_class_like(self):
        inp = 'def HelloWorld(PersonNamE):'
        out = 'def hello_world(person_name):'
        self.assertEqual(pepfy.pep_function_header(inp), out)

    def test_ugly_camel_case(self):
        inp = 'def helloWorld(personName):'
        out = 'def hello_world(person_name):'
        self.assertEqual(pepfy.pep_function_header(inp), out)


if __name__ == '__main__':
    unittest.main()
