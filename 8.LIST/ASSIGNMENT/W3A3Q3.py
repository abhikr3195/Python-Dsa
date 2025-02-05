# Q3. Make a list of your own. Count how many numbers are divisible by 5.

a=[1,25,46,75,80,95,71]
count=0
for i in range(0,len(a)):
    if a[i]%5==0:
        count=count+1
print(count, end="")   

