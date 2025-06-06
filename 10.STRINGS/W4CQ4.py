# Ask a sentence from user. Then ask a integer k from user. Print all the
# words which are greater or equal to k

def removeWord():
    result=""
    sentence= input("enter the sentence: ")
    num=int(input("enter the number: "))
    lst= sentence.split()
    # print(lst)
    for i in range(len(lst)):
        if len(lst[i])>= num:
            result += lst[i] + " "
    return result.strip()
print(removeWord())