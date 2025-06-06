# replace every i in string with z and print the new string


def replaceChar(string: str):
    new_string: str=""
    for char in string:
        if char.lower=="i":
            new_string+="z"
        else:
            new_string += char
    return new_string
string="delhi is a great city"
x=replaceChar(string)


#alternate way using .replace method
a="delhi is a great city"
print(a.replace("i","z"))


#alternate method using .join

val_string: str= "delhi is great city"
lst=list(val_string)
print(lst)
r=(ch if ch != "i" else "z" for ch in lst)
print(r)