import numpy as np

from semplici.simple import moltiplicazionematrici, sommamatrici, fatt, fatit, search

m1 = np.array([[0, 1], [2, 3]])
m2 = np.array([[0, 2, 3], [1, 4, 5]])
m3 = sommamatrici(m1,m2)
print(m3)
m3 = moltiplicazionematrici(m1,m2)
print(m3)

print("fatt(6)=" + str(fatt(6)))
print("fatt(6)=" + str(fatit(6)))

trovato = search([1,2,3,4,8,5], 14)
print(trovato)