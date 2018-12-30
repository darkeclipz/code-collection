# These methods are based on Binet's Formula.
from math import sqrt, log

# Test of a number x is a Fibonacci number.
def fib_test(x): return any([sqrt(d).is_integer() for d in [5*x**2+4, 5*x**2-4]])

# Get the Fibonacci number (Fn) at position n.
def fib(n):
    phi = (1+sqrt(5)) / 2
    psi = (1-sqrt(5)) / 2
    return (phi**n - psi**n) // sqrt(5)
        
# Get the position n for a Fibonacci number (Fn).
def invfib(x):
    if not fib_test(x):
        raise ValueError('x must be a Fibonacci number.')
    phi = (1+sqrt(5)) / 2
    rad = 5 * x**2
    f = lambda r: log((x * sqrt(5) + sqrt(r)) / 2, phi)
    if sqrt(5*x**2+4).is_integer(): 
        return round(f(rad + 4))
    return round(f(rad - 4))