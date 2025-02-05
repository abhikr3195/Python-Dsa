a=[23,"abhi",44,-100,11.23,False]
b=a
print("A->",a,id(a))
print("B->",b,id(b))
b[-1]=9999
print("A->",a,id(a))
print("B->",b,id(b))
