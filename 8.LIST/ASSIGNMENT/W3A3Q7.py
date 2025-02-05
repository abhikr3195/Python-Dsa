# Q7. Create a function findLargest that accepts an List of Integers and
# returns the largest number from the list.

def findLargest(my_list):
    largest=my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > largest:
            largest=my_list[i]
    return largest
my_list=[12,44,32,55,88,76,13]
print(findLargest(my_list))

