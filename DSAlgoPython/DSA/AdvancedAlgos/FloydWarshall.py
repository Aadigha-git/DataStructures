def floyd_warshall(graph):
    n = len(graph)
    distances = [[float('inf')] * n for _ in range(n)]

    # Initialize distances with the direct edge weights
    for i in range(n):
        for j in range(n):
            if i == j:
                distances[i][j] = 0
            else:
                distances[i][j] = graph[i][j]

    # Perform dynamic programming
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]

    return distances


# Example usage:
graph = [
    [0, 2, 4, float('inf')],
    [float('inf'), 0, 1, 4],
    [4, -3, 0, 3],
    [float('inf'), -1, -5, 0]
]

distances = floyd_warshall(graph)

print("Shortest distances between nodes:")
for i in range(len(distances)):
    for j in range(len(distances[i])):
        print(f"{i} -> {j}: {distances[i][j]}")
