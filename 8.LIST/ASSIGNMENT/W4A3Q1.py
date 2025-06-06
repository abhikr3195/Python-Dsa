# Q1. Write a Python program to get the 4th element from the last element
# of a tuple.

# a=(1,2,3,4,5,6,7)
# result=a[-4]
# print(result)
from typing import Tuple
def fourthElementFromLast(tup:tuple):
    if len(tup)<4:
        print("not enough elemnts")
        return
    else:
        print(tup[-4])
fourthElementFromLast((1,2,3,4,5,6,7))

