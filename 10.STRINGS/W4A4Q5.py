# Write a function which accepts a String as a parameter and return each
# word being in reverse.

# def rev_str(st):
#     left = 0
#     right = len(st)-1
#     while left<right:
#         st[left] , st[right] = st[right], st[left]
#         left+=1
#         right-=1
#     return ''.join(st)

# def rev_str_main(str1):
#     s=''
#     st1 = ''
#     for st in str1:
#         if st != ' ':
#             s+=st
#         elif st==' ' and s:
#             st1 = st1 + rev_str(list(s))+" "
#             s=''
#     return st1 + rev_str(list(s))

# print(rev_str_main("python is great "))

# def reverseString(user_input: str):
#     result= user_input.split()
#     print(result)
#     st1= ' '
#     for st in result:
#         st1= st1 +" "+ st[::-1]
#     print(st1)
#     #  reversed=  " ".join(result[::-1])
#     #  return reversed
# # user_input= str(input("enter a string: "))
# print(reverseString("python is great"))


def reverseString(user_input):
    result= user_input.split()
    reverdedi= " ".join(i[::-1] for i in result)
    return reverdedi
user_input=input("enter the string: ")
print(reverseString(user_input))
    