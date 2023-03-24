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


def visitaprofondita(g: Grafo, nodo: int) -> list[int]:  # MA theta(n^2) LA theta(m) spaziale theta(n)
    risultato: list[int] = []
    pila: list[int] = []
    visitati: list[bool] = [False for i in range(g.n)]
    pila.append(nodo)
    while pila:
        curr: int = pila.pop()
        if not visitati[curr]:
            visitati[curr] = True
            risultato.append(curr)
            for ad in reversed(list(g.adiacenti(curr))):
                pila.append(ad)
    return risultato


def visitaampiezza(g: Grafo, nodo: int) -> list[int]:  # MA theta(n^2) LA theta(m) spaziale theta(n)
    risultato: list[int] = []
    coda: list[int] = []
    visitati: list[bool] = [False for i in range(g.n)]
    coda.append(nodo)
    while coda:
        curr: int = coda.pop(0)  # theta(n)
        if not visitati[curr]:
            visitati[curr] = True  # theta(n)
            risultato.append(curr)  # theta(n)
            for ad in g.adiacenti(curr):  # LA theta(m)    MA theta(n^2)
                if not visitati[ad]:  # theta(m)
                    coda.append(ad)  # theta(m)
    return risultato


def econnesso(g: GrafoNO) -> bool:
    result = visitaampiezza(g, 0)
    if len(result) == g.n:
        return True
    return False


def ealbero(g: GrafoNO) -> bool:  # MA theta(n^2) LA theta(n)
    return g.n == g.m + 1 and econnesso(g)


def numcompconnesse(g: GrafoNO) -> int:
    visitati: list[bool] = [False for i in range(g.n)]
    comp: int = 0
    for i in range(g.n):
        if not visitati[i]:
            comp += 1
            __visitaprofonditaRic__(g, i, visitati, [])
    return comp


def eaciclico(g: GrafoNO) -> bool:
    return g.n == g.m + numcompconnesse(g)


def trovazero(gradi: list[int], rimossi) -> int:
    for i in range(len(gradi)):
        if gradi[i] == 0 and not rimossi[i]:
            return i
    return -1


def tuttizero(gradi: list[int]) -> bool:
    for x in gradi:
        if x != 0:
            return False
    return True


def eaciclicoOR(g: Grafo) -> bool:                          #theta(n^2)
    gradi: list[int] = [0 for i in range(g.n)]              #theta(n)
    rimossi: list[bool] = [False for i in range(g.n)]       #theta(n)
    for x, y in g.archi():                                  #MA theta(n^2) LA theta(m)
        gradi[y] += 1
    curr = trovazero(gradi, rimossi)                        #theta(n)
    while curr != -1:                                       #per ogni nodo che rimuovo (nel caso peggiore per ogni nodo) theta(n^2)
        rimossi[curr] = True
        for ad in g.adiacenti(curr):                        #MA theta(n) LA theta(grado_i(curr))
            gradi[ad] -= 1
        curr = trovazero(gradi, rimossi)                    #theta(n)
    return tuttizero(gradi)                                 #theta(n)



