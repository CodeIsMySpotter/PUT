
from Sorts import *
from Generator import *
from Matrix import *
import sqlite3

def print_matrix(matrix):
    cut_matrix = [row[1:] for row in matrix[1:]]
    max_width = max(len(str(value)) for row in cut_matrix for value in row)

    for row in cut_matrix:
        print(' '.join(f'{value:>{max_width}}' for value in row))

edges, n = read_from_file()
matrix = build_adjacency_matrix(n, edges)
gmatrix = build_graph_matrix(n, edges)


class Record():

    def __init__(self, name, time, alg):
        self.name = name
        self.time = time
        self.alg = alg


def test():
    tests = [100, 200, 300, 400, 500, 600, 700,
             800, 900, 1000, 1100, 1200, 1300, 
             1400, 1500]



print()
print_matrix(gmatrix)
print()

print(dfs_sort_gmatrix(gmatrix))
print(dfs_sort_matrix(matrix))
print(kahn_sort_gmatrix(gmatrix, n))
print(kahn_sort_matrix(matrix))
