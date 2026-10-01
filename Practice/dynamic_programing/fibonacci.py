# Yes, Jaya! Your previous approach using the `dp` list is DP, too. 

## 1. First approach — DP using a list

n = 6
dp = [0] * (n + 1)

dp[0] = 0
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])


# Approach 1: DP list

# Stores all calculated answers.
# Time: O(n) · Space: O(n)

## 2. Second approach — DP using variables
 
n = 6

if n == 0:
    print(0)
else:
    a = 0
    b = 1

    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c

    print(b)

# Approach 2: Space-optimized DP
# Stores only the two answers needed next.
# Time: O(n) · Space: O(1)
