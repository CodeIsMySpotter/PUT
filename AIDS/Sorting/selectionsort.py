import numpy as np
import time as ti
from generator import *
from records import *

def selectionSort(array: np.ndarray):
  n = len(array)
  for idx in range(n-1):
    max_idx = idx
    for jdx in range(idx + 1, n):
      if array[jdx] < array[max_idx]:
        max_idx = jdx
    if max_idx != idx:
      array[idx] = array[max_idx]

def selectionSort_(array: np.ndarray):
  changes, comparisons = 0, 0

  n = len(array)
  for idx in range(n-1):
    max_idx = idx
    for jdx in range(idx + 1, n):
      comparisons += 1
      if array[jdx] < array[max_idx]:
        max_idx = jdx
    if max_idx != idx:
      changes += 1
      array[idx] = array[max_idx]

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
    print(f'SelectionSort - {n} Done')

  return records


def test_I(n: int):
  array1 = Generator.generate_increasing(n)
  array2 = array1.copy()

  start = ti.time()
  selectionSort(array1)
  stop = ti.time()

  changes, comparsions = selectionSort_(array2)
  return Record(f'selectionsort', n, "I", stop-start, comparsions, changes)


def test_D(n: int):
  array1 = Generator.generate_decreasing(n)
  array2 = array1.copy()

  start = ti.time()
  selectionSort(array1)
  stop = ti.time()

  changes, comparsions = selectionSort_(array2)
  return Record(f'selectionsort', n, "D", stop-start, comparsions, changes)

def test_A(n: int):
  array1 = Generator.generate_A_random(n)
  array2 = array1.copy()

  start = ti.time()
  selectionSort(array1)
  stop = ti.time()

  changes, comparsions = selectionSort_(array2)
  return Record(f'selectionsort', n, "A", stop-start, comparsions, changes)

def test_V(n: int):
  array1 = Generator.generate_V_random(n)
  array2 = array1.copy()

  start = ti.time()
  selectionSort(array1)
  stop = ti.time()

  changes, comparsions = selectionSort_(array2)
  return Record(f'selectionsort', n, "V", stop-start, comparsions, changes)

def test_R(n: int):
  array1 = Generator.generate_random(n)
  array2 = array1.copy()

  start = ti.time()
  selectionSort(array1)
  stop = ti.time()

  changes, comparsions = selectionSort_(array2)
  return Record(f'selectionsort', n, "R", stop-start, comparsions, changes)

# =================================================================