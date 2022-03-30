from alberi.alberibinari import AlberoBin


class ABR:
    def __init__(self):
        self.valori: AlberoBin = None

    def search(self, val):
        x = self.__search__(valori, val)
        if x is None:
            return False
        if x.val == val:
            return True
        return False

    def __search__(self, curr,
                   val) -> AlberoBin:  # restituisce il nodo in cui è contenuto il valore cercato oppure il padre del nodo in cui sarebbe contenuto il valore cercato se non presente
        if curr is None:
            return curr
        if curr.val == val:
            return curr
        elif curr.val > val:
            if curr.sin is not None:
                return self.__search__(curr.sin, val)
            else:
                return curr
        else:
            if curr.des is not None:
                return self.__search__(curr.des, val)
            else:
                return curr

    def min(self):
        if self.valori is None:
            return None
        curr = self.valori
        while curr.sin is not None:
            curr = curr.sin
        return curr.val

    def max(self):
        if self.valori is None:
            return None
        curr = self.valori
        while curr.des is not None:
            curr = curr.des
        return curr.val

    def insert(self, val):
        n = self.__search__(self.valori, val)
        if n is None:  # Inserimento sulla radice
            self.valori = AlberoBin(val)
        else:
            if n.val != val:  # Inserimento generale
                nuovo = AlberoBin(val)
                if n.val > val:
                    n.setfigliosin(nuovo)
                else:
                    n.setfigliodes(nuovo)

    def delete(self, val):
        if self.valori is None:
            return
        n = self.__search__(self.valori, val)
        if n.val != val:
            return
        if (n.sin is not None) and (n.des is not None):
            tt = n.des
            while tt.sin is not None:
                tt = tt.sin
            n.val = tt.val
            n = tt
        padre = n.parent
        if padre is None:
            if n.sin is not None:
                self.valori = n.sin
                n.sin.pota()
            else:
                self.valori = n.des
                n.des.pota()
        else:
            if n.sin is not None:
                xx = n.sin
            else
                xx = n.des
            xx.pota()
            if padre.sin == n:
                n.pota()
                padre.sin = xx
            else:
                n.pota()
                padre.des = xx
