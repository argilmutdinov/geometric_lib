import square

def test_circle_area_1():
    side = 10

    res = square.area(side)

    assert res == 100

def test_circle_area_2():
    side = 1

    res = square.area(side)

    assert res == 1

def test_circle_perimeter_1():
    side = 10

    res = square.perimeter(side)

    assert res == 40

def test_circle_perimeter_2():
    side = 1

    res = square.perimeter(side)

    assert res == 4