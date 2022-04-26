# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-chien
Create Date: 2022/3/11
"""
import mpmath
import sympy as sp


def square_eq_both_side(eq) -> sp.Equality:
    return sp.Eq(eq.lhs ** 2, eq.rhs ** 2)


def get_quadrant_cart(t: tuple) -> str:
    """
    t can be a point or a vector in Cartesian Coordinate System

    :param t: tuple
    :return: quadrant str
    """
    x, y = t[0], t[1]
    if x == 0 and y == 0:
        return 'origin'
    elif x == 0:
        return 'y-axis'
    elif y == 0:
        return 'x-axis'
    elif x > 0 and y > 0:
        return 'q1'
    elif x < 0 and y > 0:
        return 'q2'
    elif x < 0 and y < 0:
        return 'q3'
    elif x > 0 and y < 0:
        return 'q4'
    else:
        return '[WARN] - Need to debug!'


def get_angle_to_x_axis_cart(t: tuple) -> sp.Float:
    """
    t can be a point or a vector in Cartesian Coordinate System

    :param t: tuple
    :return: always return the positive degree
    """
    x, y = sp.Float(t[0]), sp.Float(t[1])
    tangent = y / x
    rad = sp.N(sp.atan(tangent))
    deg = mpmath.degrees(rad)

    # fix deg by quadrant
    q = get_quadrant_cart(t)
    if q == 'q2' or q == 'q3':
        deg += 180
    elif q == 'q4':
        deg += 360

    return deg


def get_r_for_cart_coord(t: tuple) -> sp.Float:
    """
    t can be a point or a vector in Cartesian Coordinate System

    :param t:
    :return:
    """
    try:
        a = sp.Float(t[0])
        b = sp.Float(t[1])
    except Exception as e:
        msg = f"[INFO] - Cannot convert val_1: {t[0]}, val_2: {t[1]} into float. Error: {e}"
        print(msg)

        a, b = t[0], t[1]

    return sp.sqrt(a ** 2 + b ** 2)


def cartesian_to_polar_coord(t: tuple) -> tuple:
    """
    t can be a point or a vector in Cartesian Coordinate System

    :param t: tuple
    :return: (r, theta)
    """
    r = get_r_for_cart_coord(t)
    theta = get_angle_to_x_axis_cart(t)

    return r, theta


def polar_to_cartesian_coord(t: tuple) -> tuple:
    """
    - t is based on Polar Coordinate System
    - theta need is for degrees

    :param t:
    :return: (x, y)
    """
    r, theta = t[0], t[1]
    rad = mpmath.radians(theta)

    return r * sp.cos(rad), r * sp.sin(rad)
