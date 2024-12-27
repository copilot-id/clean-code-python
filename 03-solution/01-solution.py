# solution code

import unittest

def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers.
    """
    return a * b

class TestMultiplyFunction(unittest.TestCase):
    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-1, 3), -3)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(0, 10), 0)

if __name__ == '__main__':
    unittest.main()