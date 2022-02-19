from eccezioni import HeapFullError


class Heap:
    def __init__(self, dim):
        self.dim = dim
        self.actualdim = 0
        self.values = [0 for x in range(dim)]

    def ins(self, val):
        if self.actualdim < self.dim:
            self.values[self.actualdim] = val
            curr = self.actualdim
            self.actualdim +=1
            while curr > 0 and self.values[curr]<self.values[(curr+1)//2-1]:
                tmp = self.values[(curr+1)//2-1]
                self.values[(curr + 1) // 2 - 1] = self.values[curr]
                self.values[curr] = tmp
                curr = (curr+1)//2-1
        else:
            raise HeapFullError()

    def top(self):
        if self.actualdim <= 0:
            raise HeapEmptyError()
        return self.values[0]

    def out(self):
        x = self.top()
        self.values[0] = self.values[self.actualdim-1]
        self.actualdim -= 1
        curr = 0
        while (curr+1) * 2 - 1 < self.actualdim:
            if (curr+1) * 2 < self.actualdim:
                if self.values[curr] > min(self.values[(curr+1) * 2 - 1], self.values[(curr+1) * 2]):
                    if self.values[(curr+1) * 2 - 1] < self.values[(curr+1) * 2]:
                        tmp = self.values[curr]
                        self.values[curr] = self.values[(curr+1) * 2 - 1]
                        self.values[(curr+1) * 2 - 1] = tmp
                        curr = (curr+1) * 2 - 1
                    else:
                        tmp = self.values[curr]
                        self.values[curr] = self.values[(curr+1) * 2]
                        self.values[(curr+1) * 2] = tmp
                        curr = (curr+1) * 2
                else:
                    break
            if self.values[curr] > self.values[(curr + 1) * 2 - 1]:
                tmp = self.values[curr]
                self.values[curr] = self.values[(curr + 1) * 2 - 1]
                self.values[(curr + 1) * 2 - 1] = tmp
                curr = (curr + 1) * 2 - 1
            else:
                break
        return x

    def print(self):
        print("Numero elementi:"+ str(self.actualdim))
        print("Dimensione max:" + str(self.dim))
        print("Elenco Valori")
        print(self.values[:self.actualdim])