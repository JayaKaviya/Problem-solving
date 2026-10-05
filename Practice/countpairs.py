# Count Pairs Whose Sum Is Divisible by T

# Given an array C and an integer T, count the number of distinct pairs (i, j) where:
# (C[i] + C[j]) % T == 0

# Each element can be used only once in a pair.
# Example
# C = [2, 4, 1, 3, 5]
# T = 3

# Valid pairs:
# 2 + 4 = 6   ✅
# 2 + 1 = 3   ✅
# 4 + 5 = 9   ✅
# 1 + 5 = 6   ✅

# Answer:
# 4 


def count_pairs(C, T):
    freq = {}
    count = 0

    for x in C:
        rem = x % T
        need = (T - rem) % T

        if need in freq:
            count += freq[need]

        if rem not in freq:
            freq[rem] = 0

        freq[rem] += 1

    return count


C = [2, 4, 1, 3, 5]
T = 3

print(count_pairs(C, T)) 

# Output:
# 4 

# Approach: HashMap + Remainder Matching
# Time: O(n)
# Space: O(T)


# 3. Logic

# For every current number:

# Step 1 — Find its remainder
# rem = x % T

# Example:

# x = 4
# 4 % 3 = 1

# So rem = 1.

# Step 2 — Find the required remainder
# need = (T - rem) % T

# For rem = 1:

# need = (3 - 1) % 3
#      = 2

# Meaning:

# I need a previous number whose remainder is 2.

# Step 3 — Check previous numbers

# freq stores how many previous numbers have each remainder.

# count += freq[need]

# If:

# freq[2] = 1

# there is one valid previous number.

# If:

# freq[2] = 5

# there are five valid pairs with the current number.

# Step 4 — Store the current remainder
# freq[rem] += 1

# This allows future numbers to pair with the current number.

