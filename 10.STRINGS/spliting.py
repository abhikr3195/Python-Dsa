my_string= "python is great"

result=my_string.split()
print(result)
result=result[::-1]
s= "".join(i for i in result)
print(s)
print(result)