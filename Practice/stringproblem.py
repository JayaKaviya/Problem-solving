# You are given a string "number" representing a positive integer and a character digit.
# Return the resulting string after removing exactly one occurrence of digit from number 
# such that the value of the resulting string in decimal form is maximized. 
# The test cases are generated such that digit occurs at least once in the number.
# I/P: number = "1321" digit ="1" O/P: 321 


def remove_digit(number, digit):
    for i in range(len(number) - 1):
        if number[i] == digit and number[i + 1] > digit:
            return number[:i] + number[i + 1:]
        
    #for number is 111, remove last digit
    i = number.rfind(digit)
    return number[:i] + number[i + 1:]