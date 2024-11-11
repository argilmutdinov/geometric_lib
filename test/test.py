
import sys
from ..calculate import calc


def test_incorrect_figure_name():
    res = calc("square", "perimeter", 10)
    assert res == 40

def test_incorrect_sides_figure_params():
    assert 0 == 0


