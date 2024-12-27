def is_positive_odd(number: int) -> bool:
    """
    Check if a number is positive and odd.
    """
    return number > 0 and number % 2 == 1

print(is_positive_odd(2)) # False
print(is_positive_odd(3)) # True
