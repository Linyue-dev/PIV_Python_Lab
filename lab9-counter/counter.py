class Counter:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start
        # l: list[for i in range(self.start, self.end)]

    def __next__(self):
        # print("next was called")
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

    # make sure object can be iteration
    def __iter__(self):
        self.current = self.start
        # print("iter was called")
        return self


def print_next():
    pass
# c = Counter(1,100)
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))

# for i in c: -> TypeError: 'Counter' object is not iterable
# for i in c:
#     print(i)
#     if i == 10:
#         break
# print("2nd loop")
# for i in c:
#     print(i)

def prime_number(start, end):
    c = Counter(start, end)
    count = 0
    for i in c:
        if i != start and i != end:
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
                count += 1
                print(i)
    return count

count = prime_number(1,100)
print(f"prime number count is {count} between 1 and 100")

# def prime_number(start, end):
#     c = Counter(start, end)
#     count = 0
#     for i in c:
#         l:list = []
#         l.append(i)
#         if i != start and i != end:
#             if i % 2 == 0 or i % 3 == 0:
#                 l.pop(i)
#                 count += 1
#                 print(i)
#     return count