# 1.Given an undirected graph, determine whether the graph contains a cycle.
# Return True if a cycle exists, otherwise return False.

# Example:

#     0
#    / \
#   1---2

# There is a cycle:

# 0 → 1 → 2 → 0 

def has_cycle(graph, node, visited, parent):
    visited.add(node)

    for neighbor in graph[node]:

        if neighbor not in visited:
            if has_cycle(graph, neighbor, visited, node):
                return True

        elif neighbor != parent:
            return True

    return False


graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}

visited = set()
cycle = False

for node in graph:
    if node not in visited:
        if has_cycle(graph, node, visited, -1):
            cycle = True
            break

print(cycle) 

# Output:
# True 

# Complexity

# Let:

# V = number of vertices
# E = number of edges

# Time: O(V + E)

# Space: O(V)

#---------------------------------
# UNDIRECTED
# DFS + visited + parent

# DIRECTED
# DFS + visited + path  

#---------------------------------- 

# Directed Graph — Cycle Detection
# Question

# Given a directed graph, determine whether the graph contains a cycle. Return True if a cycle exists, otherwise return False.

# Example:

# 0 → 1 → 2
#     ↑   ↓
#     └───┘

# There is a cycle:

# 1 → 2 → 1 

def has_cycle(graph, node, visited, path):
    visited.add(node)
    path.add(node)

    for neighbor in graph[node]:

        if neighbor not in visited:
            if has_cycle(graph, neighbor, visited, path):
                return True

        elif neighbor in path:
            return True

    path.remove(node)

    return False


graph = {
    0: [1],
    1: [2],
    2: [1]
}

visited = set()
path = set()
cycle = False

for node in graph:
    if node not in visited:
        if has_cycle(graph, node, visited, path):
            cycle = True
            break

print(cycle) 

# Output
# True
# Complexity
# Time: O(V + E)
# Space: O(V)

# Where:

# V = number of vertices/nodes
# E = number of directed edges
# Remember this pattern
# Directed graph cycle
#         ↓
#        DFS
#         ↓
# visited + path
#         ↓
# neighbor already in path?
#         ↓
#       Cycle