from typing import List
import random

def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)  # Scelta randomizzata del pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Esempio di utilizzo
arr = [38, 27, 43, 3, 9, 82, 10]
print("Array originale:", arr)
print("Array ordinato:", quick_sort(arr))