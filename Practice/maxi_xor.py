### Short Question

# **Given an array of `N` elements (`N` is even), choose at most `N/2` elements such that their XOR is maximum. Return the maximum possible XOR.**

# **Example:**

# ```text
# Input:  [1, 2, 4, 7]
# Output: 7
# ```

# Because `7` can be selected alone, and `7` is the maximum possible XOR.



def solve(A):
    n = len(A)
    limit = n // 2

    # dp[k] = all XOR values possible
    # by choosing exactly k elements
    dp = [set() for _ in range(limit + 1)]

    # Choosing 0 elements gives XOR 0
    dp[0].add(0)

    for num in A:

        # Go backwards so that the same number
        # is not used more than once
        for k in range(limit - 1, -1, -1):

            for x in dp[k]:

                new_xor = x ^ num

                dp[k + 1].add(new_xor)

    answer = 0

    # We can choose 0, 1, 2, ..., limit elements
    for k in range(limit + 1):
        for x in dp[k]:
            answer = max(answer, x)

    return answer


A = [1, 2, 4, 7]

print(solve(A))