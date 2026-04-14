class CodaPFIX:
    def __init__(self, maxp: int):
        self.code: list = [[] for x in range(maxp)]
        self.maxp: int = maxp
        self.size: int = 0

    def insert(self, val, p: int):
        if 0 <= p < self.maxp:
            self.code[p].append(val)
            self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        for i in range(self.maxp):
            if len(self.code[i]) > 0:
                self.size -= 1
                return self.code[i].pop(0)
        return None

    def top(self):
        if self.size == 0:
            return None
        for i in range(self.maxp):
            if len(self.code[i]) > 0:
                return self.code[i][0]
        return None

def radix_sort(arr: list[int]) -> list[int]:
    """
    Ordina una lista di interi non negativi con RadixSort LSD
    usando CodaPFIX con 10 bucket (cifre 0-9).
    """
    if not arr:
        return arr

    max_val = max(arr)
    exp = 1  # potenza di 10 della cifra corrente (1, 10, 100, ...)

    while max_val // exp > 0:
        coda = CodaPFIX(maxp=10)

        # Distribuzione: inserisci ogni elemento nel bucket
        # corrispondente alla cifra corrente
        for num in arr:
            cifra = (num // exp) % 10
            coda.insert(num, cifra)

        # Raccolta: estrai tutti gli elementi in ordine di priorità
        arr = []
        while coda.size > 0:
            arr.append(coda.pop())

        exp *= 10

    return arr


# --- Test ---
if __name__ == "__main__":
    dati = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Input: ", dati)
    print("Output:", radix_sort(dati))
    # Output: [2, 24, 45, 66, 75, 90, 170, 802]