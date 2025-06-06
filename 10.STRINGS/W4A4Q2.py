

def words_list(user_input):
    result = user_input.split(' ') 
    return result
    
user_input=input("enter the statement: ")
hola=words_list(user_input)
print(hola)
    
