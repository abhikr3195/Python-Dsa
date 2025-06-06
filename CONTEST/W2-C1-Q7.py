def checkPrime(n):
    factors=0
    for i in range(1,n+1):
        if n%i==0:
            factors+=1
    if factors==2:
        return True
    else:
        return False
# print(checkPrime(3))
def printPrime(n1,n2):
    for i in range(n1,n2+1):
        if checkPrime(i)==True:
            print(i)
    
printPrime(1,100) 

    