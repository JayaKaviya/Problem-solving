# 1.Maximum Non-overlapping Intervals

# Approach used: Greedy + Sorting

# Question

# Given a list of intervals, select the maximum number of non-overlapping intervals.

# An interval [start, end] is non-overlapping with the previous interval if:

# start >= previous_end
# Example
# intervals = [[1,3], [2,4], [3,5], [6,7]]

# We want the maximum number of intervals that do not overlap.

# One possible answer:

# [1,3] → [3,5] → [6,7]

# So the answer is:

# 3 



def maxNonOverlapping(intervals):

    intervals.sort(key=lambda x: x[1])

    count = 0
    previous_end = float('-inf')

    for start, end in intervals:

        if start >= previous_end:
            count += 1
            previous_end = end

    return count


intervals = [[1,3], [2,4], [3,5], [6,7]]

print(maxNonOverlapping(intervals))


# Output:

# 3


# Complexity

# Sorting:

# O(n log n)

# Scanning:

# O(n)

# Overall:

# Time: O(n log n)

# Space: O(1) extra if sorting is done in-place (ignoring the sorting implementation's internal stack/storage).



# Approach
# Greedy + Sorting

# The important idea is:

# Always choose the interval that finishes earliest.

# Why?

# If an interval finishes early, it leaves more space for the remaining intervals.

# So:

# Sort intervals by their end time.
# Pick the first interval.
# For every next interval:
# If its start >= previous_end, select it.
# Update previous_end. 


# 2.Maximum Non-overlapping Intervals → Minimum Removals
# Question

# Given an array of intervals, return the minimum number of intervals that must be removed so that the remaining intervals do not overlap.

# Intervals that touch at a point are considered non-overlapping.

# Example:

# intervals = [[1,2], [2,3], [3,4], [1,3]]

# We can keep:

# [1,2] → [2,3] → [3,4]

# So we keep 3 intervals.

# There are 4 intervals total.

# Therefore:

# minimum removals = total intervals - maximum non-overlapping intervals
# = 4 - 3
# = 1  #LC QUESTION

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:

        intervals.sort(key=lambda x: x[1])

        maximum = 0
        previous_end = float('-inf')

        for start, end in intervals:

            if start >= previous_end:
                maximum += 1
                previous_end = end

        return len(intervals) - maximum 
    
    
# Complexity
# Sorting: O(n log n)
# Loop: O(n)
# Total: O(n log n)
# Extra space: O(1) apart from sorting.
# Remember this formula
# ┌────────────────────────────────────────┐
# │ Minimum removals = Total - Maximum kept│
# └────────────────────────────────────────┘ 

# Example
# [1,2]
# [2,3]
# [3,4]
# [1,3]

# After sorting by end:

# [1,2]
# [2,3]
# [1,3]
# [3,4]

# Select:

# [1,2]  → keep
# [2,3]  → keep
# [1,3]  → remove
# [3,4]  → keep

# Therefore:

# total = 4
# maximum = 3

# answer = total - maximum
#        = 4 - 3
#        = 1