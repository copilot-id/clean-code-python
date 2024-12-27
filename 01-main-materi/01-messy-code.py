# messy code

def divide(a, b):
    return a / b

try:
    result = divide(10, 0)
except Exception as e:
    print("Error:", e)