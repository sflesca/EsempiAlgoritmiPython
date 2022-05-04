from backtracking.backtracking import ProblemaBack
from grafi.grafino import GrafoNO


class Cricca(ProblemaBack):
    def __init__(self, g: GrafoNO):
        self.g: Grafo = g
        nodes: list[int] = [-1 for i in range(g.n)]