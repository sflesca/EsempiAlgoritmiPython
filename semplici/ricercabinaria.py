from typing import List

def binary_search_list(arr: List[int], target: int) -> int:
    left: int = 0
    right: int = len(arr) - 1

    while left <= right:
        mid: int = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


data = [1, 3, 5, 7, 9]
print(binary_search_list(data, 7))  # 3
print(binary_search_list(data, 4))  # -1


import numpy as np
from numpy.typing import NDArray

def binary_search_numpy(arr: NDArray[np.int_], target: int) -> int:
    left: int = 0
    right: int = arr.shape[0] - 1

    while left <= right:
        mid: int = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


data = np.array([1, 3, 5, 7, 9], dtype=int)

print(binary_search_numpy(data, 5))  # 2
print(binary_search_numpy(data, 8))  # -1