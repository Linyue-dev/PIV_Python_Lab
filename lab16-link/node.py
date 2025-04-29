class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Link to the next node

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If list is empty
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the end
                current = current.next
            current.next = new_node  # Link the last node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()
