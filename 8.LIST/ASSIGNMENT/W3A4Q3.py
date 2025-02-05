# Q3. Write a Python function that takes two lists and returns True if they
# have at least one common element.

def isCommon(a,b):
    for i in range(0,len(a)):
        if a[i] in b:
            return True
    return False
a=[1,2,3,4,5]
b=[2,6,7,8,9]
print(isCommon(a,b))