# solution code

def calculate_volume_cube(side_length: float) -> float:
    """
    Calculate the volume of a cube given its side length.
    """
    volume = side_length**3
    return volume

side_length = 3
print(calculate_volume_cube(side_length))