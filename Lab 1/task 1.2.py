import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la

def get_cond(u, l, m, h):
    n = u.size
    v = np.linspace(-l,m, n)
    # формируем матрицу системы в нужном виде
    A = np.fliplr(np.vander(v, v.size)).T 
    cond = la.cond(A)
    return cond

if __name__ == "__main__":
    p_list = [2**i for i in range(1, 7)]
    cond_list = []

    a = np.pi/3     # левая граница
    b = np.pi/2     # правая граница
    
    for i in range(0, len(p_list)):
        p = p_list[i]
        x = np.linspace(a, b, p+1)      # наложение сетки
        u = np.sin(x)       # значения синуса в точках сетки
        h = (b-a)/p     # шаг сетки
        cond = get_cond(u, 0, p, h)     # считаем дифференциал в точке a
        cond_list.append(cond)

    #print(p_list)
    #print(cond_list)

    plt.xscale("log")
    plt.yscale("log")
    plt.plot(p_list, cond_list)
    plt.show()
