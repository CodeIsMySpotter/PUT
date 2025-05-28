from collections import defaultdict

def eulerian_cycle_matrix(graph):
    n = len(graph)
    path = []

    def is_valid_graph():
        for row in graph:
            if sum(row) % 2 != 0:
                return False
        return True

    def backtrack(v, visited_edges, path):
        for u in range(n):
            if graph[v][u] > 0:
                graph[v][u] -= 1
                graph[u][v] -= 1
                visited_edges += 1
 
                path.append(u)
                if backtrack(u, visited_edges, path):
                    return True

                graph[v][u] += 1
                graph[u][v] += 1
                visited_edges -= 1
                path.pop()

        if visited_edges == total_edges:
            return True
        return False

    if not is_valid_graph():
        print("Graf wejściowy nie zawiera cyklu.")
        return

    total_edges = sum(sum(row) for row in graph) // 2
    path = [0]
    if backtrack(0, 0, path):
        print("Cykl Eulera:", path)
    else:
        print("Graf wejściowy nie zawiera cyklu.")



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
            print("Graf wejściowy nie zawiera cyklu.")
            return

    graph = copy.deepcopy(adjlist)
    path = []
    start = next(iter(adjlist))  

    def backtrack(v, visited_edges, path):
        for i in range(len(graph[v])):
            u = graph[v][i]
            if u is None:
                continue
            graph[v][i] = None
            visited_edges += 1
            path.append(u)

            if backtrack(u, visited_edges, path):
                return True

            graph[v][i] = u
            visited_edges -= 1
            path.pop()

        if visited_edges == total_edges:
            return True
        return False

    path.append(start)
    if backtrack(start, 0, path):
        print("Cykl Eulera:", path)
    else:
        print("Graf wejściowy nie zawiera cyklu.")
