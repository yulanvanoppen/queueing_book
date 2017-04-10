from functools import lru_cache
import numpy as np

mu = np.array([3, 4])
V = np.array([1, 1])
c = np.array([1, 1]) # single server stations


M=len(mu)
N = 2 # num jobs

@lru_cache(maxsize=None)
def f(i, n_i):
    if n_i == 0:
        return 1
    return V[i] / mu[i] / min(n_i, c[i]) * f(i, n_i - 1)

@lru_cache(maxsize=None) 
def G(m, n):
    if n == 0:
        return 1
    if m == 0:
        return 1 / mu[0]**n
    return sum(f(m, k) * G(m - 1, n - k) for k in range(n + 1))

for m in range(M):
    for n in range(N+1):
        print("G({}, {}) = {}".format(m, n, G(m, n)))

def test():
    print("G(1,2) = ", 1/9 + 1/12 + 1/16)

test()
