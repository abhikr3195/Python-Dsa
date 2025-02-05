a=[1,2,3,4,5,6,7,8,9]
result=a[::2]
result1=a[::-1]  # for reverse
result2=a[-2:-4:-2] 
result3=a[-2:-4:2]
result4=a[-5::2] 
result5=a[-3:]#print the last 3 elements of the lsit
print(result)
print(result1)
print(result2)
print(result3)  # this will not print since this will go from L to R
print(result4)
print(result5)

#note -- if the step is +ve then L to R
       # if the step is ive then R to L