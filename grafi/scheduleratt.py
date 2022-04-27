from grafi import GrafoLA
from algosugrafi import trovazero, tuttizero


class AttivitaNonSchedulabili(Exception):
    pass


class Attivita:
    def __init__(self, nome: str, durata: int):
        self.nome: str = nome
        self.durata: int = durata
        self.start: int = 0

    def __str__(self):
        return "("+self.nome+","+self.durata+","+self.start+")"

    def __repr__(self):
        return "("+self.nome+","+str(self.durata)+","+str(self.start)+")"


class Propedeuticita:
    def __init__(self, fromatt: int, toatt: int):
        self.fromatt: int = fromatt
        self.toatt: int = toatt



class Scheduler:
    def __init__(self, listaattivita: list[Attivita], prop: list[Propedeuticita]):
        self.atts: list(Attivita) = listaattivita
        self.grafo = GrafoLA(len(self.atts))
        for p in prop:
            self.grafo.aggiungiarco(p.fromatt, p.toatt)

    def addpropedeuticita(self, afrom: int, ato: int):
        self.grafo.aggiungiarco(afrom, ato)

    def schedule(self) -> list[Attivita]:
        gradi: list[int] = [0 for i in range(self.grafo.n)]
        rimossi: list[bool] = [False for i in range(self.grafo.n)]
        for x, y in self.grafo.archi():
            gradi[y] += 1
        curr = trovazero(gradi, rimossi)
        while curr != -1:
            rimossi[curr] = True
            for ad in self.grafo.adiacenti(curr):
                gradi[ad] -= 1
                if self.atts[ad].start < self.atts[curr].start + self.atts[curr].durata:
                    self.atts[ad].start = self.atts[curr].start + self.atts[curr].durata
            curr = trovazero(gradi, rimossi)
        if tuttizero(gradi):
            return self.atts
        else:
            raise AttivitaNonSchedulabili("propedeuticità cicliche")
