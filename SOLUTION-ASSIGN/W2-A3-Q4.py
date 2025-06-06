"""
Create a function named calSum which takes an 2 integer (n1 and n2)
as an argument. Calculate the sum of all the numbers divisible by 5
between n1 and n2 and return that sum. (Make sure that n1 is less than n2).


"""

def calSum(n1,n2):
    i = n1
    total=0
    while i <= n2:
        if i%5==0:
            total= total+i
        i+=1
    return total   
print(calSum(10,50))