# Keep asking characters from user until he presses q on the keyboard.
# Change all the capital letters to small, and all the small letters to capital.
def toggle():
    result=""
    while True:
        char= input("enter the character: ")
        if char.lower() == "q":
            break
        elif char.islower():
            result += char.upper()
        elif char.isupper():
            result+= char.lower()
        else:
            result += char
    return result
print(toggle())