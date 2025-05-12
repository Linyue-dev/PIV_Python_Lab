from typing import Optional, TypeVar, Callable

from sphinx.addnodes import index


class Link[T]:
    def __init__(self, element: T):
        self.element: T = element
        self.next: Optional[Link[T]] = None

"""
Links I. With single-links:
Code a function print_nth(head: Optional[Link[T]], n: int) that prints every n-th value in
the link chain, starting with the element at head.
"""
T = TypeVar("T")
def print_nth(head: Optional[Link[T]], n: int) -> None:
    """
    Prints every n-th element in the linked list starting from head.

    Args:
        head: The head of the linked list (or None if empty).
        n: The step size for selecting elements to print (n > 0).
    """
    if n <= 0:
        return

    current = head
    index = 1

    while current is not None:
        if index % n == 0:
            print(current.element)
        current = current.next
        index += 1

head = Link(1)
head.next = Link(2)
head.next.next = Link(3)
head.next.next.next = Link(4)
head.next.next.next.next = Link(5)
print("==================Links I. With single-links: ==========================")
# Print every 2nd value (should print 2, 4)
print("Every 2nd value:")
print_nth(head, 2)

# Print every 3rd value (should print 3)
print("Every 3rd value:")
print_nth(head, 3)



print("==================Links II ==========================")
"""
Again with double-links: Code a LinkedList method remove_with(self, pred: Callable[[T],
bool]) that removes all links where the pred function is true.
"""
class DoubleLink[T]:
    def __init__(self, element: T):
        self.element: T = element
        self.next: Optional[DoubleLink[T]] = None
        self.prev: Optional[DoubleLink[T]] = None


class LinkedList[T]:
    def __init__(self):
        self.head: Optional[Link[T]] = None
        self.tail: Optional[Link[T]] = None  # Added for doubly linked list

    def append(self, element: T) -> None:
        """Append an element to the end of the list."""
        new_link = Link(element)
        if self.head is None:
            self.head = new_link
            self.tail = new_link
        else:
            new_link.prev = self.tail
            self.tail.next = new_link
            self.tail = new_link

    def remove_with(self, pred: Callable[[T], bool]) -> None:
        """
        Removes all links where pred(element) is True.

        Args:
            pred: A function that takes an element of type T and returns True if the link should be removed.
        """
        current = self.head
        while current is not None:
            next_node = current.next  # Save next node before potential removal
            if pred(current.element):
                # Remove current link
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next  # Update head if removing first node

                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev  # Update tail if removing last node
            current = next_node

        # If head is None after removals, ensure tail is also None
        if self.head is None:
            self.tail = None

    def __str__(self) -> str:
        """Return a string representation of the list."""
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.element))
            current = current.next
        return " <-> ".join(elements)

lst = LinkedList[int]()
for i in range(1, 6):
    lst.append(i)

print("Original list:", lst)

# Remove all even elements
lst.remove_with(lambda x: x % 2 == 0)
print("After removing evens:", lst)

# Remove elements greater than 3
lst.remove_with(lambda x: x > 3)
print("After removing > 3:", lst)

print("==================Links III. With double-links:==========================")
"""
Code a function make_circular(current: DoubleLink[T]) that makes the double-linked chain
“circular”, that is, the first and last link in the chain are connected. Note: current can be anywhere
in the chain when the function is called.
"""

def make_circular(current: DoubleLink[T]):
    if current is None:
        return

    # Find the first node (head) by following prev pointers
    head = current
    while head.prev is not None:
        head = head.prev

    # Find the last node (tail) by following next pointers
    tail = current
    while tail.next is not None:
        tail = tail.next

    # Make the list circular
    tail.next = head  # Last node points to first node
    head.prev = tail  # First node points back to last node

# Create a doubly linked list: 1 <-> 2 <-> 3
link1 = DoubleLink(1)
link2 = DoubleLink(2)
link3 = DoubleLink(3)

# Set up links
link1.next = link2
link2.prev = link1
link2.next = link3
link3.prev = link2

# Print list before making circular
print("Before making circular:")
curr = link1
for _ in range(4):  # Limit to avoid infinite loop in circular list
    print(curr.element, end=" <-> ")
    curr = curr.next if curr.next is not None else link1
print("...")

# Make the list circular starting from link2
make_circular(link2)

# Print list after making circular
print("After making circular (limited to 6 steps to avoid infinite loop):")
curr = link1
for _ in range(6):
    print(curr.element, end=" <-> ")
    curr = curr.next
print("...")

# Verify circularity
print("First node's prev points to last:", link1.prev.element)  # Should be 3
print("Last node's next points to first:", link3.next.element)  # Should be 1

