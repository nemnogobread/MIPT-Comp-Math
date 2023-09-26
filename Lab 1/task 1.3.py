import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la


def central_difference(a, h):
    diff = (np.sin(a+h) - np.sin(a-h))/(2*h)
    return diff

def directional_difference(a, h):
    diff = (np.sin(a+h) - np.sin(a))/h
    return diff

def get_p(a, h):
    diff_d1 = directional_difference(a, h)
    diff_d2 = directional_difference(a, h/2)
    err_d1 = diff_d1 - 0.5
    err_d2 = diff_d2 - 0.5
    p_directional = np.log2(err_d1/err_d2)

    diff_c1 = central_difference(a, h)
    diff_c2 = central_difference(a, h/2)
    err_c1 = diff_c1 - 0.5
    err_c2 = diff_c2 - 0.5
    p_central = np.log2(err_c1/err_c2)

    return p_directional, p_central


if __name__ == "__main__":
    h_list = [2**(-i) for i in range(1, 10)]
    p_list_directional = []
    p_list_central = []

    a = np.pi/3     # левая граница
    
    for i in range(0, len(h_list)):
        h = h_list[i]
        p_directional, p_central = get_p(a, h)
        p_list_directional.append(p_directional)
        p_list_central.append(p_central)
        
    #print(h_list)
    #print(p_list_directional)
    #print(p_list_central)

    plt.xscale("log")
    plt.plot(p_list, cond_list)
    plt.show()
