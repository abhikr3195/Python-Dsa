def fact(n1):
    i = 1
    count= 0
    while i <=n1:
        if n1%i==0:
            count = count+1
        i+=1
    return count 
print(fact(7))
number_of_factors=fact(7)
if number_of_factors==2:
    print("prime number")
else:
    print("non prime number")
    

# alterante method
def factors(n: int) -> int:
    i = 1
    count = 0
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count


def isPrime(n: int) -> bool:
    return factors(n) == 2

    # if factors(n) != 2:
    #     return False
    # return True


number = 12
if isPrime(number):
    print("It is a prime")
else:
    print("It is not a prime")

