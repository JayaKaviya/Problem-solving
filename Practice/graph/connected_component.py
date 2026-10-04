# Connected Components
# 1. Question

# Given an undirected graph, find the number of separate groups of connected nodes.

# For example:

# 0 ─── 1       2 ─── 3       4

# There are 3 separate groups:

# Component 1 → {0, 1}

# Component 2 → {2, 3}

# Component 3 → {4}

# So the answer is:

# 3
# What is a connected component?

# A connected component is one group where you can travel from one node to another through the graph.

# For example:

# 0 ─── 1

# 0 and 1 belong to the same component because they are connected.

# But:

# 0 ─── 1       2 ─── 3

# There is no connection between 1 and 2, so they are two different components. 


def dfs(graph, node, visited):
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


graph = {
    0: [1],
    1: [0],
    2: [3],
    3: [2],
    4: []
}

visited = set()
count = 0

for node in graph:
    if node not in visited:
        dfs(graph, node, visited)
        count += 1

print(count) 

# Output:

# 3 


# Logic:

# Start with an empty visited set.
# Check every node.
# If a node is unvisited, start DFS from it.
# That DFS visits one entire component, so increase count by one.
# Continue until all nodes are visited.

# Complexity

# Time
# O(V+E)

# Space
# O(V)

# This version assumes an undirected graph.
# For a directed graph, the meaning of components needs to be specified—for example, strongly connected components.