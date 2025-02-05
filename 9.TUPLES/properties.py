from typing import Tuple
tup:Tuple=(32,45,-100,67,77,43)


#access index
print(tup[0])
print(tup[-1])

#update index/value

tup[2]=10000
print(tup) #TypeError: 'tuple' object does not support item assignment