# Q7. Write a Python code to find the second largest element in a list without
# sorting.

a=[1,2,3,7,5,7,9,9,19,9]
max1 = float('-inf')
max2 = float('-inf')

for i in range(0, len(a)):
    if max1 < a[i]:
        max2 = max1
        max1 = a[i]
    elif max1 > a[i] > max2:
        max2 = a[i]
    
    # print(max1, max2)

print(max1,max2)


    

# second_max=

