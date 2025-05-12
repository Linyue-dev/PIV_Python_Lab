class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value, position):
        new_node = Node(value)

        # Insert at the beginning
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 0

        # Traverse to the position before where we want to insert
        while current is not None and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            print("Position out of bounds.")
            return

        # Insert new_node after 'current'
        new_node.next = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


# Create a linked list
ll = LinkedList()

# Insert some nodes
ll.insert(1, 0)  # List: 1
ll.insert(2, 1)  # List: 1 -> 2
ll.insert(3, 1)  # List: 1 -> 3 -> 2
ll.insert(0, 0)  # List: 0 -> 1 -> 3 -> 2
ll.insert(5, 5)  # Position out of bounds (list has 4 nodes, position=5 is invalid)

# Print the list
ll.print_list()