# Clean Code (with comments and documentation):
def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Expected output: 120