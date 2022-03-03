import numpy as np


def sommamatrici(a, b):
    c = np.zeros(a.shape)
    for i in range(c.shape[0]):
        for j in range(c.shape[1]):
            c[i][j] = a[i][j] + b[i][j]
    return c


def moltiplicazionematrici(a, b):
    c = np.zeros((a.shape[0], b.shape[1]))
    for i in range(len(c)):
        for j in range(len(c[i])):
            for k in range(len(a[i])):
                c[i][j] += a[i][k] * b[k][j]
    return c


def fatt(n):
    if n > 1:
        return fatt(n - 1) * n
    else:
        return 1


def fatit(n):
    ft = 1
    for i in range(1, n + 1):
        ft *= i
    return ft


def search(vett, x):
    for v in vett:
        if v == x:
            return True
    return False


def somma(vett):
    x = 0
    for v in vett:
        x += v
    return x


def sommainefficiente(vett):
    x = [0 for i in range(len(vett) + 1)]
    for i in range(len(vett)):
        x[i + 1] = vett[i] + x[i]
    return x[len(vett)]


def ordinamentoABolle(vett):
    for i in range(len(vett) - 1):
        scambiati = False
        for j in range(i + 1, len(vett) - 1):
            if vett[j-1] > vett[j]:
                tmp = vett[j-1]
                vett[j-1] = vett[j]
                vett[j] = tmp
                scambiati = True
        if not scambiati:
            return 0
    return 1
