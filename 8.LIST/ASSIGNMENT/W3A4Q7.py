# Q7. Make two lists of same length and pass it to a function. Return a third
# list where each element is the sum of index.

def sumIndex(l1,l2):
    l3=[]
    length = min(len(l1),len(l2))
    for i in range(0,length):
        l3.append(l1[i]+l2[i])
    if length < len(l1):
        l3.extend(l1[length:len(l1)])
    else:
        l3.extend(l2[length:len(l2)])
    return l3
l1=[1,2,3,4,5]
l2=[6,7,8]
print(sumIndex(l1,l2))