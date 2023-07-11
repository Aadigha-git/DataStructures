import sys
from itertools import combinations


def tsp(graph):
    n = len(graph)
    dp = {}

    # Function to compute the cost of the optimal TSP tour
    def tsp_dp(mask, pos):
        if (mask, pos) in dp:
            return dp[(mask, pos)]

        if mask == (1 << n) - 1:
            return graph[pos][0]

        ans = sys.maxsize

        for i in range(n):
            if (mask >> i) & 1 == 0:
                new_mask = mask | (1 << i)
                cost = graph[pos][i] + tsp_dp(new_mask, i)
                ans = min(ans, cost)

        dp[(mask, pos)] = ans
        return ans

    # Compute the cost of the optimal TSP tour starting from node 0
    optimal_cost = tsp_dp(1, 0)

    # Reconstruct the optimal TSP tour
    path = [0]
    mask = 1

    while len(path) < n:
        next_node = None
        for i in range(n):
            if (mask >> i) & 1 == 0:
                if next_node is None or graph[path[-1]][i] < graph[path[-1]][next_node]:
                    next_node = i

        path.append(next_node)
        mask |= (1 << next_node)

    path.append(0)  # Return to the starting node

    return optimal_cost, path


# Example usage:
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

optimal_cost, optimal_path = tsp(graph)

print("Optimal TSP Cost:", optimal_cost)
print("Optimal TSP Path:", optimal_path)
