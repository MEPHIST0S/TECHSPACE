"""
The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

For example, consider the following dictionary:

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
In this case, the number of people online is 2.

Write a function named online_count that takes one parameter. 
The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.

Your function should return the number of people who are online.
"""
def online_count(status):
    online_count = 0
    
    for value in status.values():
        if value == "online":
            online_count += 1
    
    return (online_count)

status = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    "Charlie": "offline"
}

print(online_count(status))