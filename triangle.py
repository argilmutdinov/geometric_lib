import math


def area(a, b, c):
    """
    Принимает три стороны треугольника a b c.
    Возвращает площадь треугольника
    """

    try:
        if not (a < b + c and b < a + c and c < a + b):
            raise ValueError
    except Exception:
        return "Triangle doesn't exist"
    else:
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


def perimeter(a, b, c):
    """
    Принимает три стороны треугольника a b c.
    Возвращает периметр треугольника
    """

    try:
        if not (a < b + c and b < a + c and c < a + b):
            raise ValueError
    except Exception:
        return "Triangle doesn't exist"
    else:
        return a + b + c
