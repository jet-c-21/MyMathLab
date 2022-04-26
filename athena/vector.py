# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-chien
Create Date: 2022/3/11
"""
import sympy as sp
import mpmath
from .ult import get_quadrant_cart, get_angle_to_x_axis_cart, polar_to_cartesian_coord, get_r_for_cart_coord

mpmath.mp.dps = 15
mpmath.mp.pretty = True


def get_quadrant_of_vector(v: tuple) -> str:
    return get_quadrant_cart(v)


def get_theta_from_vector(v: tuple) -> sp.Float:
    """
    always return the positive degree
    """
    return get_angle_to_x_axis_cart(v)


def get_vector_from_mag_direct(magnitude, direction) -> tuple:
    """
    magnitude is the scalar, and direction is in degrees 
    """
    return polar_to_cartesian_coord((magnitude, direction))


def get_magnitude_of_vector(vector: tuple):
    return get_r_for_cart_coord(vector)


def add_two_vector(v1: tuple, v2: tuple) -> tuple:
    return v1[0] + v2[0], v1[1] + v2[1]
