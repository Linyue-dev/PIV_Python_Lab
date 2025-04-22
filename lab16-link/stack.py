from link import Link
"""
use 'Link' class to create a stack
"""
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










