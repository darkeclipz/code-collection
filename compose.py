from math import sqrt, log
import functools

def compose(*fs):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), fs, lambda x: x)

is_fib = lambda x: any([sqrt(d).is_integer() for d in [5*x**2+4, 5*x**2-4]])

seq = '1 2 3 4 5 6 7 8 9 10 11 12 13 14'
sum(map(compose(int, is_fib, int), seq.split(' ')))