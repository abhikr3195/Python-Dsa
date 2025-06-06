# Create a python function named isPalindrome which accepts a string
# as a parameter and return True if its a palindrome. Palindrome are words
# which is same when read from start and same when read from the end



def isPalindrome(user_input):
    if len(user_input)== user_input[::-1]:
        return True
    return False
user_input=input("enter the string: ")
print(isPalindrome(user_input))
