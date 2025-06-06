age = 28

print("adult") if age >= 18 else print("child")

#what value to add?
my_list=[f"{i}-even" if i%2==0 else f"{i}-odd" for i in range(1,11)]
print(my_list)


#when to add? we never use else in this condition
my_list2=[i for i in range(1,11) if i%2==0]
print(my_list2)