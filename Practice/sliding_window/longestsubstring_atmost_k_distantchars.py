# Question

# Find the length of the longest substring that contains at most K distinct characters.

# Given:

# s = "eceba"
# k = 2
# Example

# Possible valid substrings with at most 2 distinct characters:

# "e"      → 1 distinct
# "ec"     → 2 distinct
# "ece"    → 2 distinct
# "ba"     → 2 distinct

# The longest is:

# "ece"

# So the output is:

# 3 

s = "eceba"
k = 2

freq = {}

left = 0
maximum = 0

for right in range(len(s)):

    ch = s[right]
    freq[ch] = freq.get(ch, 0) + 1

    while len(freq) > k:
        ch = s[left]

        freq[ch] -= 1

        if freq[ch] == 0:
            del freq[ch]

        left += 1

    maximum = max(maximum, right - left + 1)

print(maximum) 

 
 
#  Time: O(n) average
# Space: O(k)