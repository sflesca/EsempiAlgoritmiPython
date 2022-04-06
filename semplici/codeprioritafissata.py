class CodaPFIX:
    def __init__(self, maxp: int):
        self.code:list = [[] for x in range(maxp)]
        self.maxp:int = maxp
        self.size:int = 0

    def insert(self, val, p:int):
        if p<self.maxp:
            self.code[p].append(val)
            self.size+=1


    def pop(self):
        if self.size==0:
            return None
        for i in range(maxp):
            if len(self.code[i])>0:
                self.size-=1
                return self.code[i].pop(0)

    def top(self):
        if self.size==0:
            return None
        for i in range(maxp):
            if len(self.code[i])>0:
                return self.code[i][0]