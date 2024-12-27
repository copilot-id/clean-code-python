#### Solve Exercise
- **Answers/Explanations:**
    - Messy Code (without tests):
    ```python
    def multiply(a, b):
        return a * b

    result = multiply(2, 3)
    print(result)  # Expected output: 6
    ```

    - Explanation: This code defines a simple multiplication function and prints the result, but it lacks formal tests to verify the function's correctness.

    - Clean Code (with tests):
    ```python
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
    ```

    - Explanation: The `multiply` function is defined with data type annotations and a docstring. Unit tests are created using the `unittest` module to check the function's correctness with different input scenarios, such as positive numbers, negative numbers, and zero.
