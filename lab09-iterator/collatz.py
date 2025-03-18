class Collatz:
    # way1
    # def __init__(self, num):
    #     self.num = num
    #
    # def __iter__(self):
    #     return self
    # def __next__(self):
    #     if self.num == 1:  # StopIteration when reaching 1
    #         raise StopIteration
    #     if self.num % 2 == 0:
    #         self.num = self.num // 2
    #     else:
    #         self.num = 3 * self.num + 1
    #     return self.num

    # way2
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        self.stop_iteration = False
        return self
    def __next__(self):
        n = self.num
        if self.stop_iteration:  # StopIteration when reaching 1
            raise StopIteration
        if self.num % 2 == 0:
            self.num = int(self.num / 2)
        else:
            self.num = 3 * self.num + 1

        if n == 1:
            self.stop_iteration = True
        return n

# 1. iterable = iter(obj)
#     - this is the setup
#     - initialize the iterable
# 2. gets the next element, raise StopIteration

# sequence = Collatz(10)
# for num in sequence:
#     print(num)

c = Collatz(10)
l = list(c)
s = sum(c)
print(l)
print(s)