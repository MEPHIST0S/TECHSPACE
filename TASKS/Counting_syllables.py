"""
Define a function named count that takes a single parameter. The parameter is a string. 
The string will contain a single word divided into syllables by hyphens, such as these:

"ho-tel"
"cat"
"met-a-phor"
"ter-min-a-tor"
Your function should count the number of syllables and return it.

For example, the call count("ho-tel") should return 2.  
"""
def count(string):
    count = 0
    for symbol in string:
        if symbol == "-":
            count += 1
    return count + 1

string = input()
print(count(string))