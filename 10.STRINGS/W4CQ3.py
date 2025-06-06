#remove duplicate from the string


def removeDup():
    result=""
    user_input=input("enter the string: ")
    for ch in user_input:
        if ch not in result:
            result += ch
    return result
print(removeDup())