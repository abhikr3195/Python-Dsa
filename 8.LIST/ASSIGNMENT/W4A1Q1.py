#make your own list of numbers.
# ask a start and end position from user.
# print the list from start position to end position using withoiut using slicing

a=[1,2,3,4,5,6,6,7]
b=[]
start_pos=int(input("enter the start position: "))
end_pos=int(input("enter the end postion: "))

print(a[start_pos:end_pos+1])
# for i in range(start_pos,end_pos):
#     b.append(a[i])
# print(b)
    