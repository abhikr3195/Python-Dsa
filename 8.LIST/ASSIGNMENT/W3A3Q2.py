# . Make a list of your own. Print all the numbers divisible by 3 and 4 in
# that list.

a=[12,34,45,24,8,9,100,99]
for i in range(0,len(a)):
    # print(i)
    if a[i]%3==0 and a[i]%4==0:
        print(a[i], end=" ")