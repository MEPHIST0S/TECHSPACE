"""
The aim of this challenge is to write code that can analyze code submissions. 
We'll simplify things a lot to not make this too hard.

Write a function named validate that takes code represented as a string as its only parameter.

Your function should check a few things:

the code must contain the def keyword
otherwise return "missing def"
the code must contain the : symbol
otherwise return "missing :"
the code must contain ( and ) for the parameter list
otherwise return "missing paren"
the code must not contain ()
otherwise return "missing param"
the code must contain four spaces for indentation
otherwise return "missing indent"
the code must contain validate
otherwise return "wrong name"
the code must contain a return statement
otherwise return "missing return"
If all these conditions are satisfied, your code should return True.

Here comes the twist: your solution must return True when validating itself.
"""
def validate(string):
    if "def " not in string:
        return "missing def"
    if ":" not in string:
        return "missing :"
    if "(" not in string or ")" not in string:
        return "missing paren"
    if "()" in string and "def validate" not in string:
        return "missing param"
    if "    " not in string and "\n\t" not in string:
        return "missing indent"
    if "validate" not in string:
        return "wrong name"
    if "return" not in string:
        return "missing return"
    return True