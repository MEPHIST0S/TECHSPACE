"""
Define a function named list_xor. Your function should take three parameters: n, list1 and list2.

Your function must return whether n is exclusively in list1 or list2.

In other words, if n is in both lists or in none of the lists, return False. If n is in only one of the lists, return True.

For example:

list_xor(1, [1, 2, 3], [4, 5, 6]) == True
list_xor(1, [0, 2, 3], [1, 5, 6]) == True
list_xor(1, [1, 2, 3], [1, 5, 6]) == False
list_xor(1, [0, 0, 0], [4, 5, 6]) == False
"""
def list_xor(n, list1, list2):
    if (n in list1) and (n not in list2):
        return True
    elif (n in list2) and (n not in list1):
        return True
    elif (n in list1) and (n in list2):
        return False
    else:
        return False

n, list1, list2 = (1, [1, 2, 3], [4, 5, 6])
print(list_xor(n, list1, list2))