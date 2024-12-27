# solution code

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