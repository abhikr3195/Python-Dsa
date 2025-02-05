"""Ask M and N from user


    M to N
    
    N to M
    
    M = 5
    N = 9
    5 6 7 8 9
    
    M = 9
    N = 3
    3456789
    
"""

m = int(input("enter the number: "))
n = int(input("enter the number: "))
if m>n:
    i=n
    while i<=m:
        print(i)
        i=i+1
else:
    i=m
    while i<=n:
        print(i)        
        i=i+1