from grafi import GrafoMA
from grafi import GrafoLA

g = GrafoLA(4)
g.aggiungiarco(0, 1)
g.aggiungiarco(0, 2)
g.aggiungiarco(1, 2)
g.aggiungiarco(2, 0)
g.aggiungiarco(3, 0)
g.stampa()

print("adiacenti di 0")
it = g.adiacenti(0)
for a in it:
    print(a)

print("tutti")
it = g.archi()
for a in it:
    print(a)