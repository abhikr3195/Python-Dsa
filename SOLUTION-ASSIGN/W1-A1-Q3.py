"""
Ask 3 numbers from user and calculate the average
"""

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
num3 = int(input("Enter number 3 : "))

average = (num1 + num2 + num3) / 3

print(f"Average : {average}")
print(f"Average : {average:.2f}")  # To display output upto 2 decimals only