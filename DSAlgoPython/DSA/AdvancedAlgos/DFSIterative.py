# Depth first search is a graph traversal algorithms 
# Algorithm to visit every vertex of graph

# We know if we have traversed every vertex of the graph if we come back to the vertex we started from

# Stacks are used in iteration
# initialise stack with just the starting vertex 
# while stack is not empty we will pop of the last vertex of the stack
# visit the vertex if not visited and mark it as visited

def dfs_iterative(graph, start):
    visited = set()  # Set to track visited nodes
    stack = [start]  # Stack to keep track of nodes to visit
    traversal_order = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            traversal_order.append(node) # Process the node (print, append to result list, etc.)

            # Add unvisited neighboring nodes to the stack
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal_order

# defining a graph using a dictionary
graph = { "a" : ["c"],
          "b" : ["c", "e", "f"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b", "f"],
          "f" : ["b", "e"]
        } 


start_node = input('Choose from any of the given nodes: \n [a, b, c, d, e, f]')
start_node = start_node.lower()

order = dfs_iterative(graph, start_node)
print("The order of DFS traversal for the graph is:", ' '.join(order))