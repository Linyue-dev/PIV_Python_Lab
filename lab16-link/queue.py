from typing import TypeVar, Generic

T = TypeVar("T")

class Link(Generic[T]):
    def __init__(self, element=None):
        self.element = element
        self.next = None
class QueueList:
    def __init__(self):
        self.front: Link = None

    def put(self, x: any):
        new_element = Link(x)
        if self.front is None:
            self.front = new_element
        else:
            end_ele = self.front
            while end_ele.next is not None:
                end_ele = end_ele.next
            end_ele.next = new_element

q = QueueList()
q.put(1)
q.put(4)
q.put(6)

print("queue list -> ")
ele = q.front
while ele:
    print(ele.element)
    ele = ele.next

