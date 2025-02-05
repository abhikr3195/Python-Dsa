# Q1. Write a Python code to check if a given list is sorted in ascending order.
# You don’t have to change the list. Just output YES if list is sorted else NO.

# l=[5,4,1,2,3]
# def sort(l):
#     for i in range(0,len(l)):
#         for j in range(i+1,len(l)):
#             if l[i]>l[j]:
#                 return False
# l=[5,4,1,2,3]
# print(sort(l))


#alternate method 
def isSort(lst):
    for i in range(0,len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True
lst=[1,2,3,6,5]
print(isSort(lst))
        
