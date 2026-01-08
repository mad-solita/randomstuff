import math

def circumference_of_circle(radius:float) -> float:
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return 2 * math.pi * radius

if __name__ == "__main__":
    radius = float(input('Must be float: ').replace(",","."))
    print(circumference_of_circle(radius))