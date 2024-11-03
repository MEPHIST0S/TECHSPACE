"""
Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True.    
"""
def all_equal(arr):
    res = True
    for i in arr:
        if i == arr[0]:
            res = True
        else:
            res = False
            break
    return res

arr = [1, 1, 1]
print(all_equal(arr))