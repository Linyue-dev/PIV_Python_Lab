# In python every instance , class is an object
a = 3
id(a) # get memory location
# >>> b=3
# >>> id(b)
# 4326926720
# >>> a=b
# >>> id(a)
# 4326926720
# =================
# >>> a=[1,2,3,4,5]
# >>> id(a[2])
# 4326926720
# >>> id(3)
# 4326926720
# =================
# >>> b= [1,2,3,4,5]
# >>> id(b)
# 4308267840
# >>> b.append(6)
# >>> id(b)
# 4308267840
# =================
# >>> a= [None]*10
# >>>
# >>> print(a)
# [None, None, None, None, None, None, None, None, None, None]
# =================
# >>> a= [[]]*4
# >>> print(a)
# [[], [], [], []]

# variable is key, value is location of memory

# =================
# >>> a=[1,2,3,4,5]
# >>> b=a.reverse()
# >>> print(b)
# None
# >>> print(a)
# [5, 4, 3, 2, 1]
# >>> b=(reversed(a))
# >>> print(b)
# <list_reverseiterator object at 0x10088d780>
# >>> print(list(b))
# [1, 2, 3, 4, 5]
# >>>

class Foo():
    def __init__(self, l:list = None):
        l = l if l is not None else []
        self.l = l
    def add(self,v):
        self.l.append(v)


