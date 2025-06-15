import random

def generate_undirected_adjacency_matrix(n, x):
    # Inicjalizacja macierzy n x n zerami
    matrix = [[0]*n for _ in range(n)]

    # Maksymalna liczba krawędzi w grafie nieskierowanym bez pętli to n*(n-1)/2
    max_edges = n * (n - 1) // 2
    # Liczba krawędzi do wylosowania
    edges_to_add = int(max_edges * x)

    # Lista wszystkich możliwych krawędzi (i < j, by nie duplikować)
    possible_edges = [(i, j) for i in range(n) for j in range(i+1, n)]
    chosen_edges = random.sample(possible_edges, edges_to_add)

    for i, j in chosen_edges:
        matrix[i][j] = 1
        matrix[j][i] = 1  # graf nieskierowany - macierz symetryczna

    return matrix


def generate_directed_successors_list(n, x):
    # Maksymalna liczba krawędzi to n*(n-1) (bez pętli)
    max_edges = n * (n - 1)
    edges_to_add = int(max_edges * x)

    # Wszystkie możliwe krawędzie (i -> j), i != j
    possible_edges = [(i, j) for i in range(n) for j in range(n) if i != j]
    chosen_edges = random.sample(possible_edges, edges_to_add)

    # Inicjalizacja listy następników jako lista pustych list
    successors = [[] for _ in range(n)]

    for i, j in chosen_edges:
        successors[i].append(j)

    return successors


n = 5
x = 0.1

print("Macierz sąsiedztwa (nieskierowany):")
matrix = generate_undirected_adjacency_matrix(n, x)
for row in matrix:
    print(row)

print("\nLista następników (skierowany):")
succ_list = generate_directed_successors_list(n, x)
for i, neighbors in enumerate(succ_list):
    print(f"{i}: {neighbors}")
