#### Main-Materi
- **Explanation:** Naming conventions are rules for choosing the names of variables, functions, classes, and other entities in your code. Good naming conventions make your code easier to understand and maintain. In Python, there are several standard naming conventions, such as using snake_case for variable and function names, and CamelCase for class names.
- **Data Types:** Applying naming conventions consistently across different data types, such as integers (`int`), floating-point numbers (`float`), strings (`str`), and booleans (`bool`), is crucial for clarity.

- **Example:**
    - Messy Code:
    ```python
    def calc(r):
        a = 3.14 * r**2
        return a

    x = 5
    print(calc(x))
    ```

    - Explanation: This code calculates the area of a circle, but the function and variable names are not descriptive, making the code hard to understand.

    - Clean Code:
    ```python
    def calculate_area(radius: float) -> float:
        """
        Calculate the area of a circle given its radius.
        """
        pi = 3.14159
        area = pi * radius**2
        return area

    radius = 5
    print(calculate_area(radius))
    ```

    - Explanation: The function `calculate_area` has a descriptive name, and the parameter `radius` is annotated with its data type (`float`). The variable `pi` is defined for clarity, and the function includes a docstring to explain its purpose. The overall code is properly indented and formatted.
