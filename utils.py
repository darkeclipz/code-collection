# Rotate the list values n steps with wrapping.
def wrap(xs, n): return xs[n%len(xs):] + xs[:n%len(xs)]

# Split a list into two pieces at index n.
def split(xs, n): return xs[:n], xs[n:]

# Reverse a list.
def reverse(xs): return xs[::-1]

# Swap two variables.
def swap(a, b): return b, a

# Count occurences of a sub string in a string.
def count_substring(string, sub_string):
    haystack = list(string)
    needle = list(sub_string)
    N = len(string)
    occurences = 0
    for i in range(N-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            occurences += 1
    return occurences

# Change a character in a string at a position.
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]