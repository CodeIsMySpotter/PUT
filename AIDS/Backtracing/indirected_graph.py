import random

from euler import *
from hamilton import *



def generuj_graf_macierz(n, saturation):
    max_edges = n * (n - 1) // 2  # maksymalna liczba krawędzi w grafie nieskierowanym bez pętli
    target_edges = int(saturation * max_edges)

    # zapewniamy parzystą liczbę krawędzi (nieobowiązkowe, ale ułatwia bilans stopni)
    if target_edges % 2 != 0:
        target_edges -= 1

    # inicjalizacja macierzy sąsiedztwa zerami
    graph = [[0]*n for _ in range(n)]
    
    edges_added = 0

    # 1. Tworzymy podstawowy cykl długości n (n krawędzi)
    for i in range(n):
        u = i
        v = (i + 1) % n
        graph[u][v] = 1
        graph[v][u] = 1
        edges_added += 1

    # 2. Przygotowujemy listę możliwych krawędzi do dodania (u < v, aby nie dublować)
    possible_edges = [(u, v) for u in range(n) for v in range(u+1, n)
                      if graph[u][v] == 0]
    random.shuffle(possible_edges)

    # 3. Dodajemy krawędzie, aż osiągniemy target_edges
    while edges_added < target_edges and possible_edges:
        u, v = possible_edges.pop()
        graph[u][v] = 1
        graph[v][u] = 1
        edges_added += 1

    return graph


def test_graph(n, saturation):
    print(f"🧪 Test: n = {n}, saturation = {saturation}")
    matrix = generuj_graf_macierz(n, saturation)

    for row in matrix:
        print(" ".join(str(x) for x in row))

    print("  ➤ Eulerowski graf skierowany:")

    if eulerian_cycle_matrix(matrix):
        print("   ✅ Zawiera cykl Eulera")
    else:
        print("   ❌ Brak cyklu Eulera")


    print("  ➤ Hamilatonowski graf skierowany:")
    if n <= 12:
        if hamiltonian_cycle_matrix(matrix):
            print("   ✅ Zawiera cykl Hamiltona")
        else:
            print("   ❌ Brak cyklu Hamiltona")
    else:
        print("   ⚠️ Pominięto test Hamiltona (zbyt duże n)")

    print()

# Przykładowe testy
test_graph(5, 0.25)
test_graph(6, 0.3)
test_graph(8, 0.9)
test_graph(10, 0.5)
test_graph(12, 1.0)