import numpy as np


def a():
    # 20 ye 20 lik içi 0 larla dolu bir matris oluituruyoruz.
    # dolu olmasını istediğim kısımları 1 yaptım ki ekrana rahat basabileyim.
    a = np.zeros((20, 20))

    # sol dolu kısım
    j = 10
    for i in range(0, 10):
        a[i][j] = '1'
        j = j - 1
    j = 11

    # sağ dolu kısım
    for i in range(1, 19):
        if j < 20:
            a[i][j] = '1'
            j = j + 1
    # orta çizgi
    i = 5
    for j in range(5, 20):
        if j < 15:
            a[i][j] = '1'
            j = j + 1

    return a
