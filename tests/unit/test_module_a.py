import unittest
from src.module_a import function_to_test

class TestModuleA(unittest.TestCase):
    def test_function_to_test(self):
        result = function_to_test(2, 3)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main() 