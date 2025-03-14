import sys

from alberi.alberibinari import AlberoBin


def altezza(a: AlberoBin) ->int:
    if a is None:
        return 0
    return 1 + max(altezza(a.sin),altezza(a.des))

menoinfinito = -sys.maxint

def massimo(a: AlberoBin)->int:
    if a is None:
        return menoinfinito
    return max(a.val,massimo(a.sin),massimo(a.des))

def verifica1(a: AlberoBin)->bool:
    if a is None or (a.sin is None and a.des is None):
        return True
    return massimo(a.sin)<massimo(a.des) and verifica1(a.sin) and verifica1(a.des)
