# Ask 5 integers from user. Then ask a single character from user. Print
# those integers separated by that character entered by user.

def character(user_input):
    nums = []
    for i in range(5):
        num=int(input("enter the number: "))
        nums.append(num)
    return f"{user_input}".join(map(str,nums))
user_input=input("enter the character: ")
print(character(user_input))