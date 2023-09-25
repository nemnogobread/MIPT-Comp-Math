import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la

def get_diff(u, l, m, h):
    n = u.size
    v = np.linspace(-l,m, n)
    # формируем матрицу системы в нужном виде
    A = np.fliplr(np.vander(v, v.size)).T 
    b = np.zeros(n)
    b[1] = 1
    alpha = la.solve(A,b)
    diff = 1/h*alpha.dot(u.T)
    return diff

if __name__ == "__main__":
    p_list = []
    diff_list = []
    error_list = []
    for i in range(1, 7):
        p_list.append(2**i)

    a = np.pi/3
    b = np.pi/2
    
    for i in range(0, len(p_list)):
        p = p_list[i]
        x = np.linspace(a, b, p+1)
        u = np.sin(x)
        h = (b-a)/p
        diff = get_diff(u, 0, p, h)
        diff_list.append(diff)
        error_list.append(abs(diff - 0.5))

    plt.xscale("log")
    plt.plot(p_list, error_list)
    plt.show()

