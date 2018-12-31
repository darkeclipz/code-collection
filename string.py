def print_dec_oct_hex_bin(n):
    width = len("{0:b}".format(n))
    for i in range(1, n+1):
        print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))

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

# Swap lower case to upper case, and upper case to lower case.
def swap_case(s):
    swap = lambda c: chr(c^32) if 123 > c > 96 or 91 > c > 64 else chr(c)
    return ''.join(map(swap, map(ord, s)))