# solution code
def fibonacci(n: int) -> list:
    """
    Generate the Fibonacci sequence up to the nth term.

    Parameters:
    n (int): The number of terms in the Fibonacci sequence to generate.

    Returns:
    list: A list containing the Fibonacci sequence up to the nth term.
    """
    if n <= 0:
            return []  # Return an empty list for non-positive input
    elif n == 1:
        return [0]  # Return [0] for input 1
    elif n == 2:
        return [0, 1]  # Return [0, 1] for input 2
    else:
        fib_seq = [0, 1]  # Initialize the Fibonacci sequence with the first two terms
        for i in range(2, n):
            fib_seq.append(fib_seq[-1] + fib_seq[-2])  # Append the sum of the last two terms
        return fib_seq

print(fibonacci(10))  # Expected output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]