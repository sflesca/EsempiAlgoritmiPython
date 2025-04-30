import sys
from platform import android_ver

from alberi.abr import ABR
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


def almenounafoglia(a: AlberoBin, val)->bool:
    if a is None:
        return False
    if not a.sin and not a.des:
        return a.val == val
    return almenounafoglia(a.sin, val) or almenounafoglia(a.des, val)


def tuttiminori(a:AlberoBin, val)->bool:
    if a is None:
        return True
    return a.val<val and tuttiminori(a.sin, val) and tuttiminori(a.des, val)


def tuttimaggiori(a:AlberoBin, val)->bool:
    if a is None:
        return True
    return a.val>=val and tuttimaggiori(a.sin, val) and tuttimaggiori(a.des, val)


def diricerca(a: AlberoBin)->bool:
    if a is None:
        return True
    return (tuttiminori(a.sin, a.val) and tuttimaggiori(a.des, a.val)
            and diricerca(a.sin) and diricerca(a.des))


def diricercasbagliato(a: AlberoBin)->bool:
    if a is None:
        return True
    if (a.sin is not None):
        if a.sin.val >= val:
            return False
    if (a.des is not None):
        if a.des.val >= val:
            return False
    return diricercasbagliato(a.sin) and diricercasbagliato(a.des)

def costruisciABRdavettoreordinato(abr:ABR, l:list, inizio: int, fine:int):
    if fine<inizio:
        return
    med = (inizio+fine)//2
    abr.insert(l[med])
    costruisciABRdavettoreordinato(abr,l,inizio, med-1)
    costruisciABRdavettoreordinato(abr, l, med+1, fine)