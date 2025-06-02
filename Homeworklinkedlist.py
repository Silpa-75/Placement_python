
class Node:
    def __init__(self, data):  # Corrected __init__
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):  # Corrected __init__
        self.head = None

    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_at_position(self, position, data):
        if position == 0:
            self.insert_at_begin(data)
            return
        new_node = Node(data)
        current = self.head
        for i in range(position - 1):
            if current is None:
                raise IndexError("Position out of bounds")
            current = current.next
        if current is None:
            raise IndexError("Position out of bounds")
        new_node.next = current.next
        current.next = new_node

    def print_list(self):  # Added method
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Test the corrected code
llist = LinkedList()
llist.insert_at_end('10')
llist.insert_at_end('20')
llist.insert_at_begin('30')
llist.insert_at_end('40')
llist.insert_at_position(2, '80')

print("Initial list:")
llist.print_list()
