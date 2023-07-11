def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}  # Initialize distances to infinity for all nodes
    distances[start] = 0  # Distance from start node to itself is 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                distance = distances[node] + weight

                # Update distance if a shorter path is found
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

    # Check for negative-weight cycles
    for node in graph:
        for neighbor, weight in graph[node].items():
            distance = distances[node] + weight

            if distance < distances[neighbor]:
                raise ValueError("Graph contains negative-weight cycle")

    return distances


# Example usage:
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'C': -1, 'D': 4},
    'C': {'A': 4, 'B': 8, 'D': 3},
    'D': {'B': -1, 'C': 5}
}

start_node = input('Choose from any of the given nodes: \n [A, B, c, D]')
start_node = start_node.upper()

distances = bellman_ford(graph, start_node)

print("Shortest distances from node", start_node + ":")
for node, distance in distances.items():
    print(node, "->", distance)
