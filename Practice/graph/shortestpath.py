# Shortest Path in an Unweighted Graph ⭐⭐⭐⭐⭐
# Question

# Given an unweighted graph, a source node, and a destination node, find the minimum number of edges needed to travel from the source to the destination. Return -1 if the destination cannot be reached.

# Recognize it

# Look for:

# Shortest path
# Minimum number of edges
# Minimum number of steps/moves
# Every edge has equal cost

# ➡️ Use BFS. 

# Example
# 0 ── 1 ── 3
#  \       /
#   ── 2 ──

# From 0 to 3:

# 0 → 1 → 3

# or

# 0 → 2 → 3

# Both require 2 edges. 


from collections import deque

def shortest_path(graph, start, end):
    q = deque([(start, 0)])
    visited = set([start])

    while q:
        node, distance = q.popleft()
        if node == end:
            return distance

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append((neighbor, distance + 1))

    return -1


graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

print(shortest_path(graph, 0, 3)) 


# Output
# 2
# Logic
# Start from start with distance 0.
# Put (node, distance) into the queue.
# BFS explores level by level.
# When moving to a neighbor, distance becomes distance + 1.
# The first time we reach end, that distance is the shortest distance.
# visited prevents visiting the same node repeatedly.
# If the queue becomes empty without finding end, return -1.
# Complexity
# Cost	Complexity
# Time	O(V + E)
# Space	O(V)

# Where:

# V = number of vertices/nodes
# E = number of edges/connections

# Memory trick:

# Shortest path + unweighted graph → BFS → Queue.