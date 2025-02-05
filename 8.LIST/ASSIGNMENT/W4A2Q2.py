# write a python code to generate a list of factorials less than 1000 using list comprehension

def factorials(number):
    result=1 
    if number==0 or number==1:
        return 1
    for i in range(2,number+1):
        result *= i
    return result 
factorial=[factorials(number) for number in range(500) if factorials(number) <1000]
print(factorial)
