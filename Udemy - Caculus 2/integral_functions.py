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
    ig_args = (x, interval[0], interval[1])

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
