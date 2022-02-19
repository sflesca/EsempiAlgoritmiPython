from heap import Heap

h = Heap(10)
h.ins(5)
h.print()
h.ins(9)
h.print()
h.ins(3)
h.print()
h.ins(6)
h.print()
h.ins(4)
h.print()

print(h.top())
print(h.out())
h.print()
