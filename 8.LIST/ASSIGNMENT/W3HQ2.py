# Q2. Given two sorted lists, write a Python code to merge them into a single
# sorted list.

l1=[1,2,3,4,5,65,65,65]
l2=[6,7,8,9,55]
i=0
j=0
result=[]
while i<len(l1) and j<len(l2):
    if l1[i]<l2[j]:
        result.append(l1[i])
        i+=1
        # print(result)
    elif l2[j] < l1[i]:
        result.append(l2[j])
        j+=1
    else:
        result.append(l1[i])
        result.append(l2[j])
        i+=1
        j+=1
    
    i+=1


while i < len(l1):
    result.append(l1[i])
    i += 1


while j < len(l2):
    result.append(l2[j])
    j += 1
print(result) 


        


