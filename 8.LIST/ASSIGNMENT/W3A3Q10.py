# Q10. Create a function updateOddEven that accepts an List of Integers
# and update all the even numbers to increment by 1 and update all the odd
# numbers to decrement by 1.

def updateOddEven(my_list):
    for i in range(len(my_list)):
        if my_list[i]%2==0:
            my_list[i]+=1
        else:
            my_list[i]-=1
    return my_list
my_list=[12,23,34,43,54,67,79]
print(updateOddEven(my_list))