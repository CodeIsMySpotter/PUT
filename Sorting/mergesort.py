import numpy as np


def mergeSort(arr: np.ndarray, compares: int) -> tuple[np.ndarray, int]:
    if len(arr) <= 1:
        return arr, compares
    
    mid = len(arr) // 2
    left = mergeSort_(arr[:mid])
    right = mergeSort_(arr[mid:])
    
    sorted_arr, compares = merge_(left, right)
    return sorted_arr

def merge(left: np.ndarray, right: np.ndarray) -> tuple[np.ndarray, int]:
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return np.array(result)






def mergeSort_(arr: np.ndarray, compares: int) -> tuple[np.ndarray, int]:
    if len(arr) <= 1:
        return arr, compares
    
    mid = len(arr) // 2
    left, compares = mergeSort_(arr[:mid], compares)
    right, compares = mergeSort_(arr[mid:], compares)
    
    sorted_arr, compares = merge_(left, right, compares)
    return sorted_arr, compares

def merge_(left: np.ndarray, right: np.ndarray, compares: int) -> tuple[np.ndarray, int]:
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        compares += 3
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return np.array(result), compares