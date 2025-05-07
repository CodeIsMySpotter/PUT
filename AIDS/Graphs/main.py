
from Sorts import *
from Generator import *
from Matrix import *

def print_matrix(matrix):
    cut_matrix = [row[1:] for row in matrix[1:]]
    max_width = max(len(str(value)) for row in cut_matrix for value in row)

    for row in cut_matrix:
        print(' '.join(f'{value:>{max_width}}' for value in row))

edges = [
    (1, 2),
    (2, 4),
    (2, 5),
    (3, 2),
    (3, 1),
    (4, 3),
    (5, 4),
    (5, 1)

]
n = 5


matrix = build_graph_matrix(n, edges)
print_matrix(matrix)