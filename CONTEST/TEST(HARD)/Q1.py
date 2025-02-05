# Q1. Make a function named reverse which accepts an integer n from the
# user. Reverse the number passed as a parameter and return the reverse
# number. Do not use STRINGS.

# example 
#  reverse(19)
 #  output
#  91

def reverse(n:int):
    num=0
    rem=0
    while n>0: 
        rem = n%10
        num= num*10+rem
        n=n//10
    return num
print(reverse(345))

def checkpalindrome(n):
    reversed_num=reverse(n)
    if reversed_num==n:
        return True
    else:
        return False
print(checkpalindrome(123321))



