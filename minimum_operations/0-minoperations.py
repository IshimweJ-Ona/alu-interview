#!/usr/bin/python3
"""Claculate the minimum number of operations
to reach n H characters.
Opreatiosn allowed: copy  all, paste.
"""


def minOpreations(n):
    if n < 2:
        return 0
    
    ops = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            ops += factor
            n //= factor
        factor += 1

    return ops
