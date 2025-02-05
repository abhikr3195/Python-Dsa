"""
Create a function named pattern which takes an integer as an
input and print the following pattern.

10 20 30 40 50
"""

def pattern(n1):
    i=1
    result = 1
    while i <= n1:
        result = i * 10
        print(result)
        i += 1
    return result    
pattern(4)