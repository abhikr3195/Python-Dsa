# Create a function named as checkPrime that takes an integer as an
# argument. Print YES if the number passed is a prime number else print NO


def Isprime(n):
    count = 0
    for i in range(2,n+1):
        if n %i == 0:
            count+=1
    if count==2:
        print("no")
    else:
        print("yes")
Isprime(13)