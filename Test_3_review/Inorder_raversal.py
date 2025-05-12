# 1. What is Inorder Traversal?
# Inorder traversal is a depth-first traversal method for a binary tree where nodes are visited in the following order:
# Left subtree (recursively)
# Current node (root of the current subtree)
# Right subtree (recursively)
# For a Binary Search Tree (BST), this traversal yields the node values in ascending order because of the BST property: left subtree < current node < right subtree.

"""
What is the "Inorder Traversal" of a Binary Search Tree? What is its Special Property?
Reference Answer:
Inorder Traversal: Inorder traversal is a method of visiting the nodes of a binary tree in the following order: left subtree -> root node -> right subtree.
Special Property for Binary Search Trees (BST): For a binary search tree, the result of an inorder traversal is a sorted list of node values in ascending order.

     5
    / \
   3   7
  /     \
 1       9

visit order -> 1, 3, 5, 7, 9.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    result = []
    def inorder(node):
        if not node:
            return
        inorder(node.left)  # Traverse left subtree
        result.append(node.val)  # Visit current node
        inorder(node.right)  # Traverse right subtree

    inorder(root)

    # Verify if the result is in ascending order
    is_ascending = all(result[i] <= result[i + 1] for i in range(len(result) - 1))
    return result, is_ascending


# Test with the example BST
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
# root.right = TreeNode(2)
root.left.left = TreeNode(1)
root.right.right = TreeNode(9)

result, is_ascending = inorderTraversal(root)
print("Inorder Traversal Result:", result)  # Output: [1, 3, 5, 7, 9]
print("Is Ascending Order?", is_ascending)  # Output: True

# Test with the example BST
root = TreeNode(5)
root.left = TreeNode(3)
# root.right = TreeNode(7)
root.right = TreeNode(2)
root.left.left = TreeNode(1)
root.right.right = TreeNode(9)

print(inorderTraversal(root))  # Output: [1, 3, 5, 7, 9]

# =================

def inorder(node, result):
    if not node:
        return
    inorder(node.left, result)    # Traverse left subtree
    result.append(node.val)      # Visit current node
    inorder(node.right, result)   # Traverse right subtree

def inorderTraversal(root):
    result = []
    inorder(root, result)
    return result

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.right.right = TreeNode(9)
print(inorderTraversal(root))  # Output: [1, 3, 5, 7, 9]