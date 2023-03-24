from heap.heap import Heap


class HeapModificabile(Heap):

    def __init__(self, dim):
        super().__init__(dim)
        self.positions = {}

    def ins(self, val):
        if self.actualdim < self.dim:
            self.values[self.actualdim] = val
            curr = self.actualdim
            self.positions[val]=curr
            self.actualdim +=1
            while curr > 0 and self.values[curr]<self.values[(curr+1)//2-1]:
                tmp = self.values[(curr+1)//2-1]
                self.values[(curr + 1) // 2 - 1] = self.values[curr]
                self.values[curr] = tmp
                self.positions[self.values[(curr + 1) // 2 - 1]] = (curr + 1) // 2 - 1
                self.positions[self.values[curr]] = curr
                curr = (curr+1)//2-1
        else:
            raise HeapFullError()

    def out(self):
        x = self.top()
        self.values[0] = self.values[self.actualdim-1]
        self.actualdim -= 1
        curr = 0
        self.positions[self.values[curr]] = curr
        while (curr+1) * 2 - 1 < self.actualdim:
            if (curr+1) * 2 < self.actualdim:
                if self.values[curr] > min(self.values[(curr+1) * 2 - 1], self.values[(curr+1) * 2]):
                    if self.values[(curr+1) * 2 - 1] < self.values[(curr+1) * 2]:
                        tmp = self.values[curr]
                        self.values[curr] = self.values[(curr+1) * 2 - 1]
                        self.values[(curr+1) * 2 - 1] = tmp
                        self.positions[self.values[curr]] = curr
                        self.positions[self.values[(curr+1) * 2 - 1]] = (curr+1) * 2 - 1
                        curr = (curr+1) * 2 - 1
                    else:
                        tmp = self.values[curr]
                        self.values[curr] = self.values[(curr+1) * 2]
                        self.values[(curr+1) * 2] = tmp
                        self.positions[self.values[curr]] = curr
                        self.positions[self.values[(curr+1) * 2]] = (curr+1) * 2
                        curr = (curr+1) * 2
                else:
                    break
            elif self.values[curr] > self.values[(curr + 1) * 2 - 1]:
                tmp = self.values[curr]
                self.values[curr] = self.values[(curr + 1) * 2 - 1]
                self.values[(curr + 1) * 2 - 1] = tmp
                self.positions[self.values[curr]] = curr
                self.positions[self.values[(curr + 1) * 2 - 1]] = (curr + 1) * 2 - 1
                curr = (curr + 1) * 2 - 1
            else:
                break
        del self.positions[x]
        return x

    def update(self, val):
        if not val in self.positions:     #implementazione inefficiente sarebbe necessario un accesso diretto
            self.ins(val)
        else:
            curr = self.positions[val]
            if val < self.values[curr]:
                self.values[curr] = val
                del self.positions[val]
                self.positions[val] = curr
                while curr > 0 and self.values[curr] < self.values[(curr + 1) // 2 - 1]:
                    tmp = self.values[(curr + 1) // 2 - 1]
                    self.values[(curr + 1) // 2 - 1] = self.values[curr]
                    self.values[curr] = tmp
                    self.positions[self.values[(curr + 1) // 2 - 1]] = (curr + 1) // 2 - 1
                    self.positions[self.values[curr]] = curr
                    curr = (curr + 1) // 2 - 1
            else:
                self.values[curr] = val
                del self.positions[val]
                self.positions[val] = curr
                while (curr + 1) * 2 - 1 < self.actualdim:
                    if (curr + 1) * 2 < self.actualdim:
                        if self.values[curr] > min(self.values[(curr + 1) * 2 - 1], self.values[(curr + 1) * 2]):
                            if self.values[(curr + 1) * 2 - 1] < self.values[(curr + 1) * 2]:
                                tmp = self.values[curr]
                                self.values[curr] = self.values[(curr + 1) * 2 - 1]
                                self.values[(curr + 1) * 2 - 1] = tmp
                                self.positions[self.values[curr]] = curr
                                self.positions[self.values[(curr + 1) * 2 - 1]] = (curr + 1) * 2 - 1
                                curr = (curr + 1) * 2 - 1
                            else:
                                tmp = self.values[curr]
                                self.values[curr] = self.values[(curr + 1) * 2]
                                self.values[(curr + 1) * 2] = tmp
                                self.positions[self.values[curr]] = curr
                                self.positions[self.values[(curr + 1) * 2]] = (curr + 1) * 2
                                curr = (curr + 1) * 2
                        else:
                            break
                    if self.values[curr] > self.values[(curr + 1) * 2 - 1]:
                        tmp = self.values[curr]
                        self.values[curr] = self.values[(curr + 1) * 2 - 1]
                        self.values[(curr + 1) * 2 - 1] = tmp
                        self.positions[self.values[curr]] = curr
                        self.positions[self.values[(curr + 1) * 2 - 1]] = (curr + 1) * 2 - 1
                        curr = (curr + 1) * 2 - 1
                    else:
                        break

    def evuoto(self):
        return self.actualdim==0

    def print(self):
        super().print()
        print(self.positions)
