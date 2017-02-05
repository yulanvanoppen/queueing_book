import numpy as np
from scipy.stats import bernoulli
import matplotlib.pyplot as plt
from matplotlib2tikz import save as tikz_save
#  import seaborn as sns


from matplotlib import style
style.use('ggplot')


np.random.seed(3)

# make a random walk with steps up and down.
# a is an array of bernoulli random variables
# z is the random walk, i.e., z[i] = sum_{j=1}^i a[i]
# zmin is the running minimum, i.e, \min{z(j), 0 \leq j \leq i}
# q is is random walk reflected in the origin, i.e,
# q[i] = z[i] - \min{z(j), 0 \leq j \leq i}

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
plt.title('Regulated Random Walk')
plt.grid(True)
plt.legend(loc='lower left')

tikz_save('reflected_random_walk.tex', figureheight='5cm', figurewidth='12cm')

# now we have an arrival process such that a[i] = 1 if there is an
# arrival in period i, and a[i]=0 otherwise. The service process is
# similar s[i] = 1 if there is a capacity for a service, and otherwise

n = 30
a = bernoulli(0.3).rvs(n)
a[0] = 0
s = bernoulli(0.4).rvs(n)
z = a.cumsum() - s.cumsum()  # z is the random walk
zmin = np.minimum.accumulate(z)
q = z - zmin  # reflection

fig = plt.figure()
plt.xlabel('Time')
plt.grid(True)
plt.legend(loc='lower left')

plt.subplot(2, 1, 1)
plt.title('Regulated Bernoulli Walk')
plt.plot(a, '2', markersize=4, label="A")
plt.plot(-s, '1', markersize=4, label="S")
plt.plot(z, 'o-', markersize=2, label="Z")
plt.ylim(ymax=2)
plt.ylabel('Arrivals/services')
plt.legend(loc='lower left')

plt.subplot(2, 1, 2)
plt.plot(z, 'o-', markersize=2, label="Z")
plt.plot(q, 'o-', markersize=4, label='Q')
plt.ylabel('Queue')
plt.legend(loc='lower left')

tikz_save('reflected_bernoulli_walk.tex', figureheight='5cm',
          figurewidth='12cm')

