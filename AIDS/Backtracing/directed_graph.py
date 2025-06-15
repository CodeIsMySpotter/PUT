import random
from collections import defaultdict

from hamilton import *
from euler import *



def generuj_graf(n, saturation):
    max_edges = n * (n - 1)
    target_edges = int(saturation * max_edges)
    
    if target_edges % 2 != 0:
        target_edges -= 1
    
    edges = set()
    in_deg = [0] * n
    out_deg = [0] * n

    for i in range(n):
        u, v = i, (i + 1) % n
        edges.add((u, v))
        out_deg[u] += 1
        in_deg[v] += 1
    
    possible_edges = [(u, v) for u in range(n) for v in range(n)
                      if u != v and (u, v) not in edges and (v, u) not in edges]
    random.shuffle(possible_edges)
    
    while len(edges) + 2 <= target_edges and possible_edges:
        (u, v) = possible_edges.pop()
        if (v, u) in edges:
            continue  
        
        edges.add((u, v))
        edges.add((v, u))
        
        out_deg[u] += 1
        in_deg[v] += 1
        out_deg[v] += 1
        in_deg[u] += 1

    # Sprawdzenie balansu
    for i in range(n):
        assert in_deg[i] == out_deg[i], f"Stopnie nie zbilansowane w wierzchołku {i}: in={in_deg[i]}, out={out_deg[i]}"

    return edges


def has_eulerian_cycle(n, edges):
    in_deg = [0] * n
    out_deg = [0] * n
    adj = [[] for _ in range(n)]
    
    for u, v in edges:
        out_deg[u] += 1
        in_deg[v] += 1
        adj[u].append(v)

    for i in range(n):
        if in_deg[i] != out_deg[i]:
            return False

    def dfs(u, visited):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs(v, visited)

    visited = [False] * n
    dfs(0, visited)
    return all(visited)
    



def edges_to_successors(edges):
    nast = {}
    for u, v in edges:
        if u not in nast:
            nast[u] = []
        nast[u].append(v)
    return nast


# ====================
# 🔍 TESTY
# ====================
def test_graph(n, saturation):
    print(f"🧪 Test: n = {n}, saturation = {saturation}")
    edges = generuj_graf(n, saturation)
    print(f"   ➤ Liczba krawędzi: {len(edges)}")

    print("  ➤ Eulerowski graf skierowany:")

    if eulerian_cycle_adjlist(edges_to_successors(edges)):
        print("   ✅ Zawiera cykl Eulera")
    else:
        print("   ❌ Brak cyklu Eulera")


    print("  ➤ Hamilatonowski graf skierowany:")
    if n <= 12:
        if hamiltonian_cycle_adjlist(edges_to_successors(edges)):
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