from collections import defaultdict

def eulerian_cycle_matrix(graph):
    n = len(graph)
    total_edges = sum(sum(row) for row in graph) // 2  # liczba krawędzi
    path = []
    visited_edges = [0]  # mutowalny licznik wykorzystanych krawędzi

    # Sprawdzenie, czy graf jest eulerowski (każdy wierzchołek ma parzysty stopień)
    for i in range(n):
        if sum(graph[i]) % 2 != 0:
            return None  # brak cyklu Eulera

    def backtrack(v):
        if visited_edges[0] == total_edges:
            return True

        for u in range(n):
            if graph[v][u] > 0:
                # Zużywamy krawędź (v,u) i (u,v)
                graph[v][u] -= 1
                graph[u][v] -= 1
                visited_edges[0] += 1
                path.append(u)

                if backtrack(u):
                    return True

                # Cofamy decyzję
                graph[v][u] += 1
                graph[u][v] += 1
                visited_edges[0] -= 1
                path.pop()

        return False

    path.append(0)  # startujemy z wierzchołka 0
    if backtrack(0):
        return path
    else:
        return None


def eulerian_cycle_adjlist(adjlist):
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
