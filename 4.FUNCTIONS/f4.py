#MAKE A FUNCTION WITH checkOddEven which takes integr as a arguement
# if even print EVEN,else print ODD

def checkOddEven(num1:int):
    if num1%2==0:
        print(f"{num1} is EVEN")
    else:
        print(f"{num1} is ODD")
        
checkOddEven(4)  
checkOddEven(5)          
checkOddEven(17)
    