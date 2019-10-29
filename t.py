import numpy as np


def t_ciz():
    t_harf = np.zeros((20, 20))

    i = 0
    for j in range(20):
        t_harf[i][j] = '1'
        j = j + 1

    j = 9
    for i in range(0, 10):
        t_harf[i][j] = '1'
        i = i + 1

    return t_harf
