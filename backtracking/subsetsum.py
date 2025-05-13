from backtracking import ProblemaBack


class SubsetSum(ProblemaBack):
    def __init__(self, s: list[int], v: int):
        super().__init__()
        self.s = s
        self.v = v
        self.sol = [True for i in range(len(s))]
        self.soluzione = []

    def primaScelta(self, liv: int)->bool:
        if liv == len(self.s):
            return False
        else:
            self.sol[liv] = True
            return True

    def successivaScelta(self, liv: int)->bool:
        if self.sol[liv]:
            self.sol[liv] = False
            return True
        else:
            return False

    def solCompleta(self, liv: int)->bool:
        somma =0
        for i in range(liv+1):
            if self.sol[i]:
                somma += self.s[i]
        return somma == self.v

    def verificaVincoli(self, liv: int)->bool:
        somma = 0
        for i in range(liv + 1):
            if self.sol[i]:
                somma += self.s[i]
        return somma <= self.v

    def costruisciSoluzione(self, liv: int):
        for i in range(liv + 1):
            if self.sol[i]:
                self.soluzione.append(self.s[i])
s = [1,21,3,40,13,15,7,8,9,10]
v = 180
p:SubsetSum = SubsetSum(s, v)
if p.risolvi():
    print(f"SubsetSum({s}, {v})")
    print(f"{p.soluzione} - {sum(p.soluzione)}")
else:
    print("SubsetSum(s,v): no sol")
