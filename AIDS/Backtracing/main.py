from euler import *
from hamilton import *

def build_adjacency_matrix(n, edges):
    matrix = [[0] * (n+1) for _ in range(n+1)]
    for u, v in edges:
        matrix[u][v] = 1
    return matrix


def build_adjacency_list(n, edges):
    adj_list = {i: [] for i in range(n)}
    for u, v in edges:
        adj_list[u].append(v)
    return adj_list



def graph_from_edge_list(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        n = int(lines[0].strip())
        edges = [tuple(map(int, line.strip().split())) for line in lines[1:]]
    return n, edges

def read_from_file():
    edges = []
    with open("graph.txt") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            line = line.split(" ")
            edges.append((int(line[0]), int(line[1])))
    
    return edges[1:], edges[0][0]

def main():
    print("Euler (macierz sąsiedztwa):")
    graph_matrix = [
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0]
    ]
    eulerian_cycle_matrix([row[:] for row in graph_matrix])  

    print("\nEuler (lista następników):")
    graph_adjlist = {
        0: [1],
        1: [2],
        2: [0]
    }
    eulerian_cycle_adjlist(graph_adjlist)

    print("\nHamilton (macierz sąsiedztwa):")
    cycle = hamiltonian_cycle_matrix([
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ])

    print(cycle)

    print("\nHamilton (lista następników):")
    cycle = hamiltonian_cycle_adjlist({
        0: [1, 2],
        1: [2, 3],
        2: [3, 0],
        3: [0]
    })

    print(cycle)

main()
