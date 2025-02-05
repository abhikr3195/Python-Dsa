def sumOfDiv(n1:int,n2:int):
    i=1
    total=0
    while i<=n1:
        if i%n2==0:
            total += i
        i+=i
    return total
print(sumOfDiv(50,8))