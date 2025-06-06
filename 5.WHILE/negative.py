"""
Ask a number from user = 50
-50 to 50

Ask a number from user = 10
-10 to 10

Ask a number from user = -13
13 to -13

Ask a number from user = -20
20 to -20
"""

number: int = int(input("enter the number: "))
if number>0:
    start= -number
    end= number
    while start <= end:
        print(start,end=" ")
        start = start + 1    
else:
    start= -number
    end= number
    while start >= end:
        print(start,end=" ")
        start -= 1
    
    
    str1="AbCdEF"
output = ""
for i in str1:
    asci = ord(i)
    if asci>=65 and asci<=90:
        output = output + chr(asci+32)
    else:
        output = output + i
print(output)