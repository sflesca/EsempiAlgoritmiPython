class ProblemaBack:
    def __init__(self):
        pass

    def risolvi(self):
        liv: int = 0
        rivedi: bool = False
        if not self.primaScelta(liv):
            return False
        while liv >= 0:
            if self.verificaVincoli(liv):
                if self.solCompleta(liv):
                    costruisciSoluzione(liv)
                    return True
                liv += 1
                if not self.primaScelta(liv):
                    rivedi = true
            else:
                if not self.successivaScelta(liv):
                    rivedi = true
            while rivedi and liv >= 0:
                liv -= 1
                if liv >= 0 and self.successivaScelta(liv):
                    rivedi = false
        return False

    def successivaScelta(self, liv: int):
        pass

    def solCompleta(self, liv: int):
        pass

    def verificaVincoli(self, liv: int):
        pass

    def primaScelta(self, liv: int):
        pass

    def costruisciSoluzione(self, liv: int):
        pass
