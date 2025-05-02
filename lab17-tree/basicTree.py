class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []  # List of child nodes

    def add_child(self, child_node):
        self.children.append(child_node)

    def display(self, level=0):
        print("  " * level + str(self.value))
        for child in self.children:
            child.display(level + 1)




# Create the tree
root = TreeNode("Root")

child1 = TreeNode("Child1")
child2 = TreeNode("Child2")

root.add_child(child1)
root.add_child(child2)

child1.add_child(TreeNode("Grandchild1"))
child2.add_child(TreeNode("Grandchild2"))
child2.add_child(TreeNode("Grandchild3"))

# Display the tree
root.display()
