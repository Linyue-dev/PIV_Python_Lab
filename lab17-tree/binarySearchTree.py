from binaryTree import Node

# ===========way1================
# def contains(self, target) :
#     if self is None:
#         return False
#     if target == self.value:
#         return True
#     elif target < self.value:
#         return target in self.left
#     else:
#         return target in self.right
# ===========way2================
def contains(self, target):
    if target == self.value:
        return True
    elif target < self.value:
        return self.left.contains(target) if self.left else False
    else:
        return self.right.contains(target) if self.right else False
# ===========way3================
# def contains(self, target) -> bool:
#     # Check if the current node's value matches the target
#     if self.value == target:
#         return True
#     # Recursively check left and right children
#     left_contains = self.left.contains(target) if self.left else False
#     right_contains = self.right.contains(target) if self.right else False
#     return left_contains or right_contains


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print(root.contains(3))  # True
print(root.contains(5))  # False
