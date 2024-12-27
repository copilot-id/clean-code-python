# clean code

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

print(calculate_total_price([{'price': 10}, {'price': 20}, {'price': 30}]))  # 60
print(calculate_average_price([{'price': 10}, {'price': 20}, {'price': 30}]))  # 20.0
