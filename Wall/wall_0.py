# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-chien
Create Date: 2022/3/6
"""
import sympy as sp


def get_area_btw_curves_up_down(eq1: sp.Equality, eq2: sp.Equality):
    ans = sp.solve([eq1, eq2], (x, y))

    integrand_1 = eq1.rhs
    integrand_2 = eq2.rhs

    f = sp.Integer(0)
    for i in range(len(ans) - 1):
        interval = [ans[i][0], ans[i + 1][0]]
        itg_args = (x, interval[0], interval[1])

        itgd_1_area = integrand_1.integrate(itg_args)
        itgd_2_area = integrand_2.integrate(itg_args)

        if itgd_1_area > itgd_2_area:
            higher_itgd = integrand_1
            lower_itgd = integrand_2
        else:
            higher_itgd = integrand_2
            lower_itgd = integrand_1

        new_term = sp.Integral(higher_itgd, itg_args) - sp.Integral(lower_itgd, itg_args)
        f += new_term

    return f


def get_area_btw_curves_left_ritght(eq1: sp.Equality, eq2: sp.Equality):
    ans = sp.solve([eq1, eq2], (x, y))
    # print(ans)

    integrand_1 = eq1.rhs
    integrand_2 = eq2.rhs

    f = sp.Integer(0)
    for i in range(len(ans) - 1):
        interval = [ans[i][1], ans[i + 1][1]]
        itg_args = (y, interval[0], interval[1])

        itgd_1_area = integrand_1.integrate(itg_args)
        itgd_2_area = integrand_2.integrate(itg_args)

        if itgd_1_area > itgd_2_area:
            higher_itgd = integrand_1
            lower_itgd = integrand_2
        else:
            higher_itgd = integrand_2
            lower_itgd = integrand_1

        new_term = sp.Integral(higher_itgd, itg_args) - sp.Integral(lower_itgd, itg_args)
        f += new_term

    return f


def get_area_btw_curves(eq1: sp.Equality, eq2: sp.Equality, wrt='x'):
    if wrt == 'x':
        return get_area_btw_curves_up_down(eq1, eq2)
    else:
        return get_area_btw_curves_left_ritght(eq1, eq2)


def get_area_btw_curves_with_intv(eq1: sp.Equality, eq2: sp.Equality, interval):
    integrand_1 = eq1.rhs
    integrand_2 = eq2.rhs
    itg_args = (x, interval[0], interval[1])

    itgd_1_area = integrand_1.integrate(itg_args)
    itgd_2_area = integrand_2.integrate(itg_args)

    if itgd_1_area > itgd_2_area:
        higher_itgd = integrand_1
        lower_itgd = integrand_2
    else:
        higher_itgd = integrand_2
        lower_itgd = integrand_1

    return sp.Integral(higher_itgd, itg_args) - sp.Integral(lower_itgd, itg_args)


if __name__ == '__main__':
    x, y = sp.symbols('x y')
    eq1 = sp.Eq(x, 3 * y ** 2)
    eq2 = sp.Eq(x, y ** 2 + 2)
    af = get_area_btw_curves(eq1, eq2, 'y')
    print(af.doit())

    # print(f1.free_symbols)

    # print(type(f1))
