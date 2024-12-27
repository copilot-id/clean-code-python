### 7. Unit Testing and Test-Driven Development (TDD)

#### Main-Materi
- **Explanation:** Unit testing involves writing tests for individual units of code (e.g., functions, methods) to ensure they perform as expected. Test-Driven Development (TDD) is a practice where you write the test cases before writing the corresponding code. This helps in writing more reliable and bug-free code.

- **Data Types:** Testing applies to all data types, such as integers (`int`), floating-point numbers (`float`), strings (`str`), and booleans (`bool`).

- **Example:**
    - Messy Code (without tests):
    ```python
    def add(a, b):
        return a + b

    result = add(2, 3)
    print(result)  # Expected output: 5
    ```

    - Explanation: This code defines a simple addition function and prints the result, but it lacks formal tests to verify the function's correctness.

    - Clean Code (with tests):
    ```python
    import unittest

    def add(a: int, b: int) -> int:
        """
        Add two numbers.
        """
        return a + b

    class TestAddFunction(unittest.TestCase):
        def test_add_positive_numbers(self):
            self.assertEqual(add(2, 3), 5)

        def test_add_negative_numbers(self):
            self.assertEqual(add(-1, -1), -2)

        def test_add_zero(self):
            self.assertEqual(add(0, 0), 0)

    if __name__ == '__main__':
        unittest.main()
    ```

    - Explanation: This code defines the `add` function with data type annotations and a docstring. It also includes unit tests using the `unittest` module to verify the function's correctness with different input scenarios.
