import numpy as np


def sommamatrici(a, b):
    c = np.zeros(a.shape)
    for i in range(c.shape[0]):
        for j in range(c.shape[0]):
            c[i][j] = a[i][j]+b[i][j]
    return c


def moltiplicazionematrici(a,b):
    c = np.zeros((a.shape[0], b.shape[1]))
    for i in range(len(c)):
        for j in range(len(c[i])):
            for k in range(len(a[i])):
                c[i][j] += a[i][k]*b[k][j]
    return c


def fatt(n):
    if n>1:
        return fatt(n-1)*n
    else:
        return 1


def fatit(n):
    ft = 1
    for i in range(1,n+1):
        ft *=i
    return ft


m1 = np.array([[0, 1], [2, 3]])
m2 = np.array([[0, 2, 3], [1, 4, 5]])
m3 = sommamatrici(m1,m2)
print(m3)
m3 = moltiplicazionematrici(m1,m2)
print(m3)

print("fatt(6)=" + str(fatt(6)))
print("fatt(6)=" + str(fatit(6)))