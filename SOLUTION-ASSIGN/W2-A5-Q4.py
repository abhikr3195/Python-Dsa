# 6^1-6^3+6^5-6^7...-272370

def pattern(x,n):
    sum=0
    value=0
    den=1
    for i in range(0,n):
        value =  x**den
        if i%2==0:
            sum = sum + value
            print(f"+ 6^{den}  " ,end=" ")

        else:         
            sum = sum - value
            print(f"- 6^{den}",end =" ")
        den +=2
        # print(sum, value)
    return sum




print(pattern(6,4))