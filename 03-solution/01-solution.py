# solution code
    
def calculate_even_sum(numbers: list) -> int:
    """
    Calculate the sum of even numbers in the list.
    """
    return sum(number for number in numbers if number % 2 == 0)

def calculate_odd_sum(numbers: list) -> int:
    """
    Calculate the sum of odd numbers in the list.
    """
    return sum(number for number in numbers if number % 2 != 0)

numbers = [1, 2, 3, 4, 5]
even_sum = calculate_even_sum(numbers)
odd_sum = calculate_odd_sum(numbers)
print(even_sum, odd_sum)
