import numpy as np
import time

from semplici.simple import moltiplicazionematrici, sommamatrici, fatt, fatit, search

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


v1 = np.random.randint(0, 10000000, 10000000)
ts = time.time()
trovato = search(v1, 14)
te = time.time() - ts
print("Tempo =" + str(te))
