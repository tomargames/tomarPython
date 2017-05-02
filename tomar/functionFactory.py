# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 17:03:05 2016

@author: tomar
"""

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def newFunction(x):
        rtn = 0
        for i in range(len(L)):
            rtn += L[i] * x**(len(L) - i - 1)
        return rtn
    return newFunction


for r in range(11):
    print(r, general_poly([1, 2, 3, 4])(r))
    print(r, general_poly([200, 100])(r))
"""
0 1234
1 4
2 3
3 380
4 189
5 2.6875
6 335.2

def make_cylinder_volume_func(r):
    def volume(h):
        return math.pi * r * r * h
    return volume
"""