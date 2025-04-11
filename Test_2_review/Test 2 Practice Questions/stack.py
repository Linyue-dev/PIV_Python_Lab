
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
