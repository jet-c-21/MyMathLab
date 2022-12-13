# coding: utf-8
"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 2022/12/5
"""
from pprint import pp

k = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

k2 = [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3],
]


def get_k2(x):
    res = []
    for i in x:
        res.append([0 for _ in range(len(i))])

    for i in range(len(res)):
        for j in range(len(res[i])):
            res[j][len(res[i]) - 1 - i] = x[i][j]

    return res


get_k2(k)
