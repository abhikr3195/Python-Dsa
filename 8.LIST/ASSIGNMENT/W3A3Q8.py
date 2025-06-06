# Q8. Create a function findSmallest that accepts an List of Integers and
# returns the smallest number from the list.

def findSmallest(my_list):
    smallest=my_list[0]
    for i in range(len(my_list)):
        if my_list[i] < smallest:
            smallest=my_list[i]
    return smallest
my_list=[12,44,32,55,88,76,13]
print(findSmallest(my_list))
