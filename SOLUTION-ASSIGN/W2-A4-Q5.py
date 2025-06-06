def pattern(n1):
    i=0
    result = 1
    while i < n1:
        result = 2**i
        print(result,end=" ")
        i += 1
    return result    
pattern(4)
pattern(7)