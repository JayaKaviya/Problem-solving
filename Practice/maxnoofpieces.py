### Short Question

# Given a string `S`, you can **rearrange its characters in any order** and then split it into the **maximum number of identical contiguous pieces**.

# Find the **maximum number of pieces** possible.

# **Example:**

# ```text
# Input:  ababcc
# Output: 2
# ```

# Because we can rearrange it as:

# ```text
# aabbcc
# ```

# and split it as:

# ```text
# abc | abc
# ```

# So the answer is **2**.

from math import gcd

def solve(s):
    freq = {}

    for ch in s:
        if ch not in freq:
            freq[ch] = 0
        freq[ch] += 1

    answer = 0

    for count in freq.values():
        answer = gcd(answer, count)

    return answer


s = input()
print(solve(s))