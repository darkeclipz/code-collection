import math

def gcd(a,b):
    a = abs(a)
    b = abs(b)
    if a == b: return a
    if b > a:
        swap = a
        a = b
        b = swap
    q = a // b
    r = a - b * q
    while r != 0:
        a = b
        b = r
        q = a // b
        r = a - b * q
    return b