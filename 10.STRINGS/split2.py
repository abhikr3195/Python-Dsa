# output = cba zyx nml

a="abc xyz lmn"
words=a.split()
print(words)
print(" ".join(i[::-1] for i in words))