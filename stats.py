import math
import numpy as np
import scipy.stats

# Calculate the mean for a list of values.
def mean(xs): return sum(xs) / len(xs)

# Calculate a weighted mean for a list of values.
# ws : weights (list)
def wmean(xs, ws): return sum([ws[i] * xs[i] for i in range(len(xs))]) / sum(ws)

# Calculate the standard deviation for a list of values.
def sd(xs): 
    m = mean(xs)
    var = sum([(x-m)**2 for x in xs]) / len(xs)
    return math.sqrt(var)

# Find the mode for a list of values.
def mode(xs): return scipy.stats.mode(xs)

# Find the median for a list of values.
def median(xs):
    n = len(xs)
    if n % 2 == 0: return (xs[n//2] + xs[n//2-1]) // 2
    else: return xs[n//2]

# Find the first, second, and third quartiles.
def quartiles(xs):
    n = len(xs)
    even = n % 2 == 0
    if even: 
        Q1 = median( xs[:n//2] )
        Q2 = median( xs )
        Q3 = median( xs[n//2:] )
        return Q1, Q2, Q3
    else:
        Q1 = median( xs[:n//2] )
        Q2 = xs[n//2]
        Q3 = median( xs[n//2+1:] )
        return Q1, Q2, Q3

# Find the interquarile range (Q3-Q1)
def iqr(xs):
    Q1, Q2, Q3 = quartiles(xs)
    return Q3-Q1

# Ways to choose x out of n
def ncr(n,x): return math.factorial(n) / (math.factorial(x) * math.factorial(n - x))

# Binomial distribution pdf
def binom(x,n,p): return ncr(n, x) * p**x * (1-p)**(n-x)

# Geometric distribution pdf
def geom(n,p): return (1-p)**(n-1)*p    

# E(x) = lambda
# Var(x) = lambda
# E(x^2) = lambda + lambda^2
# Poisson distribution pdf
def poisson(k, lamda): return lamda ** k * math.exp(-lamda) / math.factorial(k)

# Normal distribution pdf
def normal(x, mu, sigma): return 1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-((x-mu)**2)/(2*sigma**2))

# Normal distribution cdf
def normal_cdf(x, mu, sigma): return 1/2 * (1 + math.erf((x - mu)/(sigma * math.sqrt(2))))

# Convert a float to a percentage, e.g. 1.10 to 10.
def percentage(x): return x * 100

# Find the correlation coefficient for two lists of values.
def pearson_corr(xs, ys):
    if len(xs) is not len(ys):
        raise ValueError('Arrays should have equal dimensions.')
    mx = mean(xs); my = mean(ys)
    sx = sd(xs); sy = sd(ys)
    return sum([(xs[i] - mx) * (ys[i] - my) for i in range(len(xs))]) / (len(xs) * sx * sy)

# Find the spearman coefficient for two lists of values based on ranks.
def spearman_rank_corr(xs, ys):
    if len(xs) is not len(ys):
        raise ValueError('Arrays must have equal dimension.')
    N = len(xs)
    x = sorted(xs); y = sorted(ys)
    rx = {x:n for x,n in zip(x, range(N))}
    ry = {y:n for y,n in zip(y, range(N))}
    ds = [ (rx[xs[i]] - ry[ys[i]])**2 for i in range(N)]
    return 1 - 6*sum(ds) / (N**3 - N)