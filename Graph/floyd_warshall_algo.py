
def floyd_warshal(adj_matrix):
    import math
    n = len(adj_matrix)
    distances = [[math.inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if (i == j): distances[i][j] = 0
            elif adj_matrix[i][j] != -1: distances[i][j] = adj_matrix[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
    return distances 
