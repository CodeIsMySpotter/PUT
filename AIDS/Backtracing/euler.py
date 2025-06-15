from collections import defaultdict

def find_euler_cycle_undirected(graph):
    import copy
    n = len(graph)
    total_edges = sum(sum(row) for row in graph) // 2
    path = [0]  # zaczynamy od wierzchołka 0

    # Sprawdzenie, czy wszystkie stopnie są parzyste
    def is_valid():
        for row in graph:
            if sum(row) % 2 != 0:
                return False
        return True

    # Właściwy algorytm z powracaniem
    def backtrack(v, visited_edges):
        if visited_edges == total_edges:
            return True
        for u in range(n):
            if graph[v][u] > 0:
                # przechodzimy przez krawędź
                graph[v][u] -= 1
                graph[u][v] -= 1
                path.append(u)

                if backtrack(u, visited_edges + 1):
                    return True

                # cofamy się (backtrack)
                path.pop()
                graph[v][u] += 1
                graph[u][v] += 1
        return False

    if not is_valid():
        return None  # brak cyklu Eulera

    # kopiujemy oryginalny graf (żeby nie zmieniać wejścia)
    graph = copy.deepcopy(graph)
    if backtrack(0, 0):
        return path
    return None


def find_euler_cycle_directed(adjlist):
    from collections import defaultdict
    import copy

    in_deg = defaultdict(int)
    out_deg = defaultdict(int)
    total_edges = 0

    for u in adjlist:
        out_deg[u] += len(adjlist[u])
        for v in adjlist[u]:
            in_deg[v] += 1
            total_edges += 1

    all_nodes = set(in_deg.keys()) | set(out_deg.keys())
    for v in all_nodes:
        if in_deg[v] != out_deg[v]:
            return None  # nie jest eulerowski

    graph = copy.deepcopy(adjlist)
    path = []
    start = next(iter(adjlist))

    # visited_edges musi być mutowalną zmienną (tu lista z 1 elementem)
    visited_edges = [0]

    def backtrack(v):
        if visited_edges[0] == total_edges:
            return True

        for i in range(len(graph[v])):
            u = graph[v][i]
            if u is None:
                continue
            # używamy krawędź
            graph[v][i] = None
            visited_edges[0] += 1
            path.append(u)

            if backtrack(u):
                return True

            # cofnij decyzję
            graph[v][i] = u
            visited_edges[0] -= 1
            path.pop()

        return False

    path.append(start)
    if backtrack(start):
        return path
    else:
        return None
