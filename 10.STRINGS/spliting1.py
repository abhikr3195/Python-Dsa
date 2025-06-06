my_string= "python is great"

words= my_string.split()
print(words)

result= " ".join(str(i[::-1]) for i in words) # or result= " ".join((i[::-1]) for i in words)
print(result)

#mohtyp si taerg --output
