"""
The goal of this challenge is to analyze a binary string consisting of only zeros and ones. 
Your code should find the biggest number of consecutive zeros in the string. 
For example, given the string:

"1001101000110"
The biggest number of consecutive zeros is 3.

Define a function named consecutive_zeros that takes a single parameter, 
which is the string of zeros and ones. Your function should return the number described above.    
"""
def consecutive_zeros(num):
    res = 0
    arr = num.split("1")
    print(arr)
    for i in arr:
        if len(i) > res:
            res = len(i)
    return res

num = "1001101000110"
print(consecutive_zeros(num))