from calculate import calc
import pytest


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
    with pytest.raises(Exception) as e:
        fig = "cirkle"
        func = "area"
        sides = [8]

        calc(fig, func, sides)

        assert str(e.value) == "Not correct figure name"


def test_incorrect_figure_params_2():
    with pytest.raises(Exception) as e:
        fig = "circle"
        func = "areo"
        sides = [8]

        calc(fig, func, sides)

        assert str(e.value) == "Not correct function name"


def test_incorrect_figure_params_3():
    with pytest.raises(Exception) as e:
        fig = "squre"
        func = "perimetr"
        sides = [19]

        calc(fig, func, sides)

        assert str(e.value) == "Not correct figure name"


def test_incorrect_figure_params_4():
    with pytest.raises(Exception) as e:
        fig = "square"
        func = "area"
        sides = [3 , 5]

        calc(fig, func, sides)

        assert str(e.value) == "Too many figure sides to calc"


def test_incorrect_figure_params_5():
    with pytest.raises(Exception) as e:
        fig = "square"
        func = "area"
        sides = []

        calc(fig, func, sides)

        assert str(e.value) == "No figure sides inputed"
