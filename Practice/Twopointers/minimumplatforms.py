# ### Minimum Platforms — Question : Not Greedy : Two pointer approach


# > **Given the arrival and departure times of `N` trains at a railway station, 
# find the minimum number of platforms required so that no train has to wait.**
# 
# > A platform cannot be used by another train until the current train has departed.

# Example:

# ```python
# arrival   = [900, 940, 950, 1100, 1500, 1800]
# departure = [910, 1200, 1120, 1130, 1900, 2000]
# ```

# **Output:**

# ```text
# 3
# ```

# Because at one point, **3 trains are present simultaneously**, so 3 platforms are required.

# ### Complexity

# ```text
# Sort arrivals     → O(n log n)
# Sort departures   → O(n log n)
# Two-pointer scan  → O(n)

# Total Time        → O(n log n)
# Space             → O(1) extra
# ```

# If we count the space used by the sorting implementation, 
# it can depend on the language/sorting algorithm, 
# but the algorithm itself uses only the two pointers and counters beyond the input arrays. 


arrival = [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000] 

arrival.sort()
departure.sort() 
platform=0
maxi=0 
i=0
j=0
while i<len(arrival) and j<len(departure):
    
    if arrival[i]<departure[j]:
        platform+=1
        maxi=max(maxi,platform)
        i+=1 
    else:
        platform-=1
        j+=1
