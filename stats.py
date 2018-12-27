import math
import numpy as np
import scipy.stats

def mean(xs): return np.mean(xs)
def wmean(xs, ws): return sum([ws[i] * xs[i] for i in range(len(xs))]) / sum(ws)

def sd(xs): 
    m = mean(xs)
    var = sum([(x-m)**2 for x in xs]) / len(xs)
    return math.sqrt(var)

def mode(xs): return scipy.stats.mode(xs)

def median(xs):
    n = len(xs)
    if n % 2 == 0: return (xs[n//2] + xs[n//2-1]) // 2
    else: return xs[n//2]

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

def iqr(xs):
    Q1, Q2, Q3 = quartiles(xs)
    return Q3-Q1

def ncr(n,x): return math.factorial(n) / (math.factorial(x) * math.factorial(n - x))
def binom(x,n,p): return ncr(n, x) * p**x * (1-p)**(n-x)
def geom(n,p): return (1-p)**(n-1)*p    

# E(x) = lambda
# Var(x) = lambda
# E(x^2) = lambda + lambda^2
def poisson(k, lamda): return lamda ** k * math.exp(-lamda) / math.factorial(k)

def normal(x, mu, sigma): return 1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-((x-mu)**2)/(2*sigma**2))
def normal_cdf(x, mu, sigma): return 1/2 * (1 + math.erf((x - mu)/(sigma * math.sqrt(2))))

def percentage(x): return x * 100