# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-chien
Create Date: 2022/3/11
"""
import sympy as sp
import mpmath

mpmath.mp.dps = 15
mpmath.mp.pretty = True

def get_quadrant_of_vector(v: tuple) -> str:
    x, y = v[0], v[1]
    if x == 0 and y == 0:
        return 'origin'
    elif x == 0 :
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
    

def get_theata_from_vector(v: tuple) -> sp.Float:
    """
    always return the positive degree
    """
    x, y = sp.Float(v[0]), sp.Float(v[1])
    tangent = y / x
    rad = sp.N(sp.atan(tangent))
    deg = mpmath.degrees(rad)
    
    # fix deg by quadrant
    q = get_quadrant_of_vector(v)
    if q == 'q2' or q=='q3':
        deg += 180
    elif q == 'q4':
        deg += 360
    
    return deg


def get_vector_from_mag_direct(magnitude, direction) -> tuple:
    """
    magnitude is the scalar, and direction is in degrees 
    """
    rad = mpmath.radians(direction)
    
    return (magnitude * sp.cos(rad), magnitude * sp.sin(rad))


def get_magnitude_of_vector(vector: tuple):
    try:
        a = sp.Float(vector[0])
        b = sp.Float(vector[1])
    except Exception as e:
        msg = f"[INFO] - Cannot convert v1: {vector[0]}, v2: {vector[1]} into float. Error: {e}"
        print(msg)
        
        a, b = vector[0], vector[1]
        
    return sp.sqrt(a**2 + b**2)


def add_two_vector(v1: tuple, v2: tuple) -> tuple:
    return (v1[0] + v2[0], v1[1] + v2[1])