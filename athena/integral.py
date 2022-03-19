# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-chien
Create Date: 2022/3/11
"""
from .sympy_symbols import *


def get_line_by_2p(p1, p2) -> sp.Equality:
    delta_y = p1[1] - p2[1]
    delta_x = p1[0] - p2[0]
    slope = sp.Rational(delta_y, delta_x)

    # y = m * (x - x') + y'
    return sp.Eq(y, slope * (x - p1[0]) + p1[1])
