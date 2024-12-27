# exercise code

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