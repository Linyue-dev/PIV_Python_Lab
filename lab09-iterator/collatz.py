class Collatz:
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return self
    def __next__(self):
        if self.num == 1:  # StopIteration when reaching 1
            raise StopIteration
        if self.num % 2 == 0:
            self.num = self.num // 2
        else:
            self.num = 3 * self.num + 1
        return self.num


sequence = Collatz(29)
for num in range(10):
    print(num)
