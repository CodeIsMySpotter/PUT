import numpy as np
from generator import *
from records import *
import time as ti



def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1 

    for j in range(low, high):
        if arr[j] >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] 

    arr[i + 1], arr[high] = arr[high], arr[i + 1] 
    return i + 1  

def quickSort_(arr, low, high, changes, comparisons):
    if low < high:
        pi, changes, comparisons = partition_(arr, low, high, changes, comparisons)
        quickSort_(arr, low, pi - 1, changes, comparisons)
        quickSort_(arr, pi + 1, high, changes, comparisons)
    return changes, comparisons

def partition_(arr, low, high, changes, comparisons):
    pivot = arr[high]  
    i = low - 1  

    for j in range(low, high):
        comparisons += 1  
        if arr[j] >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] 
            changes += 1  

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  
    changes += 1  
    return i + 1, changes, comparisons

# =================================================================

def test():
  records = []

  for n in SIZES:

    records.append(test_A(n))
    records.append(test_V(n))
    records.append(test_I(n))
    records.append(test_D(n))
    records.append(test_R(n))
    print(f'quicksort - {n} Done')

  return records


def test_I(n: int):
  array1 = Generator.generate_increasing(n)
  array2 = array1.copy()

  start = ti.time()
  quickSort(array1, 0, len(array1)-1)
  stop = ti.time()

  changes, comparisons = 0, 0
  changes, comparisons = quickSort_(array2, 0, len(array1)-1, changes, comparisons)
  return Record(f'quicksort', n, "I", stop-start, comparisons, changes)


def test_D(n: int):
  array1 = Generator.generate_decreasing(n)
  array2 = array1.copy()

  start = ti.time()
  quickSort(array1, 0, len(array1)-1)
  stop = ti.time()

  changes, comparisons = 0, 0
  changes, comparisons = quickSort_(array2, 0, len(array1)-1, changes, comparisons)
  return Record(f'quicksort', n, "D", stop-start, comparisons, changes)

def test_A(n: int):
  array1 = Generator.generate_A_random(n)
  array2 = array1.copy()

  start = ti.time()
  quickSort(array1, 0, len(array1)-1)
  stop = ti.time()

  changes, comparisons = 0, 0
  changes, comparisons = quickSort_(array2, 0, len(array1)-1, changes, comparisons)
  return Record(f'quicksort', n, "A", stop-start, comparisons, changes)

def test_V(n: int):
  array1 = Generator.generate_V_random(n)
  array2 = array1.copy()

  start = ti.time()
  quickSort(array1, 0, len(array1)-1)
  stop = ti.time()

  changes, comparisons = 0, 0
  changes, comparisons = quickSort_(array2, 0, len(array1)-1, changes, comparisons)
  return Record(f'quicksort', n, "V", stop-start, comparisons, changes)

def test_R(n: int):
  array1 = Generator.generate_random(n)
  array2 = array1.copy()

  start = ti.time()
  quickSort(array1, 0, len(array1)-1)
  stop = ti.time()

  changes, comparisons = 0, 0
  changes, comparisons = quickSort_(array2, 0, len(array1)-1, changes, comparisons)
  return Record(f'quicksort', n, "R", stop-start, comparisons, changes)

# =================================================================