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
    p_list = [2**i for i in range(1, 7)]
    diff_list = []
    error_list = []

    a = np.pi/3     # левая граница
    b = np.pi/2     # правая граница
    
    for i in range(0, len(p_list)):
        p = p_list[i]
        x = np.linspace(a, b, p+1)      # наложение сетки
        u = np.sin(x)       # значения синуса в точках сетки
        h = (b-a)/p     # шаг сетки
        diff = get_diff(u, 0, p, h)     # считаем дифференциал в точке a
        diff_list.append(diff)
        error_list.append(abs(diff - 0.5))      # считаем ошибку как разность (sin(pi/3) = 0.5) 

    #print(p_list)
    #print(diff_list)

    plt.xscale("log")
    plt.plot(p_list, error_list)
    plt.show()
