from collections import defaultdict

def build_adjacency_matrix(n, edges):
    matrix = [[0] * (n+1) for _ in range(n+1)]
    for u, v in edges:
        matrix[u][v] = 1
    return matrix


def build_graph_matrix(n, edges):
    matrix = [[0 for idx in range(n+5)] for jdx in range(n+1)]
    vertices = set([u for u, v in edges] + [v for u, v in edges])
    adj_list = defaultdict(list)
    pred_list = defaultdict(list)
    nonincident = {}
    cycle_list, bool_cycle_list = find_cycles_double(edges)

    for u, v in edges:
        if u != v and v not in cycle_list[u]:
            adj_list[u].append(v)
        if u != v and u not in cycle_list[v]:
            pred_list[v].append(u)

        adj_list[u].sort()
        pred_list[v].sort()

    for v in vertices:
        nonincident[v] = []
        for u in vertices:
            if (v, u) not in edges and (u, v) not in edges:
                nonincident[v].append(u)

    for vi in range(1, n+1):
        if vi not in adj_list or adj_list[vi] == []:
            adj_list[vi] = [0]
        
        if vi not in pred_list or pred_list[vi] == []:
            pred_list[vi] = [0]
        
        if vi not in cycle_list or cycle_list[vi] == []:
            cycle_list[vi] = [0]

        if vi not in nonincident or nonincident[vi] == []:
            nonincident[vi] = [0]
    
    for vi in range(1, n+1):
        if len(adj_list[vi]) == 0:
            adj_list[vi] = [0]
    
    index_nonincident = {key: 1 for key in nonincident}
    index_adj = {key: 1 for key in adj_list}
    index_pred = {key: 1 for key in pred_list}
    
    for vi in range(1, n+1):
        
        matrix[vi][n+1] = adj_list[vi][0] if len(adj_list[vi]) > 0  else 0
        matrix[vi][n+2] = pred_list[vi][0] if len(pred_list[vi]) > 0 else 0
        matrix[vi][n+3] = nonincident[vi][0] if len(nonincident[vi]) > 0 else 0
        matrix[vi][n+4] = cycle_list[vi][0] if (vi in cycle_list and len(cycle_list[vi]) > 0) else 0
        indexB = 0   

        for vj in range(1, n+1):
            
            vi_vj = False
            vj_vi = False

            if (vi, vj) in edges:
                vi_vj = True
            if (vj, vi) in edges:
                vj_vi = True

            if vi_vj:
                index = index_adj[vi]
                matrix[vi][vj] = adj_list[vi][index] if index < len(adj_list[vi]) else adj_list[vi][-1]
                index_adj[vi] += 1

            elif vj_vi:
                index = index_pred[vi]
                matrix[vi][vj] = pred_list[vi][index] + n if index < len(pred_list[vi]) else pred_list[vi][-1] + n
                index_pred[vi] += 1

            elif not vi_vj:
                index = index_nonincident[vi]
                matrix[vi][vj] = -nonincident[vi][index] if index < len(nonincident[vi]) else -nonincident[vi][-1]
                index_nonincident[vi] += 1

            if bool_cycle_list[(vi, vj)]:
                matrix[vi][vj] = cycle_list[vi][indexB] + 2*n if indexB < len(cycle_list[vi]) else cycle_list[vi][-1] + 2*n

            indexB += 1
            
    return matrix


def find_cycles_double(edges):
    cycle_list = defaultdict(list)
    bool_list = defaultdict(list)
    for u, v in edges:
        if (v, u) in edges:
            cycle_list[u].append(v)
            bool_list[(v, u)] = True
    return cycle_list, bool_list


def find_reverse_edge(edges, start):
    all = []
    for u, v in edges:
        if v == start: 
            all.append(u)
    return all

def dfs(edges, start, target, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    
    if start == target:
        return True  

    for u, v in edges:
        if u == start and v not in visited:
            if dfs(edges, v, target, visited):  
                return True

    return False

def find_cycles(edges):
    cycles = {}

    for u, v in edges:
        reverse = find_reverse_edge(edges, u)  
        if len(reverse) > 0:
            for z in reverse:
                if dfs(edges, u, z):
                    if u not in cycles:
                        cycles[u] = []
                    cycles[u].append(z)

    return cycles


