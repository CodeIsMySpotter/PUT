import time as ti
from generator import *
import numpy
from records import *


def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0)

def heapify(arr, n, i):
    largest = i  
    left = 2 * i + 1
    right = 2 * i + 2  

    if left < n and arr[left] < arr[largest]:
        largest = left

    if right < n and arr[right] < arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  
        heapify(arr, n, largest)


def heapSort_(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n // 2 - 1, -1, -1):
        new_comparisons, new_swaps = heapify_(arr, n, i)
        comparisons += new_comparisons
        swaps += new_swaps

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        swaps += 1
        new_comparisons, new_swaps = heapify_(arr, i, 0)
        comparisons += new_comparisons
        swaps += new_swaps

    return comparisons, swaps

def heapify_(arr, n, i):
    largest = i  
    left = 2 * i + 1  
    right = 2 * i + 2  
    comparisons = 0
    swaps = 0

    if left < n:
        comparisons += 1
        if arr[left] < arr[largest]:
            largest = left

    if right < n:
        comparisons += 1
        if arr[right] < arr[largest]:
            largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  
        swaps += 1
        new_comparisons, new_swaps = heapify_(arr, n, largest)
        comparisons += new_comparisons
        swaps += new_swaps

    return comparisons, swaps



# =================================================================

def test():
  records = []

  for n in SIZES:

    records.append(test_A(n))
    records.append(test_V(n))
    records.append(test_I(n))
    records.append(test_D(n))
    records.append(test_R(n))
    print(f'HeapSort - {n} Done')

  return records


def test_I(n: int):
  array1 = Generator.generate_increasing(n)
  array2 = array1.copy()

  start = ti.time()
  heapSort(array1)
  stop = ti.time()

  changes, comparsions = heapSort_(array2)
  return Record(f'heapsort', n, "I", stop-start, comparsions, changes)


def test_D(n: int):
  array1 = Generator.generate_decreasing(n)
  array2 = array1.copy()

  start = ti.time()
  heapSort(array1)
  stop = ti.time()

  changes, comparsions = heapSort_(array2)
  return Record(f'heapsort', n, "D", stop-start, comparsions, changes)

def test_A(n: int):
  array1 = Generator.generate_A_random(n)
  array2 = array1.copy()

  start = ti.time()
  heapSort(array1)
  stop = ti.time()

  changes, comparsions = heapSort_(array2)
  return Record(f'heapsort', n, "A", stop-start, comparsions, changes)

def test_V(n: int):
  array1 = Generator.generate_V_random(n)
  array2 = array1.copy()

  start = ti.time()
  heapSort(array1)
  stop = ti.time()

  changes, comparsions = heapSort_(array2)
  return Record(f'heapsort', n, "V", stop-start, comparsions, changes)

def test_R(n: int):
  array1 = Generator.generate_random(n)
  array2 = array1.copy()

  start = ti.time()
  heapSort(array1)
  stop = ti.time()

  changes, comparsions = heapSort_(array2)
  return Record(f'heapsort', n, "R", stop-start, comparsions, changes)

# =================================================================