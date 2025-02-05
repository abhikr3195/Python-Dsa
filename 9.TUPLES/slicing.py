from typing import Tuple

tup:Tuple=(32,45,-100,67,77,43)
print(tup[1:3]) #o/p (45, -100)
print(tup[::-1]) #o/p (43, 77, 67, -100, 45, 32)

#tuples can be added
print(tup[-3:]+tup[:3]) # o/p (67, 77, 43, 32, 45, -100)