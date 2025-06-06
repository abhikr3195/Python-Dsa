"""
Ask a string from user
And replace all the vowels with z

inp: aeroplane
out: zzrzplznz
"""

s = "aeroplane"
vowels = ["a", "e", "i", "o", "u"]
l=list(s)
for i in range(len(l)):
    if  l[i] in vowels:
        l[i]= "z"
# print(l)
result="".join(str(i) for i in l)
print(result)

string= input("enter the string: ")
vowels=["a","e","i","o","u"]
result1= " ".join(i if i not in vowels else "z" for i in string)
print(result1)

str1="aeroplane"
str2=""
for ch in str1:
    if ch in "aeiou":
        str2 += "z"
    else:
        str2 += ch
print(str2)
