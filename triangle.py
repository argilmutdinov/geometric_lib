import math


def area(a, b, c):
    """
    Принимает три стороны треугольника a b c.
    Возвращает площадь треугольника
    """
    if (a < b + c and b < a + c and c < a + b):
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    else:
        return "Triangle doesn't exist"


def perimeter(a, b, c):
    """
    Принимает три стороны треугольника a b c.
    Возвращает периметр треугольника
    """
    try:
        return a + b + c
    except:
        return "Triangle doesn't exist"
