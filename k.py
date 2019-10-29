import numpy as np


def k():
    dizi = np.zeros((20, 20))

    for i in range(0, 10):
        dizi[i][0] = 1

    j = 0
    for i in range(5, -1, -1):
        dizi[i][j] = 1
        j += 2
    j = 0
    for i in range(4, 10):
        dizi[i][j] = 1
        j += 2

    for i in range(20):
        for j in range(20):
            if dizi[i][j] == 1:
                print('*', end='')
            else:
                print(' ', end='')
        print('')
    return dizi

