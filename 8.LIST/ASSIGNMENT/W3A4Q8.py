# Q8. Take 10 integer inputs from user and store them in a list. Now, copy all
# the elements in another list but in reverse order.

my_list=[]
for i in range(10):
    num = int(input("Enter the number = "))
    my_list.append(num)
    # print(my_list)
# print(my_list)

# reverse_list=my_list[::-1]
reverse_list=[]

for i in range((len(my_list)-1),-1,-1):
    reverse_list.append(my_list[i])
print(reverse_list)
