from collections import defaultdict

def build_adjacency_matrix(n, edges):
    matrix = [[0] * n for _ in range(n+1)]
    for u, v in edges:
        matrix[u][v] = 1
    return matrix


def build_graph_matrix(n, edges):
    matrix = [[0 for idx in range(n+4)] for jdx in range(n+1)]
    vertices = set([u for u, v in edges] + [v for u, v in edges])
    adj_list = defaultdict(list)
    pred_list = defaultdict(list)
    nonincident = {}

    for u, v in edges:
        adj_list[u].append(v)
        pred_list[v].append(u)
        adj_list[u].sort()
        pred_list[v].sort()
    
    for v in vertices:
        nonincident[v] = []
        for u in vertices:
            if (v, u) not in edges and (u, v) not in edges:
                nonincident[v].append(u)
    


    

    for vi in range(1, n+1):


        index = 1
        matrix[vi][n+1] = adj_list[vi][0] if len(adj_list[vi]) > 0 else 0
        matrix[vi][n+2] = pred_list[vi][0] if len(pred_list[vi]) > 0 else 0
        matrix[vi][n+3] = nonincident[vi][0] if len(nonincident[vi]) > 0 else 0

        for vj in range(1, n+1):
            vi_vj = False
            vj_vi = False
            if (vi, vj) in edges:
                vi_vj = True
            if (vj, vi) in edges:
                vj_vi = True

            if vi_vj:
                matrix[vi][vj] = adj_list[vi][index] if index < len(adj_list[vi]) else adj_list[vi][-1]
            elif vj_vi:
                matrix[vi][vj] = pred_list[vi][index] + n if index < len(pred_list[vi]) else pred_list[vi][-1] + n
            elif not vi_vj:
                matrix[vi][vj] = -nonincident[vi][index] if index < len(nonincident[vi]) else -nonincident[vi][-1]

            index += 1
            
        




    return matrix