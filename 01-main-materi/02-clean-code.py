# clean code

def divide(a: float, b: float) -> float:
    """
    Divide two numbers and handle division by zero.
    """
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None

result = divide(10, 0)
if result is not None:
    print("Result:", result)