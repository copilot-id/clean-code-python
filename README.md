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

#### Exercise
- **Questions/Exercises:**
    - Review the following code and improve the error handling.
    ```python
    def read_file(file_path):
        with open(file_path, 'r') as file:
            return file.read()

    try:
        content = read_file('nonexistent_file.txt')
        print(content)
    except Exception as e:
        print("Error:", e)
    ```

#### Solve Exercise
- **Answers/Explanations:**
    - Messy Code:
    ```python
    def read_file(file_path):
        with open(file_path, 'r') as file:
            return file.read()

    try:
        content = read_file('nonexistent_file.txt')
        print(content)
    except Exception as e:
        print("Error:", e)
    ```

    - Explanation: This code attempts to read a nonexistent file, which will raise an exception. The error handling is very generic and doesn't provide specific information about the type of error.

    - Clean Code:
    ```python
    def read_file(file_path: str) -> str:
        """
        Read the contents of a file and handle file-related errors.
        """
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print("Error: The file was not found.")
            return None
        except IOError:
            print("Error: An I/O error occurred.")
            return None

    content = read_file('nonexistent_file.txt')
    if content is not None:
        print(content)
    ```

    - Explanation: The function `read_file` includes specific error handling for `FileNotFoundError` and `IOError`, providing meaningful messages and fallback values (`None`). The parameter and return types are annotated for clarity.
