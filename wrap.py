def wrap(xs, n): return xs[n%len(xs):] + xs[:n%len(xs)]
def split(xs, n): return xs[:n], xs[n:]
def reverse(xs): return xs[::-1]