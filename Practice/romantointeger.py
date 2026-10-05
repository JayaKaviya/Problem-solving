# Roman to Integer ⭐⭐⭐⭐

# Question:

# Given a Roman numeral string s, convert it into an integer.

# Example:

# Input:  "MCMXCIV"
# Output: 1994 



# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

total = 0

for i in range(len(s)):

    if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
        total -= values[s[i]]
    else:
        total += values[s[i]]

print(total) 


# Complexity
# Time: O(n) — we go through the string once.
# Space: O(1) — the dictionary always contains only 7 Roman symbols.

# Main logic to remember
# current < next  → subtract
# current >= next → add

# Example:

# IV
# I = 1, V = 5
# 1 < 5 → -1
# 5 → +5

# Answer = 4

