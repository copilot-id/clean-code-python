# messy code

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