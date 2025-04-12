import numpy as np
import time as ti
from generator import *
from records import *

def insertionSort(arr: np.ndarray) -> np.ndarray:
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def insertionSort_(arr: np.ndarray) -> tuple[int, int]:
    changes, comparisons = 0, 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            comparisons += 2
            changes += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        if j + 1 != i:
            changes += 1
            
    return changes, comparisons


# =================================================================

def test():
  records = []

  for n in SIZES:

    records.append(test_A(n))
    records.append(test_V(n))
    records.append(test_I(n))
    records.append(test_D(n))
    records.append(test_R(n))
    print(f'InsertionSort - {n} Done')

  return records


def test_I(n: int):
  array1 = Generator.generate_increasing(n)
  array2 = array1.copy()

  start = ti.time()
  insertionSort(array1)
  stop = ti.time()

  changes, comparsions = insertionSort_(array2)
  return Record(f'insertionsort', n, "I", stop-start, comparsions, changes)


def test_D(n: int):
  array1 = Generator.generate_decreasing(n)
  array2 = array1.copy()

  start = ti.time()
  insertionSort(array1)
  stop = ti.time()

  changes, comparsions = insertionSort_(array2)
  return Record(f'insertionsort', n, "D", stop-start, comparsions, changes)

def test_A(n: int):
  array1 = Generator.generate_A_random(n)
  array2 = array1.copy()

  start = ti.time()
  insertionSort(array1)
  stop = ti.time()

  changes, comparsions = insertionSort_(array2)
  return Record(f'insertionsort', n, "A", stop-start, comparsions, changes)

def test_V(n: int):
  array1 = Generator.generate_V_random(n)
  array2 = array1.copy()

  start = ti.time()
  insertionSort(array1)
  stop = ti.time()

  changes, comparsions = insertionSort_(array2)
  return Record(f'insertionsort', n, "V", stop-start, comparsions, changes)

def test_R(n: int):
  array1 = Generator.generate_random(n)
  array2 = array1.copy()

  start = ti.time()
  insertionSort(array1)
  stop = ti.time()

  changes, comparsions = insertionSort_(array2)
  return Record(f'insertionsort', n, "R", stop-start, comparsions, changes)

# =================================================================