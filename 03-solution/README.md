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
