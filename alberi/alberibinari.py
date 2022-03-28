from re import match

from alberi.eccezioni import ValoriScorretti


class AlberoBin:
    def __init__(self, val):
        self.val = val
        self.sin = None
        self.des = None
        self.parent = None

    def setfigliosin(self, sin):
        # complessità: indichiamo com n il numero di nodi già memorizzati nell'albero
        # theta(1)
        if not isinstance(sin, AlberoBin):
            raise ValoriScorretti("tipo figlio non consentito")
        if sin is None:
            return
        if sin.parent is not None:
            raise ValoriScorretti("Il figlio passato ha già un padre")
        if self.sin is not None:
            self.sin.pota()  # staccare il figlio esistente
        sin.parent = self
        self.sin = sin

    def setfigliodes(self, des):
        # complessità: indichiamo com n il numero di nodi già memorizzati nell'albero
        # theta(1)
        if not isinstance(des, AlberoBin):
            raise ValoriScorretti("tipo figlio non consentito")
        if self.des is not None:
            self.des.pota()
        if des.parent is not None:
            raise ValoriScorretti("Il figlio passato ha già un padre")
        des.parent = self
        self.des = des

    def pota(self):
        # complessità: indichiamo com n il numero di nodi già memorizzati nell'albero
        # theta(1)
        if self.parent is None:
            return
        if self.parent.sin == self:
            self.parent.sin = None
        if self.parent.des == self:
            self.parent.des = None
        self.parent = None

    def __iter__(self):
        self.cur = self
        self.hasnext = True
        while self.cur.sin is not None:
            self.cur = self.cur.sin
        return self

    def __next__(self):
        if not self.hasnext:
            raise StopIteration
        tmp = self.cur.val
        self.__avanza__()
        return tmp

    def __avanza__(self):
        direzione = "des"
        while direzione != "stop":
            match direzione:
                case "sin":
                    if self.cur.sin is None:
                        direzione = "stop"
                    else:
                        self.cur = self.cur.sin
                        direzione = "sin"
                case "des":
                    if self.cur.des is None:
                        direzione = "su"
                    else:
                        self.cur = self.cur.des
                        direzione = "sin"
                case "su":
                    if self.cur.parent is None:
                        self.hasnext = False
                        direzione = "stop"
                    else:
                        if self.cur.parent.sin == self.cur:
                            self.cur = self.cur.parent
                            direzione = "stop"
                        else:
                            self.cur = self.cur.parent
                            direzione = "su"



    def visitainfissa(self, l):
        if self.sin is not None:
            self.sin.visitainfissa(l)
        l.append(self.val)
        if self.des is not None:
            self.des.visitainfissa(l)

    def visitaanticipata(self, l):
        l.append(self.val)
        if self.sin is not None:
            self.sin.visitaanticipata(l)
        if self.des is not None:
            self.des.visitaanticipata(l)

    def visitaposticipata(self, l):
        if self.sin is not None:
            self.sin.visitaposticipata(l)
        if self.des is not None:
            self.des.visitaposticipata(l)
        l.append(self.val)


    def visitalivelli(self, l):
        coda = [self]
        while len(coda)!=0:
            curr = coda.pop(0)
            l.append(curr.val)
            if curr.sin is not None:
                coda.append(curr.sin)
            if curr.des is not None:
                coda.append(curr.des)
        return l

def tonestedlist(a):
    if a is None:
        return None
    return [a.val,tonestedlist(a.sin),tonestedlist(a.des)]

def fromnestedlist(l):
    if l is None:
        return None
    x = AlberoBin(l[0])
    s = fromnestedlist(l[1])
    if s is not None:
        x.setfigliosin(s)
    d = fromnestedlist(l[2])
    if d is not None:
        x.setfigliodes(d)
    return x
