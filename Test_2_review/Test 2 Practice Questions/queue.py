# # Stacks and queues
# ```python
# class Queue:
#     def put(self, v): ...
#     def front(self): ...
#     def get(self): ...
#
# class Stack:
#     def push(self, v): ...
#     def top(self): ...
#     def pop(self): ...
# ```
#
# ## Reverse
#
# Code a function that reverses the contents of a queue.
#
# **Requirement**: use a stack and no lists. The input queue should contain the reversed elements at the end of the function.
#
# ``` python
# def reverse(queue: Queue):
# ```

class Queue:
    def put(self, v): ...
    def front(self): ...
    def get(self): ...
    def is_empty(self): ...

class Stack:
    def push(self, v): ...
    def top(self): ...
    def pop(self): ...
    def is_empty(self): ...


def reverse(queue: Queue):
    stack = Stack()
    while True:
        if queue.is_empty():
            break
        stack.push(queue.get())
    while True:
        if stack.is_empty():
            break
        queue.put(stack.pop())
    return queue

