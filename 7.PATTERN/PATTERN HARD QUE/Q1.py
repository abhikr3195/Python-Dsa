#      1
#     21
#    321
#   4321 
#  54321 
for i in range(5,0,-1):
    for k in range(1,i):
        print("",end=" ")
    for j in range(5,i-1,-1):
        print(j, end="")  
    print()  