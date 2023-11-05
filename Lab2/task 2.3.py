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

def L_solve(L, b):
    n = b.size
    x = b.copy()
    
    for k in range(0,n-1):
        for i in range(k+1,n):
            if L[i,k]!=0:
                c = L[i,k]/L[k,k]
                x[i] = x[i] - c*x[k]
    return x

def U_solve(U, b):
    n = b.size
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(U[k,k+1:n],b[k+1:n]))/U[k,k]
    return b

def get_A_inv(A, n):
    LU_matrix = A_to_LU(A)
    C = A.copy()
    L = LU_to_L(LU_matrix)
    U = LU_to_U(LU_matrix)

    E = np.eye(n)

    L_inv, U_inv = np.zeros((n,n)),np.zeros((n,n))
    for i in range(n):
        L_inv[i] = L_solve(L, E[i])
        U_inv[i] = U_solve(U, E[i])
    L_inv = L_inv.T
    U_inv = U_inv.T
    A_inv = np.dot(U_inv, L_inv)

    return A_inv


if __name__ == "__main__":
    A = np.array([[1., 1., 1.], [0., 1., 2.], [7, 1., 4.]])

    LU_matrix = A_to_LU(A)
    L = LU_to_L(LU_matrix)
    U = LU_to_U(LU_matrix)

    A_inv1 = get_A_inv(A, np.shape(A)[0])
    A_inv2 = la.inv(A)

    print(A_inv1, "\n")
    print(A_inv2)
