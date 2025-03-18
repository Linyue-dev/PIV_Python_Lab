from typing import Iterable

class Enumerate:

    def __init__(self, obj: Iterable):
        self.obj = iter(obj)
        self.index = 0
        pass

    def __iter__(self):
        return self

    def __next__(self):
        try:
            value = next(self.obj)

        except StopIteration:
            raise StopIteration

        t = (self.index, value)
        self.index += 1
        return  t
a = (1,2,3)
b=(4,5,6,7,8)

result = Enumerate(a)
for value in result:
    print(value)