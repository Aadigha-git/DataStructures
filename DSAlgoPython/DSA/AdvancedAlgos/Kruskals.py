class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1


def kruskal(graph):
    edges = []
    node_to_id = {}
    id_to_node = {}
    num_nodes = 0

    # Convert node names to unique integer identifiers
    for u in graph:
        if u not in node_to_id:
            node_to_id[u] = num_nodes
            id_to_node[num_nodes] = u
            num_nodes += 1
        for v, weight in graph[u]:
            if v not in node_to_id:
                node_to_id[v] = num_nodes
                id_to_node[num_nodes] = v
                num_nodes += 1
            edges.append((weight, node_to_id[u], node_to_id[v]))

    edges.sort()

    uf = UnionFind(num_nodes)
    minimum_spanning_tree = []
    total_weight = 0

    for weight, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            minimum_spanning_tree.append((id_to_node[u], id_to_node[v], weight))
            total_weight += weight

    return minimum_spanning_tree, total_weight


# Example usage:
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 4), ('B', 1), ('D', 3)],
    'D': [('B', 4), ('C', 3)]
}

minimum_spanning_tree, total_weight = kruskal(graph)

print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    u, v, weight = edge
    print(f"{u} - {v} : {weight}")

print("Total Weight of MST:", total_weight)
