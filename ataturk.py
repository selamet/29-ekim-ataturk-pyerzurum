import numpy as np
import time
from a import a
from r import r
from t import t_ciz as t
from u import u
from k import k

a = a()
r = r()
t = t()
u = u()
k = k()

iki_br = np.zeros((20, 3))
ataturk = np.column_stack((a, t, a, t, u, iki_br, r, k))

for i in range(20):
    for j in range(142):
        if ataturk[i][j] == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print('')
    time.sleep(.100)
