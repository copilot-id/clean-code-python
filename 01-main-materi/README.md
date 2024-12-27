### 5. Error Handling

#### Main-Materi
- **Explanation:** Error handling is the process of responding to and managing exceptions or errors that occur during the execution of a program. In Python, the `try-except` block is commonly used for this purpose. Effective error handling involves anticipating potential errors and providing meaningful responses or fallback mechanisms.
- **Data Types:** Error handling can be applied to all data types, such as integers (`int`), floating-point numbers (`float`), strings (`str`), and booleans (`bool`).

- **Example:**
    - Messy Code:
    ```python
    def divide(a, b):
        return a / b

    try:
        result = divide(10, 0)
    except Exception as e:
        print("Error:", e)
    ```

    - Explanation: This code attempts to divide by zero, which will raise an exception. However, the error handling is very generic and doesn't provide specific information about the type of error.

    - Clean Code:
    ```python
    def divide(a: float, b: float) -> float:
        """
        Divide two numbers and handle division by zero.
        """
        try:
            return a / b
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            return None

    result = divide(10, 0)
    if result is not None:
        print("Result:", result)
    ```

    - Explanation: The function `divide` includes a specific error handling for `ZeroDivisionError`, providing a meaningful message and a fallback value (`None`). The parameter and return types are annotated for clarity.
