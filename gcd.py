import math

# Find the greatest common divisor for a, b. (Euclidean algorithm)
# src: https://wstein.org/ent/ent.pdf
def gcd(a,b):
    a = abs(a)
    b = abs(b)
    if a == b: return a
    if b > a:
        a, b = b, a
    q = a // b
    r = a - b * q
    while r != 0:
        a = b
        b = r
        q = a // b
        r = a - b * q
    return b