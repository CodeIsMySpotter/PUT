
from Sorts import *
from Generator import *
from Matrix import *

def print_matrix(matrix):
    cut_matrix = [row[1:] for row in matrix[1:]]
    max_width = max(len(str(value)) for row in cut_matrix for value in row)

    for row in cut_matrix:
        print(' '.join(f'{value:>{max_width}}' for value in row))

edges, n = read_from_file()
matrix = build_adjacency_matrix(n, edges)
gmatrix = build_graph_matrix(n, edges)


print()
print_matrix(gmatrix)
print()

print(dfs_sort_gmatrix(gmatrix, n))
print(dfs_sort_matrix(matrix))
print(kahn_sort_gmatrix(matrix, n))
print(kahn_sort_matrix(matrix))
