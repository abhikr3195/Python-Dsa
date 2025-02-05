def divs(n1,n2):
    i = 1
    count = 0
    while i <= n1:
        if i%n2==0:
            count+= 1
        i+=1
    return count
print(divs(20,2))            