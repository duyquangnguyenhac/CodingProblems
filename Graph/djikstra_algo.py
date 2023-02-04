

def djikstra(adj_list, n_nodes):
    import math
    import heapq as hq
    # adj_list[a] = (b, w)
    distances = []
    processed = set()
    for i in range(n_nodes):
        distances[i] = math.inf
    pqueue = []
    hq.heappush(pqueue, (0, 0))
    while len(pqueue) != 0:
        priority, node = hq.heappop(pqueue)
        if node in processed:
            return True
        processed.add(node)
        for dest, weight in adj_list[node]:
            if (distances[node] + weight < distances[dest]):
                distances[dest] = distances[node] + weight
                hq.heappush(pqueue, (distances[dest], dest))
    return distances

