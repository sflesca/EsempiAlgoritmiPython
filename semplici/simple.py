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


def fib(n):
    if n <= 2:
        return 1
    else:
        return


def fibc(n):
    if n <= 1:
        return 1, 1
    else:
        x, y = fibc(n - 1)
        return x + y, x

def fib1(n):
    x, y =  fibc(n)
    return x


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
        for j in range(1, len(vett) - i):
            if vett[j - 1] > vett[j]:
                tmp = vett[j - 1]
                vett[j - 1] = vett[j]
                vett[j] = tmp
                scambiati = True
        if not scambiati:
            return 0
    return 1


def merge(A, B):
    n = len(A)
    m = len(B)
    C = []
    i = 0
    j = 0
    while i < n and j < m:
        if A[i] <= B[j]:
            C.append(A[i])
            i = i + 1
        else:
            C.append(B[j])
            j = j + 1
    while i < n:
        C.append(A[i])
        i = i + 1
    while j < m:
        C.append(B[j])
        j = j + 1
    return C


def quasifib(n):
    if n <= 2:
        return 1
    else:
        return quasifib(n - 1) + quasifib(n - 1)
