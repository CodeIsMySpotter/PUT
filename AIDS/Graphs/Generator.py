import random

def generate_dag(n):
    max_edges = n * (n - 1) // 2
    target_edges = max_edges // 2  # 50%

    edges = set()
    possible_edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    random.shuffle(possible_edges)

    for i in range(target_edges):
        edge = possible_edges[i]
        edges.add(edge)

    return edges
