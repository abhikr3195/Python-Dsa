"""
Make 2 functions.
add() - it will take 3 integers - return the addition

checkOddEven() - it will take 1 integer, check if odd or even
"""

def add(num1:int,num2:int,num3:int):
    total = num1 + num2 + num3
    return total
sum = add(4,5,7)


def OddEven(abc:int):
    if abc%2==0:
        print("Even")
    else:
        print("Odd")
        
print(sum)
OddEven(sum)        
        