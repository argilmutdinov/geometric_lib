import triangle

def test_circle_area_1():
    a_side = 10
    b_side = 10
    c_side = 10

    res = triangle.area(a_side, b_side, c_side)

    assert int(res) == 43

def test_circle_area_1():
    a_side = 2
    b_side = 4
    c_side = 6

    res = triangle.area(a_side, b_side, c_side)

    assert res == "Triangle doesn't exist"

def test_circle_perimeter_1():
    a_side = 3
    b_side = 4
    c_side = 5

    res = triangle.perimeter(a_side, b_side, c_side)

    assert res == 12

def test_circle_perimeter_2():
    a_side = 13
    b_side = 5
    c_side = 10

    res = triangle.perimeter(a_side, b_side, c_side)

    assert res == 28