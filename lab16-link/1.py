from typing import TypeVar, Generic
T = TypeVar("T")

class Link(Generic[T]):
    def __init__(self, element=None):
        self.element = element
        self.next = None


head = Link()
head.element = 1
head.next = Link()
head.next.element = 2
head.next.next = Link()
head.next.next.element = 3
head.next.next.next = Link()
head.next.next.next.element = 4

print("print element ->")
new = head
while new is not None:
    print(new.element)
    new = new.next

# current = head
# while True:
#     if current.next != None:
#         print(current.element)
#         current = current.next

# ============================== make a linked list =================================
def make_chain(n):
    """make a linked list
       with elements o -> n-1
    """
    head = Link(0)
    current = head
    for i in range(1, n):
        current.next = Link(i)
        current = current.next
    return head

print("Link list ->")
chain = make_chain(5)

# Traverse and print
current = chain
while current is not None:
    print(current.element)
    current = current.next
def build(n):
    head = Link(0)
    current = head
    for i in range(1, n):
        current.next = Link(i)
        current = current.next
        print(current)
    return head

# =============================== use 'Link' class to create a stack==========================

class StackList:
    def __init__(self):
        self.head: Link = None

    def push(self, x: list):
        """Add x to top of stack"""
        for ele in x:
            new_element = Link(ele)
            new_element.next = self.head
            self.head = new_element

    # def push(self, x: any):
    #     """Add x to top of stack"""
    #     n = Link(x)
    #     n.next = self.head
    #     self.head = n

    def pop(self):
        if self.head is None:
            raise Exception
        value = self.head.element
        self.head = self.head.next
        return value
    # def pop(self):
    #     if self.head is None:
    #         raise Exception
    #     value = self.head
    #     self.head = self.head.next
    #     return value


l = [4, 5, 6, 7, 8, 9]
s = StackList()
s.push(l)
current = s.head
print("Stack list ->")
while current is not None:
    print(current.element)
    current = current.next

value = s.pop()
print("pop element ->", value)













