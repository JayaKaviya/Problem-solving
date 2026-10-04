# ## Question: Graph Representation Using an Adjacency List

# Given the number of nodes and a list of edges, represent an undirected graph using an adjacency list.

# Example input:

# Python

# Run

# ```
# n = 5
# edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]
# ```

# ## Code

# Python

# Run

# ```
n = 5
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]

graph = {i: [] for i in range(n)}

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

print(graph)
# ```

# Output:

# ```
# {
#     0: [1, 2],
#     1: [0, 3],
#     2: [0, 3],
#     3: [1, 2, 4],
#     4: [3]
# }
# ```

# ## Complexity

# * Time Complexity: O(V+E) , where V is the number of vertices and E is the number of edges.

# * Space Complexity: O(V+E) to store the adjacency list.

# Remember: For an undirected graph, add both `graph[u].append(v)` and `graph[v].append(u)`.
