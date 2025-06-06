# Q10. Ask 10 numbers from the user and put them into the list. Now remove
# all the even numbers from that list

my_list=[]
for i in range(10):
    num=int(input("enter the number ="))
    my_list.append(num)
# print(my_list)

remove_even=[]
# for i in range(len(my_list)):
#     if my_list[i]%2 !=0:
#         remove_even.append(my_list[i])

for i in my_list:
    print(i)
    if i%2 !=0:
        remove_even.append(i)

print(remove_even)

    

