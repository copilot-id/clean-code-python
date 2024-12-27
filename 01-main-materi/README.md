### 6. Code Smells and Refactoring

#### Main-Materi
- **Explanation:** Code smells are indicators of potential problems in your code that may hinder its readability, maintainability, or performance. Refactoring is the process of improving the structure and readability of existing code without changing its functionality. Common code smells include duplicated code, long functions, and large classes.

- **Data Types:** Code smells and refactoring apply to all data types, including integers (`int`), floating-point numbers (`float`), strings (`str`), and booleans (`bool`).

- **Example:**
    - Messy Code:
    ```python
    def calculate_total_price(items):
        total = 0
        for item in items:
            total += item['price']
        return total

    def calculate_average_price(items):
        total = 0
        count = 0
        for item in items:
            total += item['price']
            count += 1
        return total / count
    ```

    - Explanation: This code calculates the total and average price of items but has duplicated code for calculating the total price.

    - Clean Code:
    ```python
    def calculate_total_price(items: list) -> float:
        """
        Calculate the total price of all items.
        """
        return sum(item['price'] for item in items)

    def calculate_average_price(items: list) -> float:
        """
        Calculate the average price of all items.
        """
        total_price = calculate_total_price(items)
        return total_price / len(items)
    ```

    - Explanation: The function `calculate_total_price` is reused in `calculate_average_price`, eliminating the duplicated code. Both functions have clear names, data type annotations, and are well-documented.
