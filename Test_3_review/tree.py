from typing import Optional, TypeVar
class Node:
    def __init__(self, element):
        self.element = element
        self.next = None  # Link to the next node

print("==================Tree IV. Trees definitions.==========================")

"""
       5
      / \
     3   1
    / \ / \
   7  6 6  4
  / \
 9   2
What is/are:
i) the subtrees of 3.  -> 7 and 6
ii) the ancestors of 2. -> 7 , 3 and 5
iii) the parents of 6. 3 and 1
iv) the postorder traversal starting at the root.  Full postorder: 9, 2, 7, 6, 3, 6, 4, 1, 5
v) the path from 5 to 9.  5 -> 3 -> 7 -> 9
"""

print("==================Trees I. Here is a mysterious function:==========================")
"""
Describe what this function did to the tree? Do you think that’s what the author wanted to do?
before call function:
           77
          /  \
         66   88
        /  \    \
       21  86    86
      /  \
     10  54
    /
   39

after call function
 
       77
      /  \
     88   66
          /  \
         86   21
              /  \
             10   None
            /
           39
"""
def mystery(current: Node):
    if current is None:
        return
    mystery(current.left)
    tmp = current.left
    current.left = current.right
    current.right = tmp
    mystery(current.right)

def mirror(current: Node):
    if current is None:
        return
    # current.left, current.right = current.right, current.left
    tmp = current.left
    current.left = current.right
    current.right = tmp

    mirror(current.left)
    mirror(current.right)

print("==================Trees II. Trace this method of the TreeSet class:==========================")
"""
                   82
               /       \
              68        92
            /    \      / \
           16     78   91  95
          /  \   /    /     \
         15  30 69   89      98
        /   /  \
       9  28   60
      /   /    / \
     3   20   41  63
               \
                53
               /  \
              51   54



when it is called floor(35) on this tree:


Color the nodes whose elements are accessed by this function. What does this function return?
"""



T = TypeVar("T")
def floor(self, value: T) -> Optional[T]:
    return self._floor_h(self.root, value)

def _floor_h(self, current: Optional[Node[T]], value: T) -> Optional[T]:
    if current is None:
        return None
    if current.element == value:
        return value
    if value < current.element:
        return self._floor_h(current.left, value)
    else:
        tmp = self._floor_h(current.right, value)
        if tmp is None:
            return current.element
        else:
            return tmp

