# Write a function which accepts a String as a parameter and return the
# reversed words as a String.


def reverseString(user_input):
    result=user_input.split()
    result1= " ".join(result[::-1])
    return result1
user_input= str(input("enter the string: "))
x=reverseString(user_input)
print(x)

# Alternate method

# def reverseWords(string: str) -> str:
#     words = string.split()
#     words.reverse()
#     result = " ".join(i for i in words)
#     return result

#     # Shortcut
#     # return " ".join(i for i in reversed(string.split()))


# print(reverseWords("python is great"))