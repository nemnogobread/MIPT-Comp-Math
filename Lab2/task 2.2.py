import numpy as np
import numpy.linalg as la
import copy 

def A_to_LU(a):
    n = a.shape[0]
    LU_matrix = np.matrix(np.zeros([n, n]))

    for k in range(n):

        for j in range(k, n):
            LU_matrix[k, j] = a[k, j] - LU_matrix[k, :k] * LU_matrix[:k, j]

        for i in range(k + 1, n):
            LU_matrix[i, k] = (a[i, k] - LU_matrix[i, :k] * LU_matrix[:k, k]) / LU_matrix[k, k]

    return LU_matrix

def LU_to_L(LU_matrix):
    L = LU_matrix.copy()
    for i in range(L.shape[0]):
            L[i, i] = 1
            L[i, i+1:] = 0
    return L

def LU_to_U(LU_matrix):
    U = LU_matrix.copy()
    for i in range(1, U.shape[0]):
            U[i, :i] = 0
    return U

def gauss( A_in, b_in ):
    n = b_in.size
    A = copy.deepcopy(A_in)
    b = copy.deepcopy(b_in)
    for k in range(0,n-1):
        for i in range(k+1,n):
            if A[i,k]!=0:
                c = A[i,k]/A[k,k]
                A[i,k+1:n] = A[i,k+1:n] - c*A[k,k+1:n]
                b[i] = b[i] - c*b[k]
                
    # обратный ход
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(A[k,k+1:n],b[k+1:n]))/A[k,k]
    return b


if __name__ == "__main__":
    A = np.array([[2., -1., 0.], [-1., 2., -1.], [0, 1., -1.]])
    b = np.array([1., 0., 0.])

    LU_matrix = A_to_LU(A)

    L = LU_to_L(LU_matrix)
    U = LU_to_U(LU_matrix)
    print(L, "\n")
    print(U, "\n")

    v = gauss(L, b)
    u = gauss(U, v)
    print ("u = ", u)
