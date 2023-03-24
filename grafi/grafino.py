import numpy as np

class GrafoNO:
    def __init__(self,n:int):
        self.n = n
        self.m = 0

    def aggiungiarco(self, x, y):
        pass

    def rimuoviarco(self, x, y):
        pass

    def arco(self, x, y):
        pass

    def adiacenti(self, x):
        pass

    def archi(self):
        pass

    def stampa(self):
        pass


class GrafoMANO(GrafoNO):
    def __init__(self, n):  # crea un grafo con numero di nodi nodes
        super().__init__(n)
        self.mat = np.zeros((n, n), np.bool_)


    def aggiungiarco(self, x, y):
        if not self.mat[x][y]:
            self.mat[x][y] = True
            self.mat[y][x] = True
            self.m += 1

    def rimuoviarco(self, x, y):
        if self.mat[x][y]:
            self.mat[x][y] = False
            self.mat[y][x] = False
            self.m -= 1

    def arco(self, x, y):
        return self.mat[x][y]

    def adiacenti(self, x):
        return IterArcoMAAdiacenti(self, x)

    def archi(self):
        return IterArcoMA(self)

    def stampa(self):
        for x in range(self.mat.shape[0]):
            for y in range(self.mat.shape[1]):
                if self.mat[x][y]:
                    print("(" + str(x) + ", " + str(y) + ")")


class IterArcoMAAdiacenti:
    def __init__(self, g, x):
        self.g = g
        self.x = x

    def __iter__(self):
        self.y = 0
        while self.y < self.g.mat.shape[1] and not self.g.mat[self.x][self.y]:
            self.y += 1
        if self.y < self.g.mat.shape[1]:
            self.hasnext = True
        else:
            self.hasnext = False
        return self

    def __next__(self):
        if not self.hasnext:
            raise StopIteration
        tmp = self.y
        self.y += 1
        while self.y < self.g.mat.shape[1] and not self.g.mat[self.x][self.y]:
            self.y += 1
        if self.y < self.g.mat.shape[1]:
            self.hasnext = True
        else:
            self.hasnext = False
        return tmp


class IterArcoMA:
    def __init__(self, g):
        self.g = g

    def __iter__(self):
        self.x = 0
        self.it = iter(self.g.adiacenti(self.x))
        return self

    def __next__(self):
        trovato = False
        while not trovato:
            try:
                y = next(self.it)
                if y >= self.x:
                    trovato = True
            except StopIteration:
                if self.x < self.g.n-1:
                    self.x += 1
                    self.it = iter(self.g.adiacenti(self.x))
                else:
                    raise StopIteration
        return self.x, y


class GrafoLANO(GrafoNO):
    def __init__(self, n):  # crea un grafo con numero di nodi nodes
        super().__init__(n)
        self.mat = [[] for i in range(n)]

    def aggiungiarco(self, x, y):
        if y not in self.mat[x]:
            self.mat[x].append(y)
            self.mat[y].append(x)
            self.m += 1

    def rimuoviarco(self, x, y):
        if self.arco(x,y):
            self.mat[x].remove(y)
            self.mat[y].remove(x)
            self.m -=1

    def arco(self, x, y):
        return y in self.mat[x]

    def adiacenti(self, x):
        return self.mat[x]

    def archi(self):
        return IterArcoLA(self)

    def stampa(self):
        for x in range(len(self.mat)):
            for y in self.mat[x]:
                print("(" + str(x) + ", " + str(y) + ")")

class IterArcoLA:
    def __init__(self, g):
        self.g:GrafoLA = g

    def __iter__(self):
        self.x = 0
        self.it = iter(self.g.adiacenti(self.x))
        return self

    def __next__(self):
        trovato = False
        while not trovato:
            try:
                y = next(self.it)
                if y >= self.x:
                    trovato = True
            except StopIteration:
                if self.x < self.g.n-1:
                    self.x += 1
                    self.it = iter(self.g.adiacenti(self.x))
                else:
                    raise StopIteration
        return self.x, y

