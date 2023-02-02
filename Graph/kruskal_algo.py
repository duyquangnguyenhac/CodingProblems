from union_find_algo import UnionFind

def kruskal(edges_list, n_nodes):
    # Edges_list = [(a, b, w)]
    union_find = UnionFind(n_nodes)
    sorted_edges_list = sorted(edges_list, key= lambda x: x[2])
    spanning_tree_edges = []
    for a, b, w in sorted_edges_list:
        if not union_find.same(a, b):
            spanning_tree_edges.append((a, b, w))
            union_find.union(a, b)
            # Terminate early if we already form a spanning tree
            if union_find.size(a) == n_nodes:
                return spanning_tree_edges
    return spanning_tree_edges
    

