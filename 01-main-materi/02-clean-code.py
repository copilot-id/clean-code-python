# clean code

def process_even_numbers(data: list) -> list:
    """
    Process even numbers in the data list by doubling them.
    """
    return [item * 2 for item in data if item % 2 == 0]

def process_odd_numbers(data: list) -> list:
    """
    Process odd numbers in the data list by tripling them.
    """
    return [item * 3 for item in data if item % 2 == 1]

data = [1, 2, 3, 4, 5]
even_numbers = process_even_numbers(data)
odd_numbers = process_odd_numbers(data)
print(even_numbers + odd_numbers)