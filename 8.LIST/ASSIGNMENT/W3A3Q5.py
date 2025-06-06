# Q5. Create a function countOddEven that accepts an List of Integers and
# print how many even and odd numbers are there.

def countOddEven(my_list):
    countEven=0
    countOdd=0
    for i in range(len(my_list)):
        if my_list[i]%2==0:
            countEven+=1
        else:
            countOdd+=1
    return countEven,countOdd
    # print()
my_list=[12,44,32,55,88,76,13]
print(countOddEven(my_list))
