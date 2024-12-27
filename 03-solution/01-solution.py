# Code Review Comments

# 1. Add type annotations for clarity.
# 2. Handle edge cases, such as negative prices or discount rates.
# 3. Optimize the code using list comprehensions.
# 4. Add a docstring to explain the function.

# Refactored Code After Review:
def apply_discount(prices: list, discount_rate: float) -> list:
    """
    Apply a discount to a list of prices.

    Parameters:
    prices (list): A list of original prices.
    discount_rate (float): The discount rate as a decimal.

    Returns:
    list: A list of discounted prices.
    """
    if discount_rate < 0:
        raise ValueError("Discount rate must be non-negative.")
    return [price - (price * discount_rate) for price in prices]

prices = [100, 200, 300]
discount_rate = 0.1
print(apply_discount(prices, discount_rate))