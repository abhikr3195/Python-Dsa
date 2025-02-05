def add(n):
    sum=0
    
    for i in range(0,len(str(n))):
        sum= sum +  n % 10
        n = int(n/10)
    return sum
print(add(1234))