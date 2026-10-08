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


# You have been given a string S of length N. The given string is a binary string which consists of only 0's and '1's.
# Ugliness of a string is defined as the decimal number that this binary string represents.

# Example:

# "101" represents 5.

# "0000" represents 0.

# "01010" represents 10.

# There are two types of operations that can be performed on the given string.

# Swap any two characters by paying a cost of A coins.

# Flip any character by paying a cost of B coins

# flipping a character means converting a '1'to a 'O'or converting a '0' to a '1'.

# Initially, you have been given coins equal to the value defined in CASH.
# Your task is to minimize the ugliness of the string by performing the above mentioned operations on it. 
# Since the answer can be very large, return the answer modulo 10^9+7.

# Note:

# You can perform an operation only if you have enough number of coins to perform it.

# After every operation the number of coins get deducted by the cost for that operation.

# Input Format

# The first line contains an integer, N, denoting the number of character in the string

# The next line contains a string, S, denoting the the binary string

# The next line contains an integer, CASH, denoting the total number of coins present initially

# Next will contains an integer, A, denoting the cost to swap two characters.

# Then the next line contains an integer, B, denoting the cost to flip a character.

# Constraints

# 1 <= N <= 10^5

# 1< len(S)<= 10^5

# 1<=CASH <=10^5

# 1<=Ax=10^5

# 18×10^5