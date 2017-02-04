import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context("paper")


np.random.seed(3)

labda = 20
mu = 21

a = np.random.poisson(labda, 10)
print(a)

c = mu * np.ones_like(a)
print(c)

Q = np.zeros_like(a)
d = np.zeros_like(a)
Q[0] = 10  # initial queue length

for k in range(1, len(a)):
    d[k] = min(Q[k - 1], c[k])
    Q[k] = Q[k - 1] - d[k] + a[k]

print(d)
print(Q)
loss = (Q > 20)
print(loss)

print(d.mean(), Q.mean(), Q.std(), (Q > 20).mean())

num = 100
a = np.random.poisson(labda, num)
c = mu * np.ones_like(a)
Q = np.zeros_like(a)
d = np.zeros_like(a)
Q[0] = 10  # initial queue length

for k in range(1, len(a)):
    d[k] = min(Q[k - 1], c[k])
    Q[k] = Q[k - 1] - d[k] + a[k]

print(d.mean(), Q.mean(), Q.std(), (Q > 20).mean() * 100)

# plt.plot(Q)
# plt.show()


c = np.random.poisson(mu, num)
Q = np.zeros_like(a)
d = np.zeros_like(a)
Q[0] = 10  # initial queue length

for k in range(1, len(a)):
    d[k] = min(Q[k - 1], c[k])
    Q[k] = Q[k - 1] - d[k] + a[k]

print(d.mean(), Q.mean(), Q.std(), (Q > 20).sum())

# plt.plot(Q)
# plt.show()
