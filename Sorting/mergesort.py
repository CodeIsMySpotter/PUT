import numpy as np
from generator import *
import time as ti
from records import Record

def mergeSort(arr: np.ndarray):
    if len(arr) <= 1:
        return np.array(arr, ndmin=1)
    
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    
    sorted_arr = merge(left, right)
    return sorted_arr

def merge(left: np.ndarray, right: np.ndarray):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
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

def merge_(left: np.ndarray, right: np.ndarray, comparisons: int) -> tuple[np.ndarray, int]:
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] >= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return np.array(result), comparisons


# =================================================================

def test():
  records = []

  for n in SIZES:

    records.append(test_A(n))
    records.append(test_V(n))
    records.append(test_I(n))
    records.append(test_D(n))
    records.append(test_R(n))
    print(f'MergeSort - {n} Done')

  return records


def test_I(n: int):
  array1 = Generator.generate_increasing(n)
  array2 = array1.copy()

  start = ti.time()
  mergeSort(array1)
  stop = ti.time()

  comparisons = 0
  changes, comparisons = mergeSort_(array2, comparisons)
  return Record(f'mergesort', n, "I", stop-start, comparisons, changes)


def test_D(n: int):
  array1 = Generator.generate_decreasing(n)
  array2 = array1.copy()

  start = ti.time()
  mergeSort(array1)
  stop = ti.time()

  comparsions = 0
  changes, comparsions = mergeSort_(array2, comparsions)
  return Record(f'mergesort', n, "D", stop-start, comparsions, changes)

def test_A(n: int):
  array1 = Generator.generate_A_random(n)
  array2 = array1.copy()

  start = ti.time()
  mergeSort(array1)
  stop = ti.time()

  comparisons = 0
  changes, comparisons = mergeSort_(array2, comparisons)
  return Record(f'mergesort', n, "A", stop-start, comparisons, changes)

def test_V(n: int):
  array1 = Generator.generate_V_random(n)
  array2 = array1.copy()

  start = ti.time()
  mergeSort(array1)
  stop = ti.time()

  comparsions = 0
  changes, comparsions = mergeSort_(array2, comparsions)
  return Record(f'mergesort', n, "V", stop-start, comparsions, changes)

def test_R(n: int):
  array1 = Generator.generate_random(n)
  array2 = array1.copy()

  start = ti.time()
  mergeSort(array1)
  stop = ti.time()

  comparsions = 0
  changes, comparsions = mergeSort_(array2, comparsions)
  return Record(f'mergesort', n, "R", stop-start, comparsions, changes)

# =================================================================