def dfs_recursive(graph, start, visited=None, traversal_order =None):
    if visited is None:
        visited = set()
    if traversal_order is None:
        traversal_order = []


    visited.add(start)
    traversal_order.append(start)  # Process the node (print, append to result list, etc.)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, traversal_order)

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

order = dfs_recursive(graph, start_node)
print("The order of DFS traversal for the graph is:", ' '.join(order))