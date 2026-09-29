# Sliding Window

## The Sliding Window Template

The main thing to remember:

> **First identify whether the window size is fixed or variable.**

---

# 1. Fixed-Size Window

### When to use?

When the question says:

* exactly `K` elements
* subarray of size `K`
* substring of length `K`
* every window of size `K`

Think:

```text
FIXED WINDOW
```

### Template

```python
window = sum(arr[:k])
answer = window

for i in range(k, len(arr)):
    window += arr[i]
    window -= arr[i - k]

    answer = max(answer, window)
```

### Example

**Find the maximum sum subarray of size `K`.**

```python
arr = [2, 1, 5, 1, 3, 2]
k = 3
```

Windows:

```text
[2, 1, 5] → 8
[1, 5, 1] → 7
[5, 1, 3] → 9
[1, 3, 2] → 6
```

Answer:

```text
9
```

### Complexity

```text
Time  = O(n)
Space = O(1)
```

---

# 2. Variable-Size Window

### When to use?

When the question says:

* longest subarray satisfying a condition
* shortest subarray satisfying a condition
* longest substring satisfying a condition
* at most `K`...
* minimum/maximum window satisfying a condition

Think:

```text
VARIABLE WINDOW
```

### Basic Template

```python
left = 0

for right in range(len(arr)):

    # Add arr[right]

    while window_is_invalid:

        # Remove arr[left]
        left += 1

    # Current window is valid
```

The window is:

```text
[left ... right]
```

Its length is:

```python
right - left + 1
```

---

# 3. Variable Window — Longest

When the question asks:

> Find the **longest** valid subarray/substring.

Use:

```python
answer = max(answer, right - left + 1)
```

### Example

> Find the longest subarray containing at most `K` zeros.

```python
arr = [1, 1, 0, 0, 1, 0, 1]
k = 2
```

The window must always contain:

```text
at most 2 zeros
```

When it contains more than 2:

```python
while zeros > k:
```

move `left` forward.

---

# 4. Variable Window — Count

When the question asks:

> How many subarrays/windows satisfy the condition?

After making the current window valid:

```python
count += right - left + 1
```

### Why?

If the current valid window is:

```text
[left ... right]
```

then there are:

```text
right - left + 1
```

valid subarrays ending at `right`.

### Example

```text
Window:

[1, 2, 1]
 ↑     ↑
left  right
```

Length:

```text
right - left + 1 = 3
```

So there are 3 valid subarrays ending at `right`:

```text
[1, 2, 1]
[2, 1]
[1]
```

---

# 5. Important Sliding Window Patterns

## Pattern 1 — Maximum Sum Subarray of Size K

**Type:** Fixed Window

Question:

> Find the maximum sum of a subarray of exactly `K` elements.

Think:

```text
exactly K
     ↓
FIXED WINDOW
```

---

## Pattern 2 — Longest Substring Without Repeating Characters

**Type:** Variable Window + Set

Question:

> Find the longest substring containing no repeated characters.

Think:

```text
longest
+
no duplicates
     ↓
VARIABLE WINDOW + SET
```

Example:

```text
"abcabcbb"
```

Answer:

```text
3
```

because:

```text
"abc"
```

is the longest substring without repeated characters.

---

## Pattern 3 — Longest Subarray With At Most K Distinct Elements

**Type:** Variable Window + Frequency Map

Question:

> Find the longest subarray containing at most `K` different numbers.

Example:

```python
arr = [1, 2, 1, 2, 3]
k = 2
```

Longest valid subarray:

```text
[1, 2, 1, 2]
```

It contains only:

```text
1, 2
```

So:

```text
Answer = 4
```

Think:

```text
at most K distinct
        ↓
Frequency Map
```

---

## Pattern 4 — Longest Subarray With At Most K Zeros

**Type:** Variable Window + Condition

Question:

> Find the longest subarray containing at most `K` zeros.

Example:

```python
arr = [1, 1, 0, 0, 1, 0, 1]
k = 2
```

We only need to count zeros:

```python
zeros = 0
```

Think:

```text
at most K zeros
      ↓
count zeros
```

No frequency map is required.

---

## Pattern 5 — Count Subarrays/Windows Satisfying a Condition

**Type:** Sliding Window + Count

Question:

> Count how many valid subarrays/windows exist.

After making the window valid:

```python
count += right - left + 1
```

Think:

```text
COUNT valid windows
        ↓
right - left + 1
```

---

# Fixed vs Variable Window

This is the most important distinction.

```text
"size K"
    ↓
FIXED-SIZE WINDOW
```

Example:

```text
subarray of exactly 3 elements
```

---

```text
"longest/shortest satisfying a condition"
    ↓
VARIABLE-SIZE WINDOW
```

Example:

```text
longest substring without repeating characters
```

---

```text
"how many satisfying..."
    ↓
COUNT VALID WINDOWS
```

Example:

```text
count subarrays with at most K distinct elements
```

---

# Quick Decision Rule

When you see a sliding-window question, ask these questions:

### Step 1

Does it say **exactly K / size K**?

```text
YES → Fixed Window
```

### Step 2

Does it say **longest/shortest** and give a condition?

```text
YES → Variable Window
```

### Step 3

Does it ask **how many**?

```text
YES → Count Valid Windows
```

### Step 4

What do I need to maintain?

```text
No duplicates
      ↓
Set

Distinct numbers
      ↓
Frequency Map

Number of zeros
      ↓
Simple counter

Sum
      ↓
Running window sum
```

---

# Priority for Infosys SP/DSE Preparation

## MUST KNOW

### 1. Maximum Sum Subarray of Size K

**Fixed Window**

### 2. Longest Substring Without Repeating Characters

**Variable Window + Set**

### 3. Longest Subarray With At Most K Distinct Elements

**Variable Window + Frequency Map**

### 4. Longest Subarray With At Most K Zeros

**Variable Window + Condition**

### 5. Count Subarrays/Windows Satisfying a Condition

**Count + Sliding Window**

These patterns are part of the broader DSA preparation alongside topics such as:

```text
Sliding Window
Prefix Sum
Hashing
Greedy
Dynamic Programming
Trees
Graphs
```

The goal is **not to memorize every individual problem**.

The goal is to recognize the pattern:

```text
EXACTLY K
    ↓
FIXED WINDOW


LONGEST / SHORTEST
    ↓
VARIABLE WINDOW


HOW MANY
    ↓
COUNT VALID WINDOWS
```

## One-Line Memory Trick

> **Fixed size → move the whole window.**
> **Variable size → expand right, shrink left when invalid.**
> **Longest → take maximum window length.**
> **Count → add the number of valid windows ending at `right`.**
