# Rotate the list values n steps with wrapping.
def wrap(xs, n): return xs[n%len(xs):] + xs[:n%len(xs)]

# Split a list into two pieces at index n.
def split(xs, n): return xs[:n], xs[n:]

# Reverse a list.
def reverse(xs): return xs[::-1]