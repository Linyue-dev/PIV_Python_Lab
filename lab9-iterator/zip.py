class Zip:

    """
    If obj is an iterable (like a list, tuple, set, string,
    or any class implementing __iter__()), iter(obj) returns an iterator
    that can be used to iterate over its elements one by one.
    """
    def __init__(self, obj1, obj2, longest=False,default=None):
        self.obj1 = iter(obj1)
        self.obj2 = iter(obj2)
        self.default = default

    def __iter__(self):
        return self

    def __next__(self):
        stop1 = False
        stop2 = False

        try:
            value1 = next(self.obj1)
        except StopIteration:
            value1 = self.default
            stop1 = True

        try:
            value2 = next(self.obj2)
        except StopIteration:
            value2 = self.default
            stop2 = True

        if stop1 and stop2:
            raise StopIteration
        return value1, value2

a = (1,2,3)
b=(4,5,6,7,8)

zip_num = Zip(a,b)
for i in zip_num:
    print(i)

