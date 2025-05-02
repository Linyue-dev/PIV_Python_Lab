from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

"""binary tree"""

@dataclass
class Node:
    value: any
    # left: Optional["Node"]
    # right: Optional["Node"]
    left: Optional["Node"] = None
    right: Optional["Node"] = None

    def __len__(self):
        if self is None:
            return 0
        # ===========way1================
        if self.left:
            left_len = len(self.left)
        else:
            left_len = 0
        if self.right:
            right_len = len(self.right)
        else:
            right_len = 0
        return left_len + right_len + 1

        # ===========way2================
        # return len(self.left) + len(self.right) + 1

    def height(self):
        # ===========way1================
        # left_height = self.left.height() if self.left else -1
        # right_height = self.right.height() if self.right else -1
        # return 1 + max(left_height, right_height)
        # ===========way2================
        if self is None:
            return 0
        left_height = self.left.height() + 1
        right_height = self.right.height() + 1
        return max(left_height, right_height)
    # ===========way1================
    def contains(self, target) :
        if self is None:
            return False
        if target == self.value:
            return True
        elif target < self.value:
            return target in self.left
        else:
            return target in self.right
    # ===========way2================
    # def contains(self, target):
    #     if target == self.value:
    #         return True
    #     elif target < self.value:
    #         return self.left.contains(target) if self.left else False
    #     else:
    #         return self.right.contains(target) if self.right else False
    # ===========way3================
    # def contains(self, target) -> bool:
    #     # Check if the current node's value matches the target
    #     if self.value == target:
    #         return True
    #     # Recursively check left and right children
    #     left_contains = self.left.contains(target) if self.left else False
    #     right_contains = self.right.contains(target) if self.right else False
    #     return left_contains or right_contains
    # Create tree nodes
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print("Total nodes in tree:", len(root))  # Output: 4

def display(node, level=0):
    if node:
        print("  " * level + str(node.value))
        display(node.left, level + 1)
        display(node.right, level + 1)

display(root)

# Test contains method
print(root.contains(3))  # Output: True
print(root.contains(5))  # Output: False