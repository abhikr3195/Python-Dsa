# Q9. Make a list. Write a simple program for addition of the 2nd element
# from start and 2nd element from the end.

def indexAdd(my_list):
    l2=my_list[1]+my_list[-2]
    return l2
my_list=[1,2,3,4,5,6,7]
print(indexAdd(my_list))