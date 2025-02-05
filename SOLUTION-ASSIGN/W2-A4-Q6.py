"""
Don't create a function, just print the following pattern
1  11  111  1111  11111....n times (Ask n from user)
"""

num = int(input("enter the number"))
i=1
result = 0
while i <= num:
    result = result * 10 + 1
    print(result, end =" ") # 1, 11, 1111
    i +=1 # 1, 2, 3 
