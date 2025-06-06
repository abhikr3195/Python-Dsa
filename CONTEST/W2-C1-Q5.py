"""
Might not be the best solution but easy to understand
"""

def factorial(num):
    result=1
    for i in range (1,num+1):
        result = result*i
    return result
def sumPattern(num1):
    total=1
    for i in range (num1):
        total= total+(1/factorial(i))
    return total
print(sumPattern(5))
        