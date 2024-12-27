### 8. Documentation and Comments

#### Main-Materi
- **Explanation:** Documentation and comments provide context and explanations about the code, making it easier to understand and maintain. Good documentation includes clear and concise descriptions of what the code does, how to use it, and any important details. Comments should be used to explain the purpose of complex or non-obvious code sections, but should not be overused.
- **Data Types:** Documentation and comments are applicable to all data types, such as integers (`int`), floating-point numbers (`float`), strings (`str`), and booleans (`bool`).

- **Example:**
    - Messy Code (without comments):
    ```python
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    print(factorial(5))  # Expected output: 120
    ```

    - Explanation: This code calculates the factorial of a number but lacks comments and documentation, making it harder to understand.

    - Clean Code (with comments and documentation):
    ```python
    def factorial(n: int) -> int:
        """
        Calculate the factorial of a non-negative integer.
        
        Parameters:
        n (int): A non-negative integer whose factorial is to be calculated.

        Returns:
        int: The factorial of the given number.
        """
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    print(factorial(5))  # Expected output: 120
    ```

    - Explanation: The `factorial` function includes a docstring explaining its purpose, parameters, and return value. This makes the code easier to understand and maintain. The comments are used sparingly to clarify the logic.
