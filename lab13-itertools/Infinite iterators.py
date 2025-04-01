"""
count()
cycle()
repeat()
"""
from itertools import cycle
people = ["hello", "Cat", "Pichur"]
group = ["A", "B", "C"]
for g, p in zip(cycle(group), people):
    print(g, p)