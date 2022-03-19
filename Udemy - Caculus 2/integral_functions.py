# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-chien
Create Date: 2022/3/9
"""
import sympy as sp


def show_integral(itg_f):
    eq = sp.Eq(itg_f, itg_f.doit())
    return eq


def get_area_btw_curves_with_intv(eq1, eq2, interval):
    integrand_1 = eq1.rhs
    integrand_2 = eq2.rhs
    wrt = tuple(integrand_1.free_symbols)[0]
    ig_args = (wrt, interval[0], interval[1])

    igd_1_area = integrand_1.integrate(ig_args)
    igd_2_area = integrand_2.integrate(ig_args)

    if igd_1_area > igd_2_area:
        higher_igd = integrand_1
        lower_igd = integrand_2
    else:
        higher_igd = integrand_2
        lower_igd = integrand_1

    return sp.Integral(higher_igd, ig_args) - sp.Integral(lower_igd, ig_args)


def get_area_btw_curves_up_down(eq1: sp.Equality, eq2: sp.Equality):
    ans = sp.solve([eq1, eq2], (x, y))

    integrand_1 = eq1.rhs
    integrand_2 = eq2.rhs

    f = sp.Integer(0)
    for i in range(len(ans) - 1):
        interval = [ans[i][0], ans[i + 1][0]]
        ig_args = (x, interval[0], interval[1])

        igd_1_area = integrand_1.integrate(ig_args)
        igd_2_area = integrand_2.integrate(ig_args)

        if igd_1_area > igd_2_area:
            higher_igd = integrand_1
            lower_igd = integrand_2
        else:
            higher_igd = integrand_2
            lower_igd = integrand_1

        new_term = sp.Integral(higher_igd, ig_args) - sp.Integral(lower_igd, ig_args)
        f += new_term

    return f


def get_area_btw_curves_left_right(eq1: sp.Equality, eq2: sp.Equality):
    ans = sp.solve([eq1, eq2], (x, y))
    #     print(ans)

    integrand_1 = eq1.rhs
    integrand_2 = eq2.rhs

    f = sp.Integer(0)
    for i in range(len(ans) - 1):
        interval = [ans[i][1], ans[i + 1][1]]
        ig_args = (y, interval[0], interval[1])

        igd_1_area = integrand_1.integrate(ig_args)
        igd_2_area = integrand_2.integrate(ig_args)

        if igd_1_area > igd_2_area:
            higher_igd = integrand_1
            lower_igd = integrand_2
        else:
            higher_igd = integrand_2
            lower_igd = integrand_1

        new_term = sp.Integral(higher_igd, ig_args) - sp.Integral(lower_igd, ig_args)
        f += new_term

    return f


def get_area_btw_curves(eq1: sp.Equality, eq2: sp.Equality, wrt='x'):
    if wrt == 'x':
        return get_area_btw_curves_up_down(eq1, eq2)
    else:
        return get_area_btw_curves_left_right(eq1, eq2)


def get_avg_h_of_itg(itg, itg_args):
    a, b = itg_args[1], itg_args[2]
    itg = itg.integrate(itg_args)
    avg_h = itg / sp.Integer(b - a)

    return avg_h


def get_arc_len_itgd(f):
    f_prime = f.diff()
    return sp.sqrt(1 + f_prime ** 2)

def get_line_by_2p(p1, p2):
    global x, y
    delta_y = p1[1] - p2[1]
    delta_x = p1[0] - p2[0]
    slope = sp.Rational(delta_y, delta_x)

    # y = m * (x - x') + y'
    return sp.(y, slope * (x - p1[0]) + p1[1])


def get_area_btw_two_curves(expr1, expr2, interval):
    wrt = tuple(expr1.free_symbols)[0]
    itg_args = (wrt, interval[0], interval[1])

    # check the mid value in the interval
    check_val = sp.Rational(interval[0] + interval[1], 2)

    if expr1.subs(wrt, check_val) > expr2.subs(wrt, check_val):
        higher_bound = expr1
        lower_bound = expr2
    else:
        higher_bound = expr2
        lower_bound = expr1

    return (higher_bound - lower_bound).integrate(itg_args)


def get_area_btw_two_curves_by_eqs(eq1, eq2, interval):
    return get_area_btw_two_curves(eq1.rhs, eq2.rhs, interval)


def find_triangle_area(p1, p2, p3):
    points = [p1, p2, p3]
    points.sort(key=lambda p: p[0])  # sort by x coord

    intervals = [(points[0][0], points[1][0]), (points[1][0], points[2][0])]

    l1 = get_line_by_2p(points[0], points[1])
    l2 = get_line_by_2p(points[1], points[2])
    l3 = get_line_by_2p(points[0], points[2])

    return get_area_btw_two_curves_by_eqs(l1, l3, intervals[0]) + get_area_btw_two_curves_by_eqs(l2, l3, intervals[1])