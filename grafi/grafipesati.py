class GrafoP:
    def __init__(self, n: int):
        self.n = n
        self.m = 0

    def aggiungiarco(self, x: int, y: int, peso: float):
        pass

    def rimuoviarco(self, x: int, y: int):
        pass

    def arco(self, x: int, y: int) -> float:
        pass

    def adiacenti(self, x: int):
        pass

    def archi(self):
        pass

    def stampa(self):
        pass


class CoppiaP:
    def __init__(self, y:int, peso:float):
        self.y=y
        self.peso=peso

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.y==other.y
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "(" + str(self.y) + ", " + str(self.peso) + ")"


class GrafoLAP(GrafoP):
    def __init__(self, n):  # crea un grafo con numero di nodi nodes
        super().__init__(n)
        self.mat = [[] for i in range(n)]

    def aggiungiarco(self, x: int, y: int, peso: float):
        if y not in self.mat[x]:
            self.mat[x].append(CoppiaP(y, peso))
            self.m += 1

    def rimuoviarco(self, x, y):
        try:
            self.mat[x].remove(CoppiaP(y,0))
            self.m -= 1
        except ValueError:
            pass

    def arco(self, x, y):
        c = self.mat[x][self.mat[x].index(CoppiaP(y,0))]
        return x, c.y, c.peso

    def adiacenti(self, x):
        return self.mat[x]

    def archi(self):
        return IterArcoLA(self)

    def stampa(self):
        for x in range(len(self.mat)):
            for c in self.mat[x]:
                print("(" + str(x) + ", " + str(c.y) + ", "+ str(c.peso) + ")")


class IterArcoLA:
    def __init__(self, g):
        self.g: GrafoLA = g

    def __iter__(self):
        self.x = 0
        self.it = iter(self.g.adiacenti(self.x))
        return self

    def __next__(self):
        trovato = False
        while not trovato:
            try:
                c = next(self.it)
                trovato = True
            except StopIteration:
                if self.x < self.g.n - 1:
                    self.x += 1
                    self.it = iter(self.g.adiacenti(self.x))
                else:
                    raise StopIteration
        return self.x, c.y, c.peso






g = GrafoLAP(4)
g.aggiungiarco(0, 1, 2.1)
g.aggiungiarco(0, 2, 1.1)
g.aggiungiarco(1, 2, 1)
g.aggiungiarco(2, 0, 1)
g.aggiungiarco(3, 0, 1)
g.stampa()

print("\n")
g.rimuoviarco(0,3)
g.stampa()
print("\n")
print(g.arco(0,1))

print("\n")
for c in g.archi():
    print(c)