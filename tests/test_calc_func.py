from calculate import calc


def test_correct_figure_params_1():
    fig = "square"
    func = "perimeter"
    sides = [10]

    res = calc(fig, func, sides)

    assert int(res) == 40


def test_correct_figure_params_2():
    fig = "circle"
    func = "perimeter"
    sides = [100]

    res = calc(fig, func, sides)

    assert int(res) == 628


def test_correct_figure_params_3():
    fig = "square"
    func = "area"
    sides = [3]

    res = calc(fig, func, sides)

    assert int(res) == 9


def test_correct_figure_params_4():
    fig = "circle"
    func = "area"
    sides = [8]

    res = calc(fig, func, sides)

    assert int(res) == 201


def test_incorrect_figure_params_1():
    fig = "cirkle"
    func = "area"
    sides = [8]

    res = calc(fig, func, sides)

    assert res == "Not correct figure name"


def test_incorrect_figure_params_2():
    fig = "circle"
    func = "areo"
    sides = [8]

    res = calc(fig, func, sides)

    assert res == "Not correct function name"


def test_incorrect_figure_params_3():
    fig = "squre"
    func = "perimetr"
    sides = [19]

    res = calc(fig, func, sides)

    assert res == "Not correct figure name"


def test_incorrect_figure_params_4():
    fig = "square"
    func = "area"
    sides = [3 , 5]

    res = calc(fig, func, sides)

    assert res == "Too many figure sides to calc"


def test_incorrect_figure_params_5():
    fig = "square"
    func = "area"
    sides = []

    res = calc(fig, func, sides)

    assert res == "No figure sides inputed"
