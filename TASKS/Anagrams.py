"""
Two strings are anagrams if you can make one from the other by rearranging the letters.

Write a function named is_anagram that takes two strings as its parameters. 
Your function should return True if the strings are anagrams, and False otherwise.

For example, the call is_anagram("typhoon", "opython") should 
return True while the call is_anagram("Alice", "Bob") should return False.  
"""
def is_anagram(word1, word2):
    res = False
    for l in word2:
        if l in word1 and word1.count(l) == word2.count(l):
            res = True
        else:
            res = False
    return res

word1, word2 = input().split()
print(is_anagram(word1, word2))