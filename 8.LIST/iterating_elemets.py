a=[78,65,44,-100,87,33,31]

for i in range(0,7):
    print(a[i],end =" ")
for i in range(len(a)):
    print(a[i], end=" ")
for i in range(0,len(a)):
    print(a[i], end=" ")
print(a)

# Traverse By Index
for i in range(0,len(a),2):
    print(a[i])

#REVERSE PRINTING
for i in range(-1,-8,-1):
    print(a[i],end=" ")
for i in range(-1,-(len(a)+1),-1):
    print(a[i],end=" ")
for i in range((len(a)-1),-1,-1):  # mostly this is used to reverse
    print(a[i],end= " ")
    
# for i in range(-(len(a)),-1,-1): # ye kuch kyu nhi print kr rha hai
#     print(a[i],end=" ")
    

