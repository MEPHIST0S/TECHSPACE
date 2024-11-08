"""
Write a function named capital_indexes. The function takes a single parameter, which is a string. 
Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
"""
def capital_indexes(word):
    arr = list()
    word_capital = word.upper()
    for letter in range(len(word)):
        for capital in range(len(word)):
            if word[letter] == word_capital[capital]:
                if letter not in arr:
                    arr.append(letter)
    return arr

word = input()
print(capital_indexes(word))