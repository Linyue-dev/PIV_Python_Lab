from typing import Iterable

r = range (1000)
db = ["sandy", "bob", "betle"]
z = zip(r,db)
x = dict(z)
y = tuple(x)

print('==================dict key=================')
for key in x:
    print(key)

print('==================tuple=================')
for t in y:
    print(t)

# ===============================================================
friends = ["rik", "sandy", "ian", "kelly"]
# primes = Primes()
friend_d = {}
friends = dict(zip(friends, friend_d))
# ===============================================================

# Grid((x1, y1),(x2, y2))
#
# grid1 = Grid ((1,8),4,10)
# grid2 = Grid((2,9),(5,12))
# point = set()

# for p in grid1:
#     point.add(p)
#
# for p in grid2:
#     point.add(p)

# set(grid1).union(set(grid2))
# set(list(grid1) + list(grid2))

# def evens_only(a: Iterable[int]) -> list[int]:
#     odd = list()
#     for i in a:

