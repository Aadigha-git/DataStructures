import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  # Initialize distances to infinity for all nodes
    distances[start] = 0  # Distance from start node to itself is 0

    heap = [(0, start)]  # Heap to store nodes based on their distances
    heapq.heapify(heap)

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        # Skip if the current distance is already greater than the recorded distance
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Update distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 4, 'B': 1, 'D': 3},
    'D': {'B': 4, 'C': 3}
}

start_node = input('Choose from any of the given nodes: \n [A, B, c, D]')
start_node = start_node.upper()

distances = dijkstra(graph, start_node)

print("Shortest distances from node", start_node + ":")
for node, distance in distances.items():
    print(node, "->", distance)
