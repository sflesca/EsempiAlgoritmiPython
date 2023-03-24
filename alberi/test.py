import sys

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
    vI(a, l)
    return l


def vI(a, l):
    if a is None:
        return
    vI(a.sin, l)
    l.append(a.val)
    vI(a.des, l)


def somma(a: AlberoBin)->int:
    if a is None:
        return 0
    return a.val+somma(a.sin)+somma(a.des)


def verifica(a: AlberoBin) -> bool:
    if a is None:
        return False
    if a.sin is None and a.des is None:
        return False
    return verifica(a.sin) or verifica(a.des) or (a.val == somma(a.sin) + somma(a.des))

def mini(a:AlberoBin)->int:
    if(a is None):
        return -sys.maxint
    minimo = a.val
    if(a.sin is not None):
        minimo = min(minimo, mini(a.sin))
    if(a.des is not None):
        minimo = min(minimo,mini(a.des))
    return minimo

def maxi(a:AlberoBin)->int:
    if(a is None):
        return sys.maxint
    massimo = a.val
    if(a.sin is not None):
        massimo = max(massimo, maxi(a.sin))
    if(a.des is not None):
        massimo = max(massimo,maxi(a.des))
    return massimo

def ediricercaminmax(a:AlberoBin,mini:int,maxi:int)->bool:
    if a is None:
        return True
    return (mini<=a.val and a.val <= maxi) and \
           ediricercaminmax(a.sin,mini, a.val-1) and ediricercaminmax(a.des,a.val+1,maxi)


def ediricerca(a:AlberoBin)->bool:
    if a is None:
        return True
    return ediricercaminmax(a,mini(a),maxi(a))

def sonosimmetrici(a:AlberoBin,b:AlberoBin)->bool:
    if a is None and b is None:
        return True
    if (a is not None and b is None) or (a is None and b is not None):
        return False
    return a.val==b.val and sonosimmetrici(a.sin,b.des) and sonosimmetrici(a.des, b.sin)

def esimmetrico(a:AlberoBin)->bool:
    return sonosimmetrici(a,a)



lalb = tonestedlist(a)
print(lalb)

alb = fromnestedlist([0, [1, [3, None, None], [4, None, None]], [1, [5, None, None], None]])
print(tonestedlist(alb))
print(esimmetrico(alb))

alb = fromnestedlist([0, [1, [3, None, None], [4, None, None]], [1, [4, None, None], [3, None, None]]])
print(tonestedlist(alb))
print(esimmetrico(alb))
