def display(lst):
    lst[0]=100
    print(id(lst))
    print(lst)
a=[12,23,45,67,89]
# print
print(id(a))
print(display(a))