#make your own list.
# write a python code that takes an integer as an input, 
# and make a new list containing the last n elements of the original list.
# using slicing login

a=[1,2,4,3,7,65,8]
n=int(input("enter the number: "))
new_list=a[-n:]
print(new_list)