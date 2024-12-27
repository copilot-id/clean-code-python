### 4. Functions and Methods

#### Main-Materi
- **Explanation:** Functions and methods are the building blocks of any program. Writing clear and concise functions involves ensuring that each function has a single responsibility and avoids duplicating code (DRY principle). Functions should be short, well-named, and perform a specific task.
- **Data Types:** Functions and methods often work with various data types, such as integers (`int`), floating-point numbers (`float`), strings (`str`), and booleans (`bool`). Proper data type annotation is essential for clarity.

- **Example:**
    - Messy Code:
    ```python
    def process_data(data):
        result = []
        for item in data:
            if item % 2 == 0:
                result.append(item * 2)
            else:
                result.append(item * 3)
        return result

    data = [1, 2, 3, 4, 5]
    print(process_data(data))
    ```

    - Explanation: This function processes data but lacks clear responsibilities and has mixed logic for even and odd numbers, making it harder to understand and maintain.

    - Clean Code:
    ```python
    def process_even_numbers(data: list) -> list:
        """
        Process even numbers in the data list by doubling them.
        """
        return [item * 2 for item in data if item % 2 == 0]

    def process_odd_numbers(data: list) -> list:
        """
        Process odd numbers in the data list by tripling them.
        """
        return [item * 3 for item in data if item % 2 == 1]

    data = [1, 2, 3, 4, 5]
    even_numbers = process_even_numbers(data)
    odd_numbers = process_odd_numbers(data)
    print(even_numbers + odd_numbers)
    ```

    - Explanation: The code is refactored into two separate functions `process_even_numbers` and `process_odd_numbers`, each with a single responsibility. The functions have clear names and data type annotations, and the logic is simplified using list comprehensions.

#### Exercise
- **Questions/Exercises:**
    - Review the following code and refactor it to follow the principles of clear and concise functions.
    ```python
    def calculate(numbers):
        even_sum = 0
        odd_sum = 0
        for number in numbers:
            if number % 2 == 0:
                even_sum += number
            else:
                odd_sum += number
        return even_sum, odd_sum

    numbers = [1, 2, 3, 4, 5]
    print(calculate(numbers))
    ```

#### Solve Exercise
- **Answers/Explanations:**
    - Messy Code:
    ```python
    def calculate(numbers):
        even_sum = 0
        odd_sum = 0
        for number in numbers:
            if number % 2 == 0:
                even_sum += number
            else:
                odd_sum += number
        return even_sum, odd_sum

    numbers = [1, 2, 3, 4, 5]
    print(calculate(numbers))
    ```

    - Explanation: This function calculates the sum of even and odd numbers but mixes the logic for even and odd numbers, making it less clear.

    - Clean Code:
    ```python
    def calculate_even_sum(numbers: list) -> int:
        """
        Calculate the sum of even numbers in the list.
        """
        return sum(number for number in numbers if number % 2 == 0)

    def calculate_odd_sum(numbers: list) -> int:
        """
        Calculate the sum of odd numbers in the list.
        """
        return sum(number for number in numbers if number % 2 != 0)

    numbers = [1, 2, 3, 4, 5]
    even_sum = calculate_even_sum(numbers)
    odd_sum = calculate_odd_sum(numbers)
    print(even_sum, odd_sum)
    ```

    - Explanation: The code is refactored into two separate functions `calculate_even_sum` and `calculate_odd_sum`, each with a single responsibility. The functions have clear names and data type annotations, and the logic is simplified.
