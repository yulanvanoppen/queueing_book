import numpy as np
from numpy.random import exponential
import matplotlib.pylab as plt

np.random.seed(3)

N = 1000
labda, mu = 2.6, 3

A = np.zeros(N)
D = np.zeros_like(A)
W = np.zeros_like(A)

for k in range(1, N):
    Xk = exponential(1. / labda)
    Sk = exponential(1. / mu)
    A[k] = A[k - 1] + Xk
    D[k] = max(A[k], D[k - 1]) + Sk
    W[k] = D[k] - A[k]

print(W.mean())
print(np.percentile(W, 80))
print(np.percentile(W, 90))
print(np.percentile(W, 95))
