#make your own list.
# write a python code that takes an integer as an input, 
# and make a new list containing the last n elements of the original list.
# using slicing login but in reverse order

a=[1,2,3,4,5,67,7]
n=int(input("enter the number: "))
new_list=a[:n:-1]
print(new_list)