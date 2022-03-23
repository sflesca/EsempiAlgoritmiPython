from alberi.alberibinari import AlberoBin


class ABR:
    def __init__(self):
        self.valori = None

    def search(self, val):
        x = self.__search__(valori, val)
        if x is None:
            return False
        if x.val == val:
            return True
        return False

    def __search__(self, curr, val):  # restituisce il nodo in cui è contenuto il valore cercato oppure il padre del nodo in cui sarebbe contenuto il valore cercato se non presente
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
