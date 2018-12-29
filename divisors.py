import math

# Returns all the divisors for a number x, including x.
# e.g divisors(1001) = [1, 7, 11, 13, 77, 91, 143, 1001]
def divisors(x):
    result = []
    limit = math.ceil(math.sqrt(x))
    for i in range(1, limit+1):
         if x % i == 0:
            if x / i == i:
                result.append(i)
            else:
                result.append(i)
                result.append(x//i)

    return sorted(list(set(result)))