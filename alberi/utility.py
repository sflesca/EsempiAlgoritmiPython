import sys

from alberi.alberibinari import AlberoBin


def altezza(a: AlberoBin) ->int:
    if a is None:
        return 0
    return 1 + max(altezza(a.sin),altezza(a.des))

def _xor(a:int, b: int)-> int:
    return a+b if a+b<=2 else 2


def verifica(a: AlberoBin) ->int:
    if a is None:
        return 0
    if not a.sin and not a.des:
        return 1 if a.val == 0 else 0
    return _xor(verifica(a.sin), verifica(a.des))

def verificacorretta(a: AlberoBin) ->bool:
    return verifica(a)==1

menoinfinito = -sys.maxsize

def massimo(a: AlberoBin)->int:
    if a is None:
        return menoinfinito
    return max(a.val,massimo(a.sin),massimo(a.des))

def verifica1(a: AlberoBin)->bool:
    if a is None or (a.sin is None and a.des is None):
        return True
    return massimo(a.sin)<massimo(a.des) and verifica1(a.sin) and verifica1(a.des)
