# 6/1 6/3 6/5 6/7 ..... 10.057


def pattern(x,n):
    den=1    
    sum=0
    for i in range(0,n):
        sum= sum + x/den
        print(f"6/{den}", end =" " )
        den+=2
    return sum
print(pattern(6,4))       