# Write a Python code to check if a list is a palindrome (reads the same
# forwards and backwards). Just print “YES” or “NO”

def palindrome(l):
    if l == l[::-1]:
        print("yes")
    else:
        print("No")
l=[1,2,3,3,2,1]
print(palindrome(l))