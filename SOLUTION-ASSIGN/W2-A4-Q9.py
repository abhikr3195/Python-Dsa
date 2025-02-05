"""
Ask a number from user. Print if that number is prime or not, use functions.
"""
def prime(n1):
    i=1
    count=0
    while i<=n1:
        if n1%i==0:
            count += 1
        i+=1
    if count == 2:
        print("It is prime")
    else:
        print("it not prime")
prime(34)
        
            
            
