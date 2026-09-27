### 4. Minimum Exercises to Become Tired

# Given an initial energy `E` and an array `A` of `N` exercises, each exercise reduces your energy by `A[i]`. You become tired when your energy becomes `0` or less.

# Each exercise can be performed **at most 2 times**.

# Find the **minimum number of exercises** needed to become tired. If it is impossible even after performing every exercise twice, return `-1`.

# **Example:**

# ```text
# E = 2
# A = [1, 5, 2]

# Output:
# 1
# ```

# Because performing the exercise that drains `5` energy once makes:

# ```text
# 2 - 5 = -3
# ```

# So only **1 exercise** is needed.

## need to take the high energy drain first so that we can reach 0 or less in minimum number of exercises. 

def solve(E, A):

    A.sort(reverse=True)

    count = 0

    for x in A:

        E -= x
        count += 1

        if E <= 0:
            return count

        E -= x
        count += 1

        if E <= 0:
            return count

    return -1 
    
A=[1,5,2] 
E=2
print(solve(E,A))