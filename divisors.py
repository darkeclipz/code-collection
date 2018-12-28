import math

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

    return set(result)