### 1. Introduction to Clean Code

#### Main-Materi
- **Explanation:** Clean code refers to writing code that is easy to understand, maintain, and extend. It involves using meaningful names, clear and concise functions, proper indentation, and comments. Clean code helps other developers (and your future self) to easily understand the logic and purpose of your code.

- **Data Types:** Data types specify the kind of data that a variable can hold. Common Python data types include integers (`int`), floating-point numbers (`float`), strings (`str`), and booleans (`bool`). Understanding data types is essential for writing clean and efficient code.

- **Example:**
  - Messy Code:
  ```python
  def a(x):
      if x % 2 == 0:
          return True
      else:
          return False
  ```
  - Explanation: This function checks if a number is even. However, the function name and variable names are not meaningful, making the code hard to understand.

  - Clean Code:
  ```python
  def is_even(number: int) -> bool:
      """
      Check if a number is even.
      """
      return number % 2 == 0
  ```
  - Explanation: The function `is_even` clearly conveys what it does. The parameter `number` is annotated with its data type (`int`), and the return type is `bool`. The docstring explains the function's purpose, and the logic is clear and concise.

- **How to Solve:** Start by following coding standards and best practices like using meaningful variable names, clear comments, and breaking down complex functions into smaller ones. Always aim for readability and simplicity.

#### Exercise
- **Questions/Exercises:**
  - Review the following code and rewrite it to be cleaner and more readable.
  ```python
  def b(y):
      if y > 0 and y % 2 == 1:
          return True
      else:
          return False
  ```

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
