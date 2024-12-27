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

#### Exercise
- **Questions/Exercises:**
    - Review the following code and refactor it to eliminate code smells.
    ```python
    def process_orders(orders):
        total_quantity = 0
        total_price = 0
        for order in orders:
            total_quantity += order['quantity']
            total_price += order['price']
        
        average_quantity = total_quantity / len(orders)
        average_price = total_price / len(orders)
        
        return total_quantity, total_price, average_quantity, average_price

    orders = [
        {'quantity': 2, 'price': 100},
        {'quantity': 3, 'price': 150},
        {'quantity': 1, 'price': 80}
    ]
    print(process_orders(orders))
    ```

#### Solve Exercise
- **Answers/Explanations:**
    - Messy Code:
    ```python
    def process_orders(orders):
        total_quantity = 0
        total_price = 0
        for order in orders:
            total_quantity += order['quantity']
            total_price += order['price']
        
        average_quantity = total_quantity / len(orders)
        average_price = total_price / len(orders)
        
        return total_quantity, total_price, average_quantity, average_price

    orders = [
        {'quantity': 2, 'price': 100},
        {'quantity': 3, 'price': 150},
        {'quantity': 1, 'price': 80}
    ]
    print(process_orders(orders))
    ```

    - Explanation: This code calculates the total and average quantity and price of orders but has duplicated code for calculating totals and averages.

    - Clean Code:
    ```python
    def calculate_total(orders: list, key: str) -> float:
        """
        Calculate the total value for a given key in all orders.
        """
        return sum(order[key] for order in orders)

    def calculate_average(orders: list, key: str) -> float:
        """
        Calculate the average value for a given key in all orders.
        """
        total = calculate_total(orders, key)
        return total / len(orders)

    def process_orders(orders: list) -> tuple:
        """
        Process orders to calculate total and average quantity and price.
        """
        total_quantity = calculate_total(orders, 'quantity')
        total_price = calculate_total(orders, 'price')
        average_quantity = calculate_average(orders, 'quantity')
        average_price = calculate_average(orders, 'price')
        
        return total_quantity, total_price, average_quantity, average_price

    orders = [
        {'quantity': 2, 'price': 100},
        {'quantity': 3, 'price': 150},
        {'quantity': 1, 'price': 80}
    ]
    print(process_orders(orders))
    ```

    - Explanation: The code is refactored to eliminate duplicated logic by using the helper functions `calculate_total` and `calculate_average`. These helper functions are reusable and make the code cleaner and more maintainable.
