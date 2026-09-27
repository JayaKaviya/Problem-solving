# ### Coding question

# There are `N` villains standing in a fixed order. There are `M` heroes, and each hero starts with health `H`.

# The heroes fight the villains from left to right.

# * If a hero's current health is **greater than** the villain's health, the villain is defeated and the hero loses that much health.
# * If both healths are **equal**, both the hero and villain are defeated.
# * If the hero's health is **less than** the villain's health, the hero is defeated, but the villain remains and the next hero fights that villain.

# You are allowed to remove villains **only from the front** of the array.

# Find the **minimum number of villains that must be removed** so that all remaining villains can be defeated using at most `M` heroes.

# #### Input

# ```text
# N M H
# V1 V2 V3 ... VN
# ```

# #### Example

# ```text
# 5 1 4
# 1 2 3 1 3
# ```

# #### Output

# ```text
# 3
# ```

# Because after removing the first 3 villains:

# ```text
# [1, 3]
# ```

# one hero with health `4` can defeat them:

# ```text
# 4 → 3 → 0
# ```

# So the minimum number of removals is `3`.
 
 
N, M, H = 4, 4, 3
V = [3, 1, 3, 3]

heroes = 1
used = 0
answer = N

for i in range(N - 1, -1, -1):

    v = V[i]

    if v > H:
        break

    if used + v <= H:
        used = used + v
    else:
        heroes = heroes + 1
        used = v

    if heroes > M:
        break

    answer = i

print(answer)