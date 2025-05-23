from collections import defaultdict

def eulerian_cycle_matrix(graph):
    n = len(graph)
    graph_copy = [row[:] for row in graph]
    path = []

    def dfs(u):
        for v in range(n):
            while graph_copy[u][v] > 0:
                graph_copy[u][v] -= 1
                graph_copy[v][u] -= 1
                dfs(v)
        path.append(u)

    # Sprawdź parzystość stopni
    for i in range(n):
        if sum(graph[i]) % 2 != 0:
            print("Graf wejściowy nie zawiera cyklu.")
            return

    visited = [False] * n
    def dfs_check(u):
        visited[u] = True
        for v in range(n):
            if graph[u][v] > 0 and not visited[v]:
                dfs_check(v)

    start = next((i for i in range(n) if sum(graph[i]) > 0), None)
    if start is None:
        print("Graf wejściowy nie zawiera cyklu.")
        return

    dfs_check(start)
    for i in range(n):
        if sum(graph[i]) > 0 and not visited[i]:
            print("Graf wejściowy nie zawiera cyklu.")
            return

    dfs(start)
    print(path[::-1])



def eulerian_cycle_adjlist(graph):
    graph_copy = defaultdict(list)
    in_deg = defaultdict(int)
    out_deg = defaultdict(int)

    for u in graph:
        for v in graph[u]:
            graph_copy[u].append(v)
            out_deg[u] += 1
            in_deg[v] += 1

    all_nodes = set(in_deg) | set(out_deg)
    for node in all_nodes:
        if in_deg[node] != out_deg[node]:
            print("Graf wejściowy nie zawiera cyklu.")
            return

    # Sprawdź silną spójność (tu uproszczenie — DFS w obu kierunkach)
    def dfs(g, u, visited):
        visited.add(u)
        for v in g[u]:
            if v not in visited:
                dfs(g, v, visited)

    start = next(iter(graph), None)
    if start is None:
        print("Graf wejściowy nie zawiera cyklu.")
        return

    visited = set()
    dfs(graph, start, visited)
    if len(visited) != len(all_nodes):
        print("Graf wejściowy nie zawiera cyklu.")
        return

    # Odwrócony graf
    rev_graph = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            rev_graph[v].append(u)

    visited.clear()
    dfs(rev_graph, start, visited)
    if len(visited) != len(all_nodes):
        print("Graf wejściowy nie zawiera cyklu.")
        return

    path = []

    def dfs_euler(u):
        while graph_copy[u]:
            v = graph_copy[u].pop()
            dfs_euler(v)
        path.append(u)

    dfs_euler(start)

    total_edges = sum(len(vs) for vs in graph.values())
    if len(path) == total_edges + 1:
        print(path[::-1])
    else:
        print("Graf wejściowy nie zawiera cyklu.")
