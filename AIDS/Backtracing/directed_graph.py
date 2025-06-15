import random
from collections import defaultdict

from hamilton import *
from euler import *



def generate_directed_graph(n, saturation):
    import random

    max_edges = n * (n - 1)
    target_edges = int(saturation * max_edges)

    if target_edges % 3 != 0:
        target_edges -= target_edges % 3

    edges = set()
    in_deg = [0] * n
    out_deg = [0] * n

    # Losowe trójki typu x → y → z → x
    triplets = [(x, y, z) for x in range(n) for y in range(n) for z in range(n)
                if len({x, y, z}) == 3]

    added = 0
    for x, y, z in triplets:
        if added + 3 > target_edges:
            break
        if ((x, y) in edges or (y, z) in edges or (z, x) in edges):
            continue

        edges.add((x, y))
        edges.add((y, z))
        edges.add((z, x))

        out_deg[x] += 1
        in_deg[y] += 1
        out_deg[y] += 1
        in_deg[z] += 1
        out_deg[z] += 1
        in_deg[x] += 1

        added += 3


    print(target_edges, added)
    # Weryfikacja balansu
    for i in range(n):
        if in_deg[i] != out_deg[i]:
            print(f"❗ Wierzchołek {i} ma in={in_deg[i]}, out={out_deg[i]}")

    return edges




def edges_to_successors(edges):
    nast = {}
    for u, v in edges:
        if u not in nast:
            nast[u] = []
        nast[u].append(v)
    return nast

def find_euler_cycle_directed2(adjlist):
    from collections import defaultdict, deque

    # Oblicz stopnie
    in_deg = defaultdict(int)
    out_deg = defaultdict(int)
    for u in adjlist:
        out_deg[u] += len(adjlist[u])
        for v in adjlist[u]:
            in_deg[v] += 1

    # Sprawdź warunek Eulera
    nodes = set(in_deg.keys()) | set(out_deg.keys())
    for v in nodes:
        if in_deg[v] != out_deg[v]:
            return None

    # Tworzymy kopię grafu do modyfikacji
    graph = {u: deque(vs) for u, vs in adjlist.items()}

    stack = []
    circuit = []
    curr = next(iter(graph))

    while stack or graph.get(curr):
        if not graph.get(curr):
            circuit.append(curr)
            curr = stack.pop()
        else:
            stack.append(curr)
            curr = graph[curr].popleft()

    circuit.append(curr)
    circuit.reverse()
    return circuit


# ====================
# 🔍 TESTY
# ====================
def test_graph(n, saturation):
    print(f"🧪 Test: n = {n}, saturation = {saturation}")
    edges = generate_directed_graph(n, saturation)
    print(f"   ➤ Liczba krawędzi: {len(edges)}")

    print("  ➤ Eulerowski graf skierowany:")


    now = time.time()
    if find_euler_cycle_directed(edges_to_successors(edges)):
        print("   ✅ Zawiera cykl Eulera")
    else:
        print("   ❌ Brak cyklu Eulera")
    print(f"   ⏱️ Czas: {time.time() - now:.4f} sekund")


    print("  ➤ Hamilatonowski graf skierowany:")
    now = time.time()
    if find_hamilton_cycle_directed(edges_to_successors(edges)):
        print("   ✅ Zawiera cykl Hamiltona")
    else:
        print("   ❌ Brak cyklu Hamiltona")
    print(f"   ⏱️ Czas: {time.time() - now:.4f} sekund")


    print()


if __name__ == "__main__":
    import sys
    import time
    sys.setrecursionlimit(10**6)  # Zwiększenie limitu rekurencji
    n_values = [5, 15, 25, 35, 45]
    saturation = 0.5

    for n in n_values:
        test_graph(n, saturation)

    print("Testy zakończone.")