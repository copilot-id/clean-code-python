# Code Review Comments
# 1. Add type annotations for clarity.
# 2. Handle edge cases, such as negative prices or discount rates.
# 3. Add a docstring to explain the function.

def calculate_discount(price: float, discount_rate: float) -> float:
    """
    Calculate the discounted price.

    Parameters:
    price (float): The original price.
    discount_rate (float): The discount rate as a decimal.

    Returns:
    float: The discounted price.
    """
    if price < 0 or discount_rate < 0:
        raise ValueError("Price and discount rate must be non-negative.")
    return price - (price * discount_rate)