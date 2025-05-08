import random

def generate_dag(n):
    max_edges = n * (n - 1) // 2
    target_edges = max_edges // 2  # 50%

    edges = []
    possible_edges = [(i, j) for i in range(1, n + 1) for j in range(i + 1, n + 1)]
    random.shuffle(possible_edges)

    for i in range(target_edges):
        edge = possible_edges[i]
        edges.append(edge)
    return edges


def read_from_file():
    edges = []
    with open("graph.txt") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            line = line.split(" ")
            edges.append((int(line[0]), int(line[1])))
    
    return edges[1:], edges[0][0]