import circle
import math

def test_circle_area_1():
    radius = 10

    res = circle.area(radius)

    assert int(res) == 314

def test_circle_area_2():
    radius = 1

    res = circle.area(radius)

    assert res == math.pi

def test_circle_perimeter_1():
    radius = 10

    res = circle.perimeter(radius)

    assert int(res) == 62

def test_circle_perimeter_2():
    radius = 1

    res = circle.perimeter(radius)

    assert res == 2*math.pi

