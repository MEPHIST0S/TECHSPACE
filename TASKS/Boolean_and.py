"""
Define a function named triple_and that takes three parameters and 
returns True only if they are all True and False otherwise.    
"""
def triple_and(a, b, c):
    if a == True and b == True and c == True:
        return True
    else:
        return False

a, b, c = (False, True, True)
print(triple_and(a, b, c))