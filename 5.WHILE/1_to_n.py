# print 1 to n
#ask n from user


i :int =1
n :int= int(input("enter the number :"))
while i <= n:
    print(i)
    i =i +1
print()   # for gap 
    

def printPattern(n:int):
    i =1
    while i <= n:
        print(i)
        i= i+1
    print() # this will give gave between below two called func
printPattern(10)
printPattern(5)        
