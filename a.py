import numpy as np

def a():
    a = np.zeros((20,20))

    j=10
    for i in range(0,10):
            a[i][j]='1'
            j=j-1
    j=11

    for i in range(1,19):
        if j<20:
            a[i][j]='1'
            j=j+1
    i=5
    for j in range(5,20):
        if j<15:
            a[i][j]='1'
            j=j+1


    for i in range(0,19):
        for j in range(20):
            if a[i][j]==1:
                print('*',end='')
            else:
                print(' ',end='')
        print('')

a()
