# Q6. Create a function sumCountOddEven that accepts an List of Integers
# and calculate sum of even and odd numbers.


def countOddEven(my_list):
    totalEven=0
    totalOdd=0
    for i in range(len(my_list)):
        if my_list[i]%2==0:
            totalEven+=my_list[i]
        else:
            totalOdd+=my_list[i]
    return totalEven,totalOdd
    # print()
my_list=[12,44,32,55,88,76,13]
print(countOddEven(my_list))