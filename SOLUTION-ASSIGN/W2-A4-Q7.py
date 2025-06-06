"""
Keep asking numbers from user until the user enters 0. 
Then display the average of all numbers.
"""

def average():
    total=0
    count=0
    while True:
        num = int(input("enter the number: "))
        if num == 0:
            break
        total += num
        count += 1
    print(f"the average of the numbers is : {total/count}")
    return average
print(average())

        