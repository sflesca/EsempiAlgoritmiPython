from grafi import GrafoMA
from grafi import GrafoLA, Grafo
from algosugrafi import visitaprofonditaRic, visitaprofondita, visitaampiezza, eaciclicoOR
from grafino import GrafoLANO, GrafoMANO
from unionfind import UnionFind
from scheduleratt import Scheduler, Attivita, Propedeuticita

g = GrafoMANO(4)
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


UF = UnionFind(5)
print('UF')
print(UF)
UF.union(UF.find(0), UF.find(1))
print('DOPO UNION Set(0) e Set(1)')
print(UF)
UF.union(UF.find(2), UF.find(1))
print('DOPO UNION Set(2) e Set(1)')
print(UF)


g: Grafo = GrafoLA(7)
g.aggiungiarco(0, 1)
g.aggiungiarco(0, 2)
g.aggiungiarco(1, 3)
# g.aggiungiarco(2, 3)
g.aggiungiarco(3, 4)
g.aggiungiarco(5, 6)
g.stampa()

print(visitaprofonditaRic(g, 0))
print(visitaprofondita(g, 0))
print(visitaampiezza(g, 0))
# print("E' connesso:"+str(econnesso(g)))
# print("E' albero:"+str(ealbero(g)))
# print("Num componenti connesse:"+str(numcompconnesse(g)))
# print("E' aciclico:"+str(eaciclico(g)))
print("E' aciclico:" + str(eaciclicoOR(g)))


listatt = [Attivita(str(i), i+1) for i in range(g.n)]
listprop = [Propedeuticita(x,y) for x,y in g.archi()]
schedulatore: Scheduler = Scheduler(listatt,listprop)
listatt = schedulatore.schedule()
print(listatt)