#count the capital 
a="Python is A greaT LangUage"
count=0
for char in a:
    ascii_number=ord(char)
    if ascii_number>=65 and ascii_number<=90:
        count+=1
print(count)

#count how many digits are there

c="Pytho2n i4s A1 gr4eaT La2ngUa6ge"
count=0
for char in c:
    ascii_number=ord(char)
    if ascii_number>=48 and ascii_number<=57:
        count+=1
print(count)

#count how many digits are there

b="Pytho2n i4s A1 g3r4eaT La2ng5Ua6ge"
cnt=0
for char in b:
    ascii_num=ord(char)
    if 48<=ascii_num<=57:
        cnt+=1
print(cnt)

