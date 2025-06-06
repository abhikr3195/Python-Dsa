# Ask a string from user. Replace all the space characters with “-”. Do not
# use replace() method


def replace():
    user_input=input("enter the string sent: ")
    x=user_input.replace(" ", "-")
    return x
print(replace())

#without replcae method

def replaceSpaces(string):
    result = ""
    for char in string:
        if char == " ":
            result += "-"
        else:
            result += char
    return result


user_string = input("Enter a string: ")

r = replaceSpaces(user_string)

print(r)