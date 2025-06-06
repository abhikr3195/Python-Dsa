# it is used to create list 
# 1 to 10

# my_list=[]
# for i in range(1,11):
#     my_list.append(i)
# print(my_list)

my_list=[i for i in range(1,11)]
print(my_list)


my_list1=[i%2==0 for i in range(1,11)]
print(my_list1)

my_list2=[i for i  in range(10,-1,-1)]
print(my_list2)


#list_comprehension
# my_list = [i%2==0 for i in range(1,11)]
#     what value to add?  
# when to add?
