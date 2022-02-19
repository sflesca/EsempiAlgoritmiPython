class HeapFullError(Exception):
    def __init__(self, message="Heap pieno"):
        self.message = message