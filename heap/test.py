from heap import Heap
from heapmodificabile import HeapModificabile

class Pair:
    def __init__(self, x, p):
        self.x = x
        self.p = p

    def __lt__(self, other):
        return self.p< other.p

    def __eq__(self, other):
        return self.x == other.x

    def __hash__(self):
        return self.x

    def print(self):
        print("("+str(self.x)+", "+str(self.p)+")")

    def __str__(self):
        return "("+str(self.x)+", "+str(self.p)+")"

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.p) + ")"

h = HeapModificabile(10)
h.ins(Pair(0,5))
h.ins(Pair(1,9))
h.ins(Pair(2,3))
h.ins(Pair(3,6))
h.ins(Pair(4,4))
h.print()

print(h.top())
print(h.out())
h.print()

h.update(Pair(4,2))
h.print()
h.update(Pair(1,1))
h.print()

h.update(Pair(1,9))
h.print()