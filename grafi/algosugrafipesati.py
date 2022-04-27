import sys

from grafinopesati import GrafoNOP, GrafoNOLAP
from heap.heapmodificabile import HeapModificabile
from unionfind import UnionFind


def _peso(elem):
    return elem[2]


class Pair:
    def __init__(self, x, p):
        self.x = x
        self.p = p

    def __lt__(self, other):
        return self.p < other.p

    def __eq__(self, other):
        return self.x == other.x

    def __hash__(self):
        return self.x

    def print(self):
        print("(" + str(self.x) + ", " + str(self.p) + ")")

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.p) + ")"

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.p) + ")"


def kruskal(g: GrafoNOP):
    archiordinati = sorted(g.archi(), key=_peso)
    forest: UnionFind = UnionFind(g.n)
    result = []
    count = 0
    for x, y, p in archiordinati:
        if forest.find(x) != forest.find(y):
            result.append((x, y, p))
            forest.union(forest.find(x), forest.find(y))
            count += 1
        if count == g.n - 1:
            return result
    return []


def prim(g: GrafoNOP):
    padri: list[int] = [-1 for i in range(g.n)]
    pesi: list[int] = [sys.maxsize for i in range(g.n)]
    preso: list[bool] = [False for i in range(g.n)]
    curr: int = 0
    padri[0] = 0
    preso[0] = True
    count = 1
    result = []
    mioheap: HeapModificabile = HeapModificabile(g.n)
    for a in g.adiacenti(curr):
        mioheap.ins(Pair(a.y, a.peso))
        padri[a.y] = curr
        pesi[a.y] = a.peso
    while not mioheap.evuoto():
        count += 1
        cp: Pair = mioheap.out()
        preso[cp.x] = True
        result.append((padri[cp.x], cp.x, cp.p))
        for a in g.adiacenti(cp.x):
            if not preso[a.y]:
                if padri[a.y] == -1:
                    mioheap.ins(Pair(a.y, a.peso))
                    padri[a.y] = cp.x
                    pesi[a.y] = a.peso
                elif pesi[a.y] > a.peso:
                    mioheap.update(Pair(a.y, a.peso))
                    padri[a.y] = cp.x
                    pesi[a.y] = a.peso
    if count == g.n:
        return result
    else:
        return []


g = GrafoNOLAP(5)
g.aggiungiarco(0, 1, 2.1)
g.aggiungiarco(0, 2, 1.1)
g.aggiungiarco(1, 2, 1)
g.aggiungiarco(3, 0, 1)
g.aggiungiarco(3, 4, 1.2)
g.aggiungiarco(0, 4, 2.2)
g.stampa()

print(kruskal(g))
print(prim(g))
