# Activity Selection Problem

# You are given N activities. Each activity has a start time and a finish time. 
# Select the maximum number of activities such that no two selected activities overlap.

# Example:

# Start  =  [1, 3, 0, 5, 8, 5]
# Finish =  [2, 4, 6, 7, 9, 9]

# Activities:

# A1 = (1,2)
# A2 = (3,4)
# A3 = (0,6)
# A4 = (5,7)
# A5 = (8,9)
# A6 = (5,9)

# We want:

# Maximum number of non-overlapping activities.

# Greedy approach
# Sort activities by finish time.
# Select the activity that finishes earliest.
# For every next activity:
# If start >= last_finish, select it.
# Otherwise skip it.
# Continue until all activities are checked.

# For this example:

# (1,2) → choose
# (3,4) → choose
# (0,6) → skip
# (5,7) → choose
# (8,9) → choose

# Therefore:

# Answer = 4

# Selected:

# (1,2)
# (3,4)
# (5,7)
# (8,9)




start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9] 


activities=[] 

for i in range(len(start)):   
    activities.append([start[i],finish[i]]) 
    
activities.sort(key=lambda x: x[1]) 

last=-1
count=0

for s,f in activities:
    if s>=last:
        count+=1
        last=f
        
print(count)


# TC:
# Time  : O(n log n)
# Space : O(n) 

# B finishes earlier
#         ↓
# more time remains
#         ↓
# more activities may fit afterward