from collections import Counter
from matplotlib.pylab import plt
from matplotlib2tikz import save as tikz_save
from matplotlib import style
style.use('ggplot')

from lea import Lea

W0 = 5  # Lea.fromVals(0, 1, 2)
S = Lea.fromVals(1,  2, 3)
X = Lea.fromVals(1,  2, 4)
U = S - X

def simulate():
    count = Counter()
    N = 1000
    W = max(W0 + U.random(), 0)
    for k in range(1, N + 1):
        W = max(W + U.random(), 0)
        count[W] += 1
        if k % (N // 5) == 0: # make 5 plots
            x = [w for w in count]
            tot = sum(count.values())
            y = [count[w] / tot for w in count]
            plt.plot(x, y, label="N={}".format(k))
    return x, y


def exact():
    W = Lea.fastMax(W0 + U, 0)
    for k in range(1, 21):
        if k % 5 == 0:
            plt.plot(W.support(), W.pmf(), label="k={}".format(k))
        W = Lea.fastMax(W + U, 0)
    return W.support(), W.pmf()


plt.figure() 
plt.axis([0, 20, 0, 0.3])
plt.title("Exact")
xex, yex = exact()
plt.legend()
tikz_save('waiting_time_1.tex', figureheight='5cm', figurewidth='5cm')
plt.close() 

plt.figure() 
plt.axis([0, 20, 0, 0.3])
plt.title("Simulation")
xsim, ysim = simulate()
plt.legend()
tikz_save('waiting_time_2.tex', figureheight='5cm', figurewidth='5cm')
plt.close() 

plt.figure() 
plt.axis([0, 20, 0, 0.3])
plt.title("Sim/Exact")
plt.plot(xsim, ysim, label="sim")
plt.plot(xex, yex, label="ex")
plt.legend()
tikz_save('waiting_time_3.tex', figureheight='5cm', figurewidth='5cm')
plt.close()

