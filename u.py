import numpy as np

np.set_printoptions(linewidth=3000)


def u():
    str = ""
    for i in range(20):
        for j in range(20):
            if ((j == 0 + 2 or j == 18 or j == 20) and (i >= 0 and i < 10 and i != 2)) or (
                    (j > 1 and j < 18) and i == 9):
                str = str + "1"

            else:
                str = str + "0"

    b = list(str)
    a = list(map(int, b))
    a = np.array(a)

    a = np.resize(a, (20, 20))
    return a


u()
