# First Non-Repeating Character
# Question

# Given a string s, find and return the first character that occurs only once.

# Example:

# s = "swiss"

# Character frequencies:

# s → 3
# w → 1
# i → 1

# The first character occurring once is:
# w 

def first_non_repeating(s):
    freq = {}

    for ch in s:
        if ch not in freq:
            freq[ch] = 0
        freq[ch] += 1

    for ch in s:
        if freq[ch] == 1:
            return ch

    return -1


s = "swiss"
print(first_non_repeating(s)) 

# Output
# w
# Complexity
# Time: O(n) — two traversals of the string
# Space: O(k) — k = number of distinct characters
# Approach

# HashMap / Dictionary + Two Traversals

# First traversal → count each character
# Second traversal → find the first character with count = 1