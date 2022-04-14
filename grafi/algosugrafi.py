from grafi import Grafo, GrafoLA, GrafoMA
from grafino import GrafoNO, GrafoLANO, GrafoMANO


def __visitaprofonditaRic__(g: Grafo, nodo: int, visitati: list[bool], risultato: list[int]):
    if not visitati[nodo]:
        visitati[nodo] = True
        risultato.append(nodo)
        for ad in g.adiacenti(nodo):
            __visitaprofonditaRic__(g, ad, visitati, risultato)


def visitaprofonditaRic(g: Grafo, nodo: int) -> list[int]:
    risultato: list[int] = []
    __visitaprofonditaRic__(g, nodo, [False for i in range(g.n)], risultato)
    return risultato



def visitaprofondita(g: Grafo, nodo: int) -> list[int]:
    risultato: list[int] = []
    pila: list[int] = []
    visitati: list[bool] = [False for i in range(g.n)]
    pila.append(nodo)
    while pila:
        curr: int = pila.pop()
        if not visitati[curr]:
            visitati[curr] =  True
            risultato.append(curr)
            for ad in reversed(list(g.adiacenti(curr))):
                pila.append(ad)
    return risultato


def visitaampiezza(g: Grafo, nodo: int) -> list[int]:
    risultato: list[int] = []
    pila: list[int] = []
    visitati: list[bool] = [False for i in range(g.n)]
    pila.append(nodo)
    while pila:
        curr: int = pila.pop(0)
        if not visitati[curr]:
            visitati[curr] = True
            risultato.append(curr)
            for ad in g.adiacenti(curr):
                pila.append(ad)
    return risultato


def econnesso(g: GrafoNO)->bool:
    result = visitaampiezza(g,0)
    if len(result) == g.n:
        return True
    return False

def ealbero(g: GrafoNO)->bool:
    return g.n==g.m+1 and econnesso(g)

g: GrafoNO = GrafoLANO(5)
g.aggiungiarco(0, 1)
g.aggiungiarco(0, 2)
g.aggiungiarco(1, 3)
#g.aggiungiarco(2, 3)
g.aggiungiarco(3, 4)
g.stampa()

print(visitaprofonditaRic(g,0))
print(visitaprofondita(g,0))
print(visitaampiezza(g,0))
print("E' connesso:"+str(econnesso(g)))
print("E' albero:"+str(ealbero(g)))