import math

radius = float(input('Must be float: ').replace(",","."))

def circumference_of_circle(radius:float):
    result = 2*math.pi*radius
    print(result)
    return result

circumference_of_circle(radius)