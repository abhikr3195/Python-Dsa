# def highest_odd_number(num):
#     # current_num=""
#     highest_odd=""
#     for digit in num:
#         current_num += digit
#         if int(digit)%2!=0:
#             if int(current_num) >= int(digit):
#                 highest_odd = current_num
#         else:
#             current_num=""
#     return highest_odd

#     # for i in range(len(num)-1, 0, -1):
#     #     if num[i]%2!=0:
#     #         return num[0:i]
#     # return -1
# num = "61632826"
# print(highest_odd_number(num))

def reverse_string(s):
    left, right = 0, len(s) - 1
    result = ""
    
    # Loop over the string and swap characters using two pointers
    for i in range(len(s)):
        if left < right:
            result = s[right] + result  # Add character at 'right' to the result string
            right -= 1
        else:
            break
    
    return result

# Test the function
s = "sanyam"
reversed_s = reverse_string(s)
print(reversed_s)
