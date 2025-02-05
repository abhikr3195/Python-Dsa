# Create a function named sumOfSquares, which takes a single integer
# as a parameter named n. Return the sum of squares from 1 to n

def SumOfPatterns(num):
    total=0
    for i in range(1,num+1):
        total = total+(i**2)
    return total    
print(SumOfPatterns(5))
  
