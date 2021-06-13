"""
Zbiór funkcji liczących pola kilku figur geometrycznych.

"""

import math

def pole_prostokata (a, b):
    return a * b

def pole_kwadratu (a):
    return a ** 2

def pole_trojkata (a, h):
    return 0.5 * a * h

def pole_trapezu (a, b, h):
    return ((a + b) * h) * 0.5

def pole_kola (r):
    return math.pi * (r ** 2)
