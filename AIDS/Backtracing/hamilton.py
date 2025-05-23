def hamiltonian_cycle_matrix(graph):
    n = len(graph)
    path = [0]  

    def is_valid(v, pos):
        if graph[path[pos - 1]][v] == 0:
            return False
        if v in path:
            return False
        return True

    def backtrack(pos):
        if pos == n:
            return graph[path[-1]][path[0]] == 1  
        for v in range(1, n):
            if is_valid(v, pos):
                path.append(v)
                if backtrack(pos + 1):
                    return True
                path.pop()
        return False

    if backtrack(1):
        return path + [path[0]]  
    else:
        return None

def hamiltonian_cycle_adjlist(graph):
    n = len(graph)
    path = [0]  
    visited = set([0])

    def backtrack():
        if len(path) == n:
            return path[0] in graph[path[-1]]  
        for neighbor in graph[path[-1]]:
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                if backtrack():
                    return True
                path.pop()
                visited.remove(neighbor)
        return False

    if backtrack():
        return path + [path[0]]
    else:
        return None
