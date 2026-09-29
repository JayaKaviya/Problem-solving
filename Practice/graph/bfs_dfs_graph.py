#     0
#   / \
#   1   2
#  / \
# 3   4

#in ADJACENT LIST representation
graph={ 
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]  
} 

#BFS  traversal on adjacent list 
print("BFS")

from collections import deque 

q=deque([0]) 
visited=set() 
visited.add(0) 

while q:
    node=q.popleft()
    print(node,end="->") 
    for x in graph[node]:   
        if x not in visited:
            visited.add(x)
            q.append(x) 
             
# 0->1->2->3->4->


#DFS  traversal on adjacent list  
print("\nDFS")

visited=set() 

def dfs(node): 
   visited.add(node) 
   print(node,end="->") 
   
   for x in graph[node]:
       if x not in visited:
           visited.add(x)
           dfs(x)
dfs(0) 

# 0->1->3->4->2

# Time  = O(V + E)
# Space = O(V)







