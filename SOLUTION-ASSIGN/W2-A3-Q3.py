"""
Create a function named multiplicationTable that takes an integer
num as an argument. Print the multiplication table of that number up to 10
numbers.
"""

def multiplocationTable(num:int):
    i=1
    while i<=10:
        # print(num*i,end =" ")
        print(f"{num} X {i} ={num*i}")
        i=i+1
multiplocationTable(3)     
   