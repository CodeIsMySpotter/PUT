
from Sorts import *
from Generator import *
from Matrix import *



edges = [
  (0+1, 1+1),
  (1+1, 3+1),
  (1+1, 4+1),
  (2+1, 1+1),
  (2+1, 0+1),
  (3+1, 2+1),
  (4+1, 3+1),
  (4+1, 0+1)
]
n = 5

matrix = build_graph_matrix(n, edges)
for idx in range(n+1):
  if idx != 0:
    print(matrix[idx][1:])