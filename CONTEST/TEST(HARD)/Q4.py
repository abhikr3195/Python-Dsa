def armstong(n):
    total=0
    temp=n
    while temp!=0:
        last_digit=temp%10
        total=total+(last_digit**3)
        temp=temp//10    
    if total==n:
        return True
    else:
        return False
print(armstong(407))