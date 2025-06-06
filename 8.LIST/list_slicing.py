#list_slicing
a= [1,2,3,4,5,7,8,9]
result=a[1:3] #here  1 and 3 are the index ,[included-start:exclude-stop]
print(result)

print(f"ID for a= {id(a)}")
print(f"ID for result= {id(result)}")


result1=a[0:6:3] # start-include:stop-exlude:step
print(result1)