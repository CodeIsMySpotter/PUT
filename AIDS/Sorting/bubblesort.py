import numpy as np
import time as ti
from generator import *
from records import *

def bubbleSort(array: np.ndarray):
  for idx in range(len(array)):
    for jdx in range(len(array) - idx - 1):
      if array[jdx] < array[jdx + 1]:
        array[jdx], array[jdx + 1] = array[jdx + 1], array[jdx]

def bubbleSort_(array: np.ndarray):
  changes, comparsions = 0, 0
  for idx in range(len(array)):
    for jdx in range(len(array) - idx - 1):
      comparsions += 1
      if array[jdx] < array[jdx + 1]:
        array[jdx], array[jdx + 1] = array[jdx + 1], array[jdx]
        changes += 1
  return changes, comparsions



# =================================================================

def test():
  records = []

  for n in SIZES:

    records.append(test_A(n))
    records.append(test_V(n))
    records.append(test_I(n))
    records.append(test_D(n))
    records.append(test_R(n))
    print(f'BubbleSort - {n} Done')

  return records


def test_I(n: int):
  array1 = Generator.generate_increasing(n)
  array2 = array1.copy()

  start = ti.time()
  bubbleSort(array1)
  stop = ti.time()

  changes, comparsions = bubbleSort_(array2)
  return Record(f'bubblesort', n, "I", stop-start, comparsions, changes)


def test_D(n: int):
  array1 = Generator.generate_decreasing(n)
  array2 = array1.copy()

  start = ti.time()
  bubbleSort(array1)
  stop = ti.time()

  changes, comparsions = bubbleSort_(array2)
  return Record(f'bubblesort', n, "D", stop-start, comparsions, changes)

def test_A(n: int):
  array1 = Generator.generate_A_random(n)
  array2 = array1.copy()

  start = ti.time()
  bubbleSort(array1)
  stop = ti.time()

  changes, comparsions = bubbleSort_(array2)
  return Record(f'bubblesort', n, "A", stop-start, comparsions, changes)

def test_V(n: int):
  array1 = Generator.generate_V_random(n)
  array2 = array1.copy()

  start = ti.time()
  bubbleSort(array1)
  stop = ti.time()

  changes, comparsions = bubbleSort_(array2)
  return Record(f'bubblesort', n, "V", stop-start, comparsions, changes)

def test_R(n: int):
  array1 = Generator.generate_random(n)
  array2 = array1.copy()

  start = ti.time()
  bubbleSort(array1)
  stop = ti.time()

  changes, comparsions = bubbleSort_(array2)
  return Record(f'bubblesort', n, "R", stop-start, comparsions, changes)

# =================================================================