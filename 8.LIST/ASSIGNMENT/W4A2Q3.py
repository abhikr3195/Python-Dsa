#write a python code to generate a list of prime numbers less than 500 using list comprehension

# def checkPrime(number):
#     factor=0
#     for i in range(0,number+1):
#         if number%i==0:
#             factor+=

def isPrime(num):
    if num<2:
        return False
    for i in range(0,num):
        if num%2==0:
            return False
    return True

prime=[num for num in range(500) if isPrime(num)]
print(prime)