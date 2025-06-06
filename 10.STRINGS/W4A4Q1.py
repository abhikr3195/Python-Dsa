# Q1. Ask a string from user. If the length of string is odd, then change all the
# capital letters to small and vice versa, but if the length of string is even,
# reverse the string. Do this using a function and return the output


def odd_even(string):
    if len(string)%2==0:
        return string[::-1]
    else:
        return string.swapcase()
user_input=input("enter the string: ")
result=odd_even(user_input)
print(result)