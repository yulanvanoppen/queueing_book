from math import factorial
import numpy as np
import matplotlib.pylab as plt
from matplotlib2tikz import save as tikz_save

from matplotlib import style
style.use('ggplot')


def G(labda, mu, c):
    rho = labda / mu / c
    res = sum((c * rho)**n / factorial(n) for n in range(c))
    res += (c * rho)**c / ((1 - rho) * factorial(c))
    return res


def ELQ(labda, mu, c):
    rho = labda / mu / c
    g = G(labda, mu, c)
    return (c * rho)**c / (factorial(c) * g) * rho / (1 - rho)**2


def ELS(labda, mu, c):
    rho = labda / mu / c
    return rho * c


def EL(labda, mu, c):
    return ELS(labda, mu, c) + ELQ(labda, mu, c)


mu = 2
c = 3

Q = []
L = []
load = []

for labda in np.linspace(0.1, 5.8, 20):
    Q.append(ELQ(labda, mu, c) / ELQ(labda, c * mu, 1))
    L.append(EL(labda, mu, c) / EL(labda, c * mu, 1))
    load.append(labda / mu / c)

plt.figure(figsize=(6, 2))
plt.subplot(111)
plt.axis([0, 1, 0, 3])
plt.title("$M/M/3$ vs $M/M/1$")
plt.plot(load, L, label="$\E{L(M/M/3)}/\E{L(M/M/1)}$")
plt.plot(load, Q, label="$\E{L_Q(M/M/3)}/\E{L_Q(M/M/1)}$")
plt.xlabel("$\\rho$")
plt.legend()
plt.subplots_adjust(bottom=0.24)
tikz_save('multi_vs_single_server.tex', figureheight='5cm', figurewidth='12cm')
plt.close()

