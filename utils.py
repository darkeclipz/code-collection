import functools

# Create a function composition of multiple functions.
def compose2(f, g): return lambda x: f(g(x))
def compose3(f, g, h): return lambda x: f(g(h(x)))
def compose(*fs):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), fs, lambda x: x)

# Rotate the list values n steps to the left with wrapping.
def wrap(xs, n): return xs[n%len(xs):] + xs[:n%len(xs)]

# Split a list into two pieces at index n.
def split(xs, n): return xs[:n], xs[n:]

# Reverse a list.
def reverse(xs): return xs[::-1]

# Swap two variables.
def swap(a, b): return b, a

def between(x, a, b): return b > x > a