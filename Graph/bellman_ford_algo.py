

def bellman_ford(edges_list, n_nodes):
    # edges_list = [(a, b, w)]
    import math
    distances = []
    distances[0] = 0
    for i in range(1, n_nodes):
        distances[i] = math.inf
    for i in range(n_nodes + 1):
        for edge in edges_list:
            a,b,w = edge
            if (i == n_nodes) and distances[b] < distances[a] + w:
                return False, None
            distances[b] = min(distances[b], distances[a] + w)
    return True, distances
        
