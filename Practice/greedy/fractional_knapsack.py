# ## Fractional Knapsack — Question

# > You are given `N` items. Each item has a **weight** and a **value**. You also have a bag with a maximum capacity. Find the **maximum total value** that can be placed in the bag.
# >
# > **You are allowed to take a fraction of an item.**

# Example:

# ```text
# weights = [10, 20, 30]
# values  = [60, 100, 120]

# capacity = 50
# ```

# Output:

# ```text
# 240
# ```

# ### Complexity

# ```text
# Calculate value/weight → O(n)
# Sort items            → O(n log n)
# Process items         → O(n)

# Overall Time           → O(n log n)
# Space                  → O(n)
# ```

# **Why O(n log n)?**
# Because the main costly operation is sorting the items by `value / weight`.



# Therefore, there is nothing left to put into the bag, so we use:
# break , once we take the fraction value in else then the bag is full and we break the loop. 

weights = [10, 20, 30]
values = [60, 100, 120]

capacity = 50

items = []

for i in range(len(weights)):
    ratio = values[i] / weights[i]
    items.append((ratio, weights[i], values[i]))

items.sort(reverse=True)

total = 0

for ratio, weight, value in items:

    if capacity >= weight:
        capacity -= weight
        total += value

    else:
        total += ratio * capacity
        break

print(total)