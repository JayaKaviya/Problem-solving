### Question

# Given a binary string `S`, calculate the **decimal value** represented by the binary string.

# Since the answer can be very large, return the result **modulo `10^9 + 7`**.

# **Example:**

# ```text
# Input:  00111
# Output: 7
# ```

# Because:

# ```text
# 00111₂ = 7
# ```

def solve(n, s, cash, a, b):

    s = list(s)

    def swap_zero():
        i = 0
        j = n - 1

        while i < j and cash_left[0] >= a:

            if s[i] == '0':
                i += 1

            elif s[j] == '0':
                s[i], s[j] = s[j], s[i]
                cash_left[0] -= a
                i += 1
                j -= 1

            else:
                j -= 1

    def flip_one():
        i = 0

        while i < n and cash_left[0] >= b:

            if s[i] == '1':
                s[i] = '0'
                cash_left[0] -= b

            i += 1

    cash_left = [cash]

    if a < b:
        swap_zero()
        flip_one()
    else:
        flip_one()
        swap_zero()

    answer = 0

    # for ch in s:
    #     answer = (answer * 2 + int(ch)) % (10**9 + 7)
    s2="".join(s)
    return int(s2,2) % (10**9+7)

n= 6
s= '111011'
cash= 7
a = 1
b= 3
print(solve(n, s, cash, a, b))