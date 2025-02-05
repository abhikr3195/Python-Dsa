#write a python program to generate a list of powers 2 less than 100 using list comprehension



def Power(number):
    return[2**i for i in range(0,number) if 2**i < 100]
x=Power(8)

print(x)