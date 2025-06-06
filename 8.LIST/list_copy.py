import copy

a=[23,"abhi",44,[1,2,3],-100,11.23,False]

b=copy.copy(a) #shallow copy
b[1]=9999
print("A->",a,id(a))
print("B->",b,id(b))

# b[]=9999
# print("A->",a,id(a))
# print("B->",b,id(b))

b=copy.deepcopy(a)  # deep copy
b[3][1]=1000
print("A->",a,id(a))
print("B->",b,id(b))





