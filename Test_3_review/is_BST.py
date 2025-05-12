"""
Given the root node of a binary tree, determine whether it is a valid binary search tree.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def validate(node, min_val, max_val):
    """
    Validates if a binary tree is a valid BST.
    Args:
        node: TreeNode, the current node.
        min_val: float/int, the minimum allowed value for the node.
        max_val: float/int, the maximum allowed value for the node.
    Returns:
        bool: True if the subtree rooted at node is a valid BST, False otherwise.
    """
    if not node:
        return True
    if node.val <= min_val or node.val >= max_val:
        return False
    return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)

def isValidBST(root) -> bool:
    return validate(root, float("-inf"), float("inf"))


#============================================2=======================
"""
Given the root node of a binary search tree and a value, insert the value and return the new root node.
"""

def insertIntoBST(root, value):
    if not root:
        return TreeNode(value)
    if value < root.val:
        root.left = insertIntoBST(root.left, value)
    if value > root.val:
        root.right = insertIntoBST(root.right, value)

    return root
