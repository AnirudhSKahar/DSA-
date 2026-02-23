# doubly linked list implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
# Create nodes
curr = Node(5)
node2 = Node(10)
node3 = Node(20)
# Link nodes
curr.next = node2  
node2.prev = curr
node2.next = node3
node3.prev = node2
# head = node1  # Head points to the first node
# Traverse and print the doubly linked list
current = curr

    