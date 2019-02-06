import numpy as np
import matplotlib.pyplot as plt
from matplotlib2tikz import save as tikz_save
#  import seaborn as sns


from matplotlib import style
style.use('ggplot')


np.random.seed(3)


def superposition(a):
    A = np.cumsum(a, axis=1)
    A = np.sort(A.flatten())
    a = A[1:] - A[:-1]
    return a


x = np.arange(0, 8, 0.1)


def makePlot(A, N, bins=50):
    plt.axis([0, 8, 0, 2])

    X = superposition(A)
    yy, xx = np.histogram(X, bins=bins, density=True)
    #print(yy)
    #print(xx)
    #print(np.dot(yy,xx[1:]-xx[:-1]))
    #print(yy.sum())
    xx = (xx[1:] + xx[:-1])/2
    #d = xx[1]-xx[0]
    #print(9/100/d)
    #print(len(xx), len(yy))
    #quit()
    labda = N / A.mean()
    #plt.hist(X, 20, normed=1, label='simulation')
    plt.plot(xx, yy, "o",  markersize=1, color='black', label='simulation')
    plt.plot(x, labda * np.exp(-labda * x), label="theory", color='black')
    plt.title("$N={}, n={}, b={}$".format(N, n, bins))
    plt.legend()


n = 100  # simulation run length

fig = plt.figure(figsize=(6, 2))
#plt.subplot(311)
plt.subplot(131)
N = 1
A = np.random.uniform(4, 6, (N, n))
makePlot(A, N, bins=10)


#plt.subplot(312)
plt.subplot(132)
N = 3
A = np.random.uniform(4, 6, (N, n))
makePlot(A, N, bins=10)


#plt.subplot(313)
plt.subplot(133)
N = 10
A = np.random.uniform(4, 6, (N, n))
makePlot(A, N, bins=10)

#fig.suptitle('PLOT TITLE', fontsize=18, fontweight='bold')

tikz_save('uniform_to_exponential_few.tex', figureheight='5cm', figurewidth='5cm')
plt.close()

n = 1e3  # simulation run length

fig = plt.figure(figsize=(6, 2))
#plt.subplot(311)
plt.subplot(131)
N = 1
A = np.random.uniform(4, 6, (N, n))
makePlot(A, N)


#plt.subplot(312)
plt.subplot(132)
N = 3
A = np.random.uniform(4, 6, (N, n))
makePlot(A, N)


#plt.subplot(313)
plt.subplot(133)
N = 10
A = np.random.uniform(4, 6, (N, n))
makePlot(A, N)

#fig.suptitle('PLOT TITLE', fontsize=18, fontweight='bold')

tikz_save('uniform_to_exponential_many.tex', figureheight='5cm', figurewidth='5cm')
plt.close()


# normal distribution

fig = plt.figure(figsize=(6, 2))
#plt.subplot(311)
plt.subplot(131)
N = 1
A = np.random.normal(5, 1, (N, n))
makePlot(A, N)


#plt.subplot(312)
plt.subplot(132)
N = 3
A = np.random.normal(5, 1, (N, n))
makePlot(A, N)


#plt.subplot(313)
plt.subplot(133)
N = 10
A = np.random.normal(5, 1, (N, n))
makePlot(A, N)

#fig.suptitle('PLOT TITLE', fontsize=18, fontweight='bold')

tikz_save('normal_to_exponential.tex', figureheight='5cm', figurewidth='5cm')
plt.close()


