# Q4. Write a Python Program to find sum and average of List in Python.
def sumAverage(my_list):
    total=0
    for i in range(0,len(my_list)):
        total+=my_list[i]
    print(f"Total={total}")


    ave=total/len(my_list)
    print(f"Average={ave}")

my_list=[1,2,3,4,5,6,7,8,9]
sumAverage(my_list)
