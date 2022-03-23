import numpy as np
import time

from semplici.simple import moltiplicazionematrici, sommamatrici, fatt, fatit, search, somma, sommainefficiente, \
    ordinamentoABolle, merge, fib, quasifib

# m1 = np.array([[0, 1], [2, 3]])
# m2 = np.array([[0, 2, 3], [1, 4, 5]])
# m3 = sommamatrici(m1,m2)
# print(m3)
# m3 = moltiplicazionematrici(m1,m2)
# print(m3)
#
# print("fatt(6)=" + str(fatt(6)))
# print("fatt(6)=" + str(fatit(6)))
#
# trovato = search([1,2,3,4,8,5], 14)
# print(trovato)


# v1 = np.random.randint(0, 10000000, 10000000)
# x = 15
# ts = time.time()
# trovato = search(v1, x)
# te = time.time() - ts
# if trovato:
#     print(str(x)+" è presente")
# else:
#     print(str(x) + " non è presente")
# print("Tempo ricerca = " + str(te)+" secondi")


# v1 = np.random.randint(0, 4, 100000000)
# ts = time.time()
# s = somma(v1)
# te = time.time() - ts
# print(str(s)+"è la somma")
# print("Tempo ricerca = " + str(te)+" secondi")

# v1 = [1, 2,3, 6, 28, 2]
# print(somma(v1))
# print(sommainefficiente(v1))

# v = [0,3,12,24,1,2]
# v1 = [12,5, 17, 34,1]
# ordinamentoABolle(v)
# ordinamentoABolle(v1)
# print(v)
# print(v1)
# v2 = merge(v,v1)
# print(v2)

# for i in range(1,21):
#     print("fib "+str(i)+"="+str(fib(i)))

quasifib(6)