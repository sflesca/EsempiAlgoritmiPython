from alberi.alberibinari import AlberoBin, tonestedlist, fromnestedlist

a = AlberoBin(0)
b = AlberoBin(1)
c = AlberoBin(2)
d = AlberoBin(3)
e = AlberoBin(4)
f = AlberoBin(5)
a.setfigliosin(b)
a.setfigliodes(c)
b.setfigliosin(d)
b.setfigliodes(e)
c.setfigliosin(f)
# for x in a:
#     print(x)

l = []
a.visitainfissa(l)
print(l)

l = []
a.visitaanticipata(l)
print(l)

l = []
a.visitaposticipata(l)
print(l)

l = []
a.visitalivelli(l)
print(l)

def vI1(a):
    l = []
    vI(a,l)
    return l

def vI(a, l):
    if a is  None:
        return
    vI(a.sin, l)
    l.append(a.val)
    vI(a.des,l)


print("new")
print(vI1(a))

lalb = tonestedlist(a)
print(lalb)

alb = fromnestedlist(lalb)
print(tonestedlist(alb))