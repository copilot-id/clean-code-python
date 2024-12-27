#### Solve Exercise
- **Answers/Explanations:**
  - Messy Code:
  ```python
  def b(y):
      if y > 0 and y % 2 == 1:
          return True
      else:
          return False
  ```
  - Explanation: This function checks if a number is positive and odd. The function name `b` and variable `y` are not descriptive, making the code unclear.

  - Clean Code:
  ```python
  def is_positive_odd(number: int) -> bool:
      """
      Check if a number is positive and odd.
      """
      return number > 0 and number % 2 == 1
  ```
  - Explanation: The function name `is_positive_odd` clearly conveys its purpose. The parameter `number` is annotated with its data type (`int`), and the return type is `bool`. The docstring explains the function's purpose, and the logic is clear and concise.
  