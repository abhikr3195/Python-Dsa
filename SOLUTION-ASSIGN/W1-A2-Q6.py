"""
Ask 4 numbers from user. Make sure all the numbers entered by user are dierent. 
Print which number is the smallest.
"""

num1 = int(input("enter the num1:"))
num2 = int(input("enter the num2:"))
num3 = int(input("enter the num3:"))
num4 = int(input("enter the num4:"))
small=num1
if num2<small:
    small=num2
if num3<num2:
    small=num3
if num4<num3:
    small=num4
print(small)