# Q5. Write a program to put all the common elements (in 2 lists) in another
# list and print it using function.

def common(a,b):
    c=[]
    for i in range(0,len(a)):
        if a[i] in b:
            c.append(a[i])
    return c
a=[1,2,3,4,5]
b=[2,3,4,5,]
print(common(a,b))



