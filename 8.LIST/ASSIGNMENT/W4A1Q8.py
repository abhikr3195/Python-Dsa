# write the python code to split the list into two halves using slicing
#make the list even

def splitList(my_list):
    center=len(my_list)//2
    First_half=my_list[:center]
    Second_half=my_list[center:]
    print(First_half, Second_half) 
my_list=[1,2,3,4,5,6,7,8]
splitList(my_list)