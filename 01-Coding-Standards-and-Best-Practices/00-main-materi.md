### 2. Coding Standards and Best Practices

#### Main-Materi
- **Explanation:** Coding standards and best practices are guidelines that help maintain code quality, readability, and consistency across a project. In Python, PEP 8 is the most widely accepted style guide for writing clean and readable code.

- **Data Types:** While coding standards apply to all data types, it's important to annotate data types for clarity. Common data types in Python include integers (`int`), floating-point numbers (`float`), strings (`str`), and booleans (`bool`).

- **Example:**
    - Messy Code:
    ```python
    def calArea(r):
        a = 3.14 * r**2
        return a
    x = 5
    print(calArea(x))
    ```

    - Explanation: This code calculates the area of a circle but lacks meaningful variable names, proper indentation, and consistent formatting.

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
