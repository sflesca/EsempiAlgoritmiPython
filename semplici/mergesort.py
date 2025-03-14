from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) > 1:
        mid = len(arr) // 2  # Trova il punto medio dell'array
        left_half: List[int] = arr[:mid]  # Dividi la parte sinistra
        right_half: List[int] = arr[mid:]  # Dividi la parte destra

        merge_sort(left_half)  # Ricorsivamente ordina la parte sinistra
        merge_sort(right_half)  # Ricorsivamente ordina la parte destra

        merge(arr, left_half, right_half)

    return arr


def merge(arr: List[int], left_half: List[int], right_half: List[int]) -> None:
    i = j = k = 0

    # Unisci le due metà ordinate
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Controlla se ci sono elementi rimasti
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1


# Esempio di utilizzo
arr = [38, 27, 43, 3, 9, 82, 10]
print("Array originale:", arr)
print("Array ordinato:", merge_sort(arr))