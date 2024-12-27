# clean code

def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle given its radius.
    """
    pi = 3.14159
    area = pi * radius**2
    return area

radius = 5
print(calculate_area(radius))