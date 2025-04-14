"""
## `Take`
Code the iterator `Take` that will produce the first `n` elements in a list.
If `n` is larger than the list, then the entire list is produced.
"""
from queue import Queue
from queue import Stack

class Take:
    def __init__(self,lst:list, n:int):
        self.n = n
        self.index = 0
        self.lst = lst

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.index or self.index >= len(self.lst):
            raise StopIteration
        value = self.lst[self.index]
        self.index += 1
        return value

l = list(Take([1,2,3,4,5,6,4],5))
print(l)

"""
## `TakeWhile`
Code the iterator `TakeWhile` that will produce the elements while a given
predicate is true.aq
"""

class TakeWhile:
    def __init__(self, predicate, lst:list):
        self.lst = lst
        self.count = 0
        self.predicate = predicate

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= len(self.lst):
            raise StopIteration
        value = self.lst[self.count]
        if self.predicate(value):
            self.count += 1
        else:
            raise StopIteration
        return value

for i in TakeWhile(lambda x: x%2 ==0,[2, 4, 6, 8, 9, 5, 2, 3]):
    print(i)

print("=========================================================================")
"""
## `find_with`
Code a higher-order function `find_with` that returns one element in the list for which the predicate is true, or `None` if not found.
For example,
"""

my_games = [
    (27, "Great game 1"),
    (20, "Average game 1"),
    (10, "Bad game 1"),
    (12, "Bad game 2"),
    (7,  "Terrible game"),
    (25, "Average game 2"),
    (49, "Best game ever")
]

def good_game(g):
    return g[0] >= 25

def find_with(predicate, lst:list):
    new_list =[]
    for item in lst:
        if predicate(item):
            new_list.append(item)
    return new_list

print(find_with(good_game, my_games))
print("=========================================================================")
"""
# Increasing
You have a sequence of numbers stored in a queue. Code a function that
replaces the queue with only the values that *increase*. For example, if
the queue has `~FRONT -> 3, 2, 5, 4, 3, 6, 5, 7 <- BACK` then the
increasing values would be `3, 5, 6, 7`. Requirement: use stacks and no
lists.
"""
class Queue:
    def __init__(self):
        self.items = []

    def put(self, v):
        self.items.append(v)  # 放在末尾

    def get(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items.pop(0)  # 从前面拿

    def front(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

class Stack:
    def __init__(self):
        self.items = []

    def push(self, v):
        self.items.append(v)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

def increasing(queue: Queue) -> Queue:
    stack1 = Stack()
    stack2 = Stack()
    last_value = None

    while not queue.is_empty():
        value = queue.get()
        if last_value is None or value > last_value:
            stack1.push(value)
            last_value = value

    while not stack1.is_empty():
        stack2.push(stack1.pop())

    while not stack2.is_empty():
        queue.put(stack2.pop())
    return queue

# test：
l = [3, 2, 5, 4, 3, 6, 5, 7]
q = Queue()
for num in l:
    q.put(num)

q = increasing(q)
while not q.is_empty():
    print(q.get(), end=' ')  # output 3 5 6 7

print("\n=========================================================================")
"""
# Code an iterator `Tails` that produces one by one consecutively smaller lists: first the entire
list, then the list without the first element, then the list without the
second element, until the empty list (included in tails). The original
list should not be modified.
"""

class Tails:
    def __init__(self, lst:list):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
       if self.index > len(self.lst):
           raise StopIteration
       result = self.lst[self.index:]
       self.index += 1
       return result
l = [1, 2, 3]

for tail in Tails([1, 2, 3]):
    print(tail)
# 输出：
# [1, 2, 3]
# [2, 3]
# [3]
# []

print("\n=========================================================================")

"""
# Code an iterator `Nub` that takes an list and produces only unique values, i.e.: no duplicates.

    ["aaa", "bbb", "aaa", "zzz", "bbb", "zzz"]

would produce: "aaa", "bbb", "zzz"
"""

class Nub:
    def __init__(self, lst:list):
        self.seen = []
        self.lst = iter(lst)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            item = next(self.lst)  # 使用初始化好的迭代器
            if item not in self.seen:
                self.seen.append(item)
                return item

l = ["aaa", "bbb", "aaa", "zzz", "bbb", "zzz"]

print(list(Nub(l)))

print("\n=========================================================================")

"""
# Code a higher-order function `drop_while` that will return a list without the beginning 
elements for which the predicate function (`pred`) returns `True`.
"""

def drop_while(pred, lst:list) -> list:
    b = []
    for item in lst:
        if pred(item):
            b.append(item)
    return b

def pred(x):
    return x < 3
a = [1, 2, 3, 4]
print(drop_while(pred,a))

print("\n=========================================================================")

"""
# Code a higher-order function `partition` that returns a tuple of lists, the 
first are the elements that the predicate function (`pred`) return True, the 
second are the ones returning False.

"""

def partition(pred, lst: list) ->tuple:
    list1 = []
    list2 = []
    for item in lst:
        if pred(item):
            list1.append(item)
        else:
            list2.append(item)
    return list1, list2

print(partition(pred,a))