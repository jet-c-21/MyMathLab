# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-chien
Create Date: 2022/3/11
"""
import sympy as sp


def get_eq_sq_both_side(eq) -> sp.Equality:
    return sp.Eq(eq.lhs ** 2, eq.rhs ** 2)
