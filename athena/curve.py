import sympy


def is_closed_curve(c: sympy.Curve) -> bool:
    st = c.subs(c.parameter, c.limits[1])
    ed = c.subs(c.parameter, c.limits[2])

    return st == ed
