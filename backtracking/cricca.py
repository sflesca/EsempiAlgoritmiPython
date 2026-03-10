from backtracking import ProblemaBack
from grafi.grafino import GrafoNO, GrafoMANO


class Cricca(ProblemaBack):
    def __init__(self, g: GrafoNO, k: int):
        self.g: Grafo = g
        self.nodes: list[int] = [-1 for i in range(k)]
        self.sol: list[int] = []

    def primaScelta(self, liv: int) -> bool:
        if liv == 0:
            self.nodes[liv] = 0
            return True
        if self.nodes[liv - 1] >= self.g.n - 1:
            return False
        self.nodes[liv] = self.nodes[liv - 1] + 1
        return True

    def successivaScelta(self, liv: int) -> bool:
        if self.nodes[liv] >= self.g.n - 1:
            return False
        self.nodes[liv] = self.nodes[liv] + 1
        return True

    def solCompleta(self, liv: int) -> bool:
        return liv == len(self.nodes) - 1

    def verificaVincoli(self, liv: int) -> bool:
        for i in range(liv - 1):
            if not self.g.arco(self.nodes[i], self.nodes[liv]):
                return False
        return True

    def costruisciSoluzione(self, liv: int):
        for x in self.nodes:
            self.sol.append(x)


g: GrafoNO = GrafoMANO(6)
g.aggiungiarco(0,1)
g.aggiungiarco(1,4)
g.aggiungiarco(0,4)
g.aggiungiarco(2,1)
g.aggiungiarco(1,5)
g.aggiungiarco(3,4)
g.stampa()

c:Cricca = Cricca(g,3)
if c.risolvi():
    print("Cricca(g,3)")
    print(c.sol)
else:
    print("Cricca(g,3): no sol")

c:Cricca = Cricca(g,4)
if c.risolvi():
    print("Cricca(g,4)")
    print(c.sol)
else:
    print("Cricca(g,4): no sol")
