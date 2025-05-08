

def dfs_sort_matrix(matrix):
    n = len(matrix)
    visited = [0] * (n+1)  
    result = []
    has_cycle = False

    def dfs(u):
        nonlocal has_cycle
        if visited[u] == 1:
            has_cycle = True
            return
        if visited[u] == 2:
            return
        visited[u] = 1
        for v in range(1, n):
            if matrix[u][v]:
                dfs(v)
        visited[u] = 2
        result.append(u)

    for i in range(1, n):
        if visited[i] == 0:
            dfs(i)

    if has_cycle:
        print("DFS sort: Graf zawiera cykl!")
        return None
    return result[::-1]


def dfs_sort_gmatrix(matrix, V):
    n = len(matrix)
    visited = [0] * (n + 1)
    result = []
    has_cycle = False

    def dfs(u):
        nonlocal has_cycle
        if visited[u] == 1:
            has_cycle = True
            return
        if visited[u] == 2:
            return
        visited[u] = 1
        for v in range(1, n):
            val = matrix[u][v]
            if 1 <= val <= V:
                dfs(v)

        visited[u] = 2
        result.append(u)

    for i in range(1, n):
        if visited[i] == 0:
            dfs(i)

    if has_cycle:
        print("DFS sort: Graf zawiera cykl!")
        return None
    return result[::-1]

def kahn_sort_matrix(matrix):
    n = len(matrix)
    in_degree = [0] * n
    for u in range(n):
        for v in range(n):
            if matrix[u][v]:
                in_degree[v] += 1

    queue = [i for i in range(n) if in_degree[i] == 0]
    result = []

    while queue:
        u = queue.pop(0)
        result.append(u)
        for v in range(n):
            if matrix[u][v]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

    if len(result) != n:
        print("Kahn sort: Graf zawiera cykl!")
        return None
    return result[1:]


def kahn_sort_gmatrix(matrix, V):
    n = len(matrix)
    in_degree = [0] * n

    for u in range(1, n):
        for v in range(1, n):
            val = matrix[u][v]
            if 1 <= val <= V:
                in_degree[v] += 1  
            elif V + 1 <= val <= 2 * V:
                in_degree[u] += 1  

    queue = [i for i in range(1, n) if in_degree[i] == 0]
    result = []

    while queue:
        u = queue.pop(0)
        result.append(u)
        for v in range(1, n):
            val = matrix[u][v]
            if 1 <= val <= V:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
            elif V + 1 <= val <= 2 * V:
                in_degree[u] -= 1
                if in_degree[u] == 0:
                    queue.append(u)

    if len(result) != n - 1: 
        print("Kahn sort: Graf zawiera cykl!")
        return None
    return result
