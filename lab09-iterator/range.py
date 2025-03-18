class Range:
    def __init__(self, n):
        self.end = n
        self.count = 0

    def __iter__(self):
        # self.count = 0
        return self

    def __next__(self):
        t = self.count
        if self.count >= self.end:
            self.count += 1
        # if self.count >= self.end:
        #     raise StopIteration
        self.count += 1
        return t
# x= range(5)

x = Range(5)
# for i in x:
#     print(i)
# for j in x:
#     print(j)

for i in x:
    for j in x:
        print(i, j)