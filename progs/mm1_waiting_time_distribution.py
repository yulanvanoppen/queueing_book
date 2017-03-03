import numpy as np
from scipy.stats import bernoulli
import matplotlib.pyplot as plt
from matplotlib2tikz import save as tikz_save

from matplotlib import style
style.use('ggplot')

mu = 1.2 # per minute
t  = np.linspace(0, 10)

fig = plt.figure()
for labda in np.linspace(0.5, 1., 8):
   rho = labda/mu
   Ws = rho/(1.-rho)/labda
   res = 1 - rho + rho*(1.-np.exp(-1./Ws*t))
   plt.plot(t, res, label="$\lambda$=%3.2f"%labda)
plt.xlabel('$t$')
plt.ylabel('$\P{W_Q\leq t}$')
plt.title('Waiting time as function of arrival rate')
plt.grid(True)
plt.legend(loc=5, bbox_to_anchor=(15, -2))
tikz_save('mm1_waiting_time.tex', figureheight='6cm', figurewidth='12cm')

