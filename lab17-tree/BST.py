from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    value: any
    # left: Optional["Node"]
    # right: Optional["Node"]
    left: Optional["Node"] = None
    right: Optional["Node"] = None

class BST:
    head: Optional["Node"]
    current: Optional["Node"]


def add(Node, value):
    if not Node.value == value:
        return
    if value > Node.value:
        # return add(Node.right, value)
        if Node.right is None:
            Node.right = Node(value)
        else:
            add(Node.right, value)


