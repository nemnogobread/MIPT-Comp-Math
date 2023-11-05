import numpy as np
import numpy.linalg as la
import copy 

def get_max_index(A, k, n):
    max = 0
    max_i = k
    for i in range (k, n):
        if abs(A[i, k]) >= abs(max):
            max = A[i, k]
            max_i = i
    return max_i


def gauss_upgraded( A_in, b_in ):
    n = b_in.size
    A = copy.deepcopy(A_in)
    b = copy.deepcopy(b_in)
    for k in range(0,n-1):
        k_max = get_max_index(A, k, n)
        if k_max != k:
            A[[k, k_max]] = A[[k_max, k]]
            b[[k, k_max]] = b[[k_max, k]]
        for i in range(k+1,n):
            if A[i,k]!=0:
                c = A[i,k]/A[k,k]
                A[i,k+1:n] = A[i,k+1:n] - c*A[k,k+1:n]
                b[i] = b[i] - c*b[k]
                
    # обратный ход
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(A[k,k+1:n],b[k+1:n]))/A[k,k]
    return b

A1 = np.array([[1e-16, 1., -1.], [-1., 2., -1.], [2., -1., 0.]])
b1 = np.array([0., 0., 1.])

A2 = np.array([[2., -1., 0.], [-1., 2., -1.], [1e-16, 1., -1.]])
b2 = np.array([1., 0., 0.])

print('mu1 = ', la.cond(A1))
print('mu2 = ', la.cond(A2))

print('u1 = ', gauss_upgraded(A1, b1))
print('u2 = ', gauss_upgraded(A2, b2))
