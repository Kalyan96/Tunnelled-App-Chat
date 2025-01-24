
from enum import Enum

# d=[1,2,3,4,5]
st = ['a','b','c','d','e','e']
d = {}
for x,y in enumerate(st):
    try:
        if d[y] != "":
            d[y]+=(" "+str(x))
    except :
        d[y]=str(x)

# for i in d.values()
print(  d )

# en = enumerate(st)
# print(en[0])