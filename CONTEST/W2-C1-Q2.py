# Print all the prime numbers between 1 to 100.

def Isprime(n):
    count = 0
    for i in range(1,n+1):
        if n %i == 0:
            count+=1
    # print("count:", count)
    if count==2:
        return True
    else:
        return False
# print(Isprime(3))    

def print_prime(n1, n2):
    for i in range(n1, n2+1):
        # print(i, Isprime(i))
        if Isprime(i):
            print("prime:",i)

print_prime(1, 100)