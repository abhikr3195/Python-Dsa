# Q1. Make a list of your own. Make two more empty list like odd and even.
# Put all the even numbers from original list to even and odd numbers to
# odd and print both lists. (Don’t remove anything from original one).
from typing import List

def oddEvelList(my_list): 
    a=[]
    b=[]
    for i in range(0,len(my_list)):
        if my_list[i]%2==0:
            a.append(my_list[i])
        else:
            b.append(my_list[i])
    return a,b
my_list=[12,22,33,45,65,76,88,100]
print(oddEvelList(my_list))
