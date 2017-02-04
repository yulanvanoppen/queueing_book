import numpy as np
from scipy.stats import bernoulli
import matplotlib.pyplot as plt
from matplotlib2tikz import save as tikz_save
#  import seaborn as sns


from matplotlib import style
style.use('ggplot')


np.random.seed(3)

n = 30
a = 2*bernoulli(0.49).rvs(n)-1
a[0] = 0
z = a.cumsum()
zmin = np.minimum.accumulate(z)
q = z-zmin

fig = plt.figure()
plt.plot(z, 'o-', markersize=2, label="Z")
plt.plot(q, 'o-', markersize=4, label='Q')

plt.xlabel('Time')
plt.ylabel('Queue')
plt.title('Reflected Random Walk')
plt.grid(True)
plt.legend(loc='lower left')

tikz_save('reflected_random_walk.tex', figureheight='5cm', figurewidth='12cm')

n = 30
a = bernoulli(0.3).rvs(n)
a[0] = 0
s = bernoulli(0.4).rvs(n)
z = a.cumsum() - s.cumsum()
zmin = np.minimum.accumulate(z)
q = z-zmin

fig = plt.figure()
plt.xlabel('Time')
plt.grid(True)
plt.legend(loc='lower left')

plt.subplot(2, 1, 1)
plt.title('Reflected Bernoulli Walk')
plt.plot(a, '2', markersize=4, label="A")
plt.plot(-s, '1', markersize=4, label="S")
plt.plot(z, 'o-', markersize=2, label="Z")
plt.ylabel('Arrivals/services')

plt.subplot(2, 1, 2)
plt.plot(z, 'o-', markersize=2, label="Z")
plt.plot(q, 'o-', markersize=4, label='Q')
plt.ylabel('Queue')

tikz_save('reflected_bernoulli_walk.tex', figureheight='5cm',
          figurewidth='12cm')

