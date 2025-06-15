import random

from euler import *
from hamilton import *


def possible_triplets(possible_vertices, graph):
    triplets = []
    length = len(possible_vertices)
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                x = possible_vertices[i]
                y = possible_vertices[j]
                z = possible_vertices[k]
                if graph[x][y] == 0 and graph[x][z] == 0 and graph[y][z] == 0:
                    triplets.append((x, y, z))
    return triplets



def generate_undirected_graph(n, saturation):
    max_edges = n * (n - 1) // 2
    target_edges = int(saturation * max_edges)
    if target_edges % 2 != 0:
        target_edges -= 1

    graph = [[0]*n for _ in range(n)]
    for i in range(n):
        u = i
        v = (i + 1) % n
        graph[u][v] = graph[v][u] = 1
    edges_added = n

    degrees = [2]*n

    possible_vertices = [v for v in range(n) if sum(graph[v]) < n - 1]
    triplets = possible_triplets(possible_vertices, graph)

    while edges_added <= target_edges-3 and triplets:
        x, y, z = triplets.pop()
        if graph[x][y] == 0 and graph[x][z] == 0 and graph[y][z] == 0:
            graph[x][y] = graph[y][x] = 1
            graph[x][z] = graph[z][x] = 1
            graph[y][z] = graph[z][y] = 1
            degrees[x] += 2
            degrees[y] += 2
            degrees[z] += 2
            edges_added += 3
      

    print(target_edges, edges_added)

    if any(d % 2 != 0 for d in degrees):
        print("❗ Ostrzeżenie: Nie wszystkie wierzchołki mają parzysty stopień!")

    return graph


def wszystkie_stopnie_parzyste(graph):
    n = len(graph)
    for i in range(n):
        stopien = sum(graph[i])
        if stopien % 2 != 0:
            return False
    return True

def test_graph(n, saturation):
    print(f"🧪 Test: n = {n}, saturation = {saturation}")
    matrix = generate_undirected_graph(n, saturation)



    print("  ➤ Eulerowski graf skierowany:")
    now = time.time()
    if find_euler_cycle_undirected(matrix):
        print("   ✅ Zawiera cykl Eulera")
    else:
        print("   ❌ Brak cyklu Eulera")
    print(f"   ⏱️ Czas: {time.time() - now:.4f} sekund")

    print("  ➤ Hamilatonowski graf skierowany:")
    now = time.time()
    if find_hamilton_cycle_undirected(matrix):
        print("   ✅ Zawiera cykl Hamiltona")
    else:
        print("   ❌ Brak cyklu Hamiltona")
    print(f"   ⏱️ Czas: {time.time() - now:.4f} sekund")

    print()

if __name__ == "__main__":
    import sys
    import time
    sys.setrecursionlimit(10**6)  # Zwiększenie limitu rekurencji
    n_values = [5, 15, 25]
    saturation = 0.5

    for n in n_values:
        test_graph(n, saturation)

    print("Testy zakończone.")