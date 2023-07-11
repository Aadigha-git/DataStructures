import heapq


def prim(graph, start):
    visited = set()
    min_heap = []
    total_weight = 0
    mst_edges = []

    # Add the start node to the visited set
    visited.add(start)

    # Add the edges from the start node to the min heap
    for neighbor, weight in graph[start]:
        heapq.heappush(min_heap, (weight, start, neighbor))

    while min_heap:
        weight, src, dest = heapq.heappop(min_heap)

        if dest not in visited:
            visited.add(dest)
            mst_edges.append((src, dest, weight))
            total_weight += weight

            # Add the edges from the newly visited node to the min heap
            for neighbor, weight in graph[dest]:
                heapq.heappush(min_heap, (weight, dest, neighbor))

    return mst_edges, total_weight


# Example usage:
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 4), ('B', 1), ('D', 3)],
    'D': [('B', 4), ('C', 3)]
}

start_node = input('Choose from any of the given nodes: \n [A, B, C, D]')
start_node = start_node.upper()

minimum_spanning_tree, total_weight = prim(graph, start_node)

print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    src, dest, weight = edge
    print(f"{src} - {dest} : {weight}")

print("Total Weight of MST:", total_weight)
