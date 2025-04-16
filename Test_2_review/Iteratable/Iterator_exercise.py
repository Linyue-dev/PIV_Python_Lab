# 1. Custom Iterator: CountUpTo
# Write a class CountUpTo that counts from 1 up to a max number.
# Practice: Try for num in CountUpTo(5): print(num)
class CountUpTo:

    def __init__(self, max):
        self.max = max
        self.current_value = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_value > self.max:
            raise StopIteration
        next_value = self.current_value
        self.current_value += 1
        return next_value

countUpTo = CountUpTo(6)
print(list(countUpTo))

for i in countUpTo:
    print(i)

# 2. Custom Iterator that wraps another iterable
# Make a class UppercaseIterator that takes an iterable of strings and returns each string uppercased.
class UppercaseIterator:

    def __init__(self, data: str):
        self.data = data
        self.count = 0

    def __iter__(self):
        self.data = iter(self.data)
        return self.data

    def __next__(self):
        self.count += 1
        return self.data[self.count].upper()

# class UppercaseIterator:
#     def __init__(self, iterable):
#         if isinstance(iterable, str):
#             self.iterator = iter(iterable.split())  # or just iter(iterable) for letters
#         else:
#             self.iterator = iter(iterable)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         return next(self.iterator).upper()


# class UppercaseIterator:
#     def __init__(self, iterable):
#         self.iterator = iter(iterable)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         return next(self.iterator).upper()


words = ["hello", "world", "python"]
for word in UppercaseIterator(words):
    print(word)