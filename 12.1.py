import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize_scalar

def f(p):
    if (p < 0.96):
        return (8 * np.exp(-(p/4.0)) + 6 * np.exp(-(p/2.0))-10) + p*(14 - 8 * np.exp(-(p/4.0)) - 6 * np.exp(-(p/2.0)))

    elif (p>=0.96 and p<1.27):
        return p*(14 - 8 * np.exp(-(p/4.0)) - 6 * np.exp(-(p/2.0)))

    elif (p>=1.27): 
        return (9 - 8 * np.exp(-(p/4.0)) - 6 * np.exp(-(p/2.0))) + p*(14 - 8 * np.exp(-(p/4.0)) - 6 * np.exp(-(p/2.0)))


# d1 = 9 : 1.27
# d1 = 10: 0.96

vfun = np.vectorize(f)


def plot(func):
    res = minimize_scalar(func)
    print(res.x)
    print(res.fun)

    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

    p = np.linspace(0, 4, 100)

    plt.plot(p, func(p), color='red')
    plt.plot([res.x], [res.fun], marker="o", markersize=5, 
        markeredgecolor="black", markerfacecolor="black", 
        label=("Min cost: p=" + str(float("{:.4f}".format(res.x))) + ", W=" + str(float("{:.4f}".format(res.fun)))) )

    plt.legend(loc="upper left")
    plt.show()

    
if __name__ == '__main__':

    plot(vfun)
