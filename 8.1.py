import numpy as np
import numpy.linalg as lg

A_mat = np.matrix([
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0]
])

eigen = lg.eig(A_mat) # return Arr[5] with 5 different linear independent eigen values

vec = eigen[1][:, 0] # the column (eigen vector) with the largest eigen value

value = eigen[0][0] # the largest eigen value

print(vec)

print(A_mat * vec)

print(value * vec)
