# number= input("enter the number: ")
# i = 0
# total =0
# while i < len(number):
#     total = total + int(number[i])
#     i+=1
# print(total)


#Alternate Method

num = int(input("enter the number:"))
total= 0
while num > 0:
    last_digit=num%10
    total= total+last_digit
    num = num // 10
print(total)
    
