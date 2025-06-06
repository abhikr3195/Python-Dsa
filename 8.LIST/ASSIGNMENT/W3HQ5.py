# Q5. Write a Python code to find the occurrence of each element in a list
# and print the element with the highest occurrence.

a=[1,2,3,4,4,4,5,5,5,1,1,2]
max_f = 0
ind_v = set()
for i in range(len(a)):
    count_max = 0
    for j in range(0,len(a)):
        if a[i]==a[j]:
            count_max+=1
    if count_max>=max_f:
        max_f = count_max
        ind_v.add(a[i])

print(ind_v)

# b=[]
# result=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b) 
       
# for i in b:
#     number=a.count(i)
#     result.append((number, i))
# result.sort(reverse=True)
# for count,number in result:
#     print(f"{number}:occurs {count} times")


# for value in a:
#     print(f"{value} occurs {a.count(value)}")

