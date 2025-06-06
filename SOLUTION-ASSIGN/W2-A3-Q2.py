"""
Create a function named calSum() which takes 2 integers n1 and n2 as
a argument. Calculate the sum of all the numbers from n1 and n2 and
RETURN THAT SUM. Also make sure that n1 is smaller than n2. If it is not,
then return “n1 should be smaller”.
"""

def calSum(n1,n2):
    if n1<n2:
        i=0
        sum=0
        while i<=n2:
            sum = sum + i
            i+=1 
        return sum 
    else:
        print("n1 should be smaller n2")   
print(calSum(20,10))   
       
            