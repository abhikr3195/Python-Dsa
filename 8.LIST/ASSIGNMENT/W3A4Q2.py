# Q2. Write a function to remove duplicates from a list and print them.

from typing import List
def removeDup(my_list:int):
    unique=[]
    for i in range(0,len(my_list)):
        if my_list[i] not in unique:
            unique.append(my_list[i])
    return unique
my_list=[1,22,3,4,3,22,4,5,6,7]
print(removeDup(my_list))

    # # for i in range(0,len(my_list)):
    # #     for j in range(i+1,len(my_list)-1):
    # #         if my_list[i] == my_list[j]:
    # #                 my_list.pop(j)
    # temp_list=[]
    # for i in range(len(my_list)):
    #     if my_list[i] not in temp_list:
    #         temp_list.append(my_list[i])

    # print(temp_list)


    
    # # print(my_list)
    # return
    #     # if my_list[i]
    #     #     if my_list[i] not in unique:
    #     #         unique.append(my_list[i])
    # # return unique

        
