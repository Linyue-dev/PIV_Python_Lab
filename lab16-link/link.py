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



