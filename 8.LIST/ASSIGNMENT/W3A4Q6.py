# Q6. Write a program to remove the nth index element from a list using a
# function.
def removeNth(my_list,i):
    my_list.pop(i)
    return my_list
my_list=[1,2,3,4,5,6]

print(removeNth(my_list,2))      