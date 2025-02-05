# 1  1/2  1/3  1/4   1/5   and their sum


num=int(input("enter the number:"))
total=1
print(total, end=" ")
for i in range(2,num+1):
    print(f"1/{i}", end=" ")
    total=total+1/i
    print()
print(total)