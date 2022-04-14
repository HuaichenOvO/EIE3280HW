import numpy as np
import numpy.linalg as la

if __name__ == '__main__':
    # m = (np.exp(-0.075))
    # n = (np.exp(-0.15))

    # W_mat = np.matrix([
    #     [1,1],
    #     [m,n]
    # ])

    # v_mat = np.matrix([
    #     [17],
    #     [15.2]
    # ])

    # print(la.inv(W_mat) * v_mat)

    top = 1.8-17*(1 - np.exp(-0.3/2))
    bot = np.exp(-0.3/2) - np.exp(-0.3/4)

    print(top/bot)