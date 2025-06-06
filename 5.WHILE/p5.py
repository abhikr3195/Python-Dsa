# 1 3 6 8 11 13 16 18 21 23...upto N numbers
    
# i    = 0, 1, 2, 
# diff = 1, 2, 1     

def pattern(n):
    i = 0
    num = 1
    while i<=n:
        print(num)
        if i%2 == 0:
            num=num+2
        else:
            num=num+3
        i=i+1

            
pattern(10)