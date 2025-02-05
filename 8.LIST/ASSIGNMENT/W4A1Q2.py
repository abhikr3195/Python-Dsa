# make your own list of numbers. ask a start and end position from user.
#make another different list which will contain number from start to end position .use slicing logic


a=[1,2,3,4,5,6,6,7]
b=[]
start_pos=int(input("enter the start position: "))
end_pos=int(input("enter the end postion: "))

print(a[start_pos:end_pos+1:-1])