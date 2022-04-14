class MySet:
    def __init__(self, elem: int):
        self.elementlist: list[int] = [elem]
        self.name: int = elem
        self.pos: int = self.name
        self.size: int = 1

    def __repr__(self):
        return "("+str(self.name)+", "+str(self.size)+", "+str(self.pos)+", "+str(self.elementlist) +")"


class UnionFind:
    def __init__(self, n: int):
        self.sets: list = [MySet(i) for i in range(n)]
        self.elements: list = [i for i in range(n)]

    def find(self, elem: int) -> MySet:
        return self.sets[self.elements[elem]]

    def union(self, a: MySet, b: MySet):
        if a.size < b.size:
            for el in a.elementlist:
                self.elements[el] = b.pos
                b.elementlist.append(el)
            b.size += a.size
            b.name = a.name
            a.size = 0
            a.elementlist = []
        else:
            for el in b.elementlist:
                self.elements[el] = a.pos
                a.elementlist.append(el)
            a.size += b.size
            b.size = 0
            b.elementlist = []


    def unionSenzaBilanciamento(self, a: MySet, b: MySet):
        for el in b.elementlist:
            self.elements[el] = a.pos
            a.elementlist.append(el)
        a.size += b.size
        b.size = 0
        b.elementlist = []

    def __repr__(self):
        return str(self.sets)+"\n"+str(self.elements)
