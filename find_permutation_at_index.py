# S is the set of permutations, e.x: ['A', 'B', 'C']
# index is Sx in the set of permutations.
# example:    find_permutations_at_index(['A', 'B', 'C'], 0) = [A, B, C]
def find_permutation_at_index(S, index):
    factorial = [1,1]
    for i in range(2, len(S)):
        factorial.append(i*factorial[i-1])
    R = []
    remainder = index
    while remainder > 0:
        n = len(S)-1
        index = remainder // factorial[n]
        remainder -= index * factorial[n]
        R.append(S[index])
        del S[index]
    return R + S