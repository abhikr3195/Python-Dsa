# Q3. Write a python program to check if the list contains three consecutive
# common numbers in Python

l=[1,2,3,4,4,4,5,6,7,7,7,9]
for i in range(0,len(l)-2):
    if l[i]==l[i+1] and l[i]==l[i+2] :
        print(l[i], end=" ")
    


