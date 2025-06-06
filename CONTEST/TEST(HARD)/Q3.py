"""
Make a function named printWords which accepts an integer n from
the user. Print the number as words.
"""

def reverse(n):
    num=0
    last_digit=0
    while n>0:
        last_digit= n%10
        num = num * 10 + last_digit
        n = n//10
    return num
print(reverse(123))

def printWords(n):
    reverse_num=reverse(n)
    while reverse_num>0:
        last_digit=reverse_num%10
        if last_digit==0:
            print("zero", end=" ")
        elif last_digit==1:
            print("one", end=" ")
        elif last_digit==2:
            print("two", end=" ")
        elif last_digit==3:
            print("three", end=" ")
        elif last_digit==4:
            print("four", end=" ")
        elif last_digit==5:
            print("five", end=" ")
        elif last_digit==6:
            print("six", end=" ")    
        elif last_digit==7:
            print("seven", end=" ")    
        elif last_digit==8:
            print("eight", end=" ")    
        elif last_digit==9:
            print("nine", end=" ")
        reverse_num=reverse_num//10
        
    print()
        
printWords(123)
        
            