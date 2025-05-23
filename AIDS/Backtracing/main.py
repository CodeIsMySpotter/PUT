from euler import *
from hamilton import *

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
