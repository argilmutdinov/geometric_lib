import math


def area(a, b, c):
    """
    Принимает три стороны треугольника a b c.
    Возвращает площадь треугольника
    """
    try:
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    except:
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
