class ProblemaBack:
    def __init__(self):
        pass

    def risolvi(self)->bool:
        liv: int = 0
        rivedi: bool = False
        if not self.primaScelta(liv):
            return False
        while liv >= 0:
            if self.verificaVincoli(liv):
                if self.solCompleta(liv):
                    self.costruisciSoluzione(liv)
                    return True
                liv += 1
                if not self.primaScelta(liv):
                    rivedi = True
            else:
                if not self.successivaScelta(liv):
                    rivedi = True
            while rivedi and liv >= 0:
                liv -= 1
                if liv >= 0 and self.successivaScelta(liv):
                    rivedi = False
        return False

    def primaScelta(self, liv: int)->bool:
        pass

    def successivaScelta(self, liv: int)->bool:
        pass

    def solCompleta(self, liv: int)->bool:
        pass

    def verificaVincoli(self, liv: int)->bool:
        pass

    def costruisciSoluzione(self, liv: int):
        pass
