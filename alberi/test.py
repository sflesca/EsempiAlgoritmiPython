from alberi.alberibinari import AlberoBin

a = AlberoBin(0)
b = AlberoBin(1)
c = AlberoBin(2)
d = AlberoBin(3)
e = AlberoBin(4)
f = AlberoBin(5)
a.setfigliosin(b)
a.setfigliodes(c)
c.setfigliosin(d)
b.setfigliosin(e)
b.setfigliodes(f)
for x in a:
    print(x)

l = []
a.visitainfissa(l)
print(l)

l = []
a.visitaanticipata(l)
print(l)

l = []
a.visitaposticipata(l)
print(l)