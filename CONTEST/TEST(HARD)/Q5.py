def firstandLast(n):
    total=n%10 #n=123 total =3 
    n//=10 #n=12
    temp=0 # temp=0
    while n!=0: #n=0
        temp=n%10 #temp=1
        n//=10 #0
    total+=temp #3+1
    return total
print(firstandLast(123))