"""
int -> bool
Truthy -> 1 2 3 -5
Falsy -> 0"""

abc=bool(3)
print(abc)
xyz=bool(0)
print(xyz)

"""
float -> bool
Truthy -> 1.36 2.324 3.2211 -5.36
Falsy -> 0.0"""

lmn=bool(1.1)
print(lmn)
jkl=bool(0.0)
print(jkl)

"""str -> bool
Truthy -> "dwadaw" " " "." "dwa wda dawd aw"
Falsy -> ""
"""

c=bool("hey")
print(c)
b = bool("")
print(b)

