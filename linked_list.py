class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create nodes
node1 = Node(15)
node2 = Node(3)
node3 = Node(17)
node4 = Node(90)

# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4  

# head = node1  # Head points to the first node

# # Traverse and print the linked list
# current = head
# while current:
#     print(current.data, end=" -> ")
#     current = current.next
# print("None")

# # deletion of linked list
# current = head
# while current.next.next is not None:
#     current = current.next
# current.next = None  # Remove reference to the last node

# to delete any node with specific value

# head = node1
# # Reset head to the first node
# current = head
# while current.next.data != 17:
#     current = current.next
# current.next = current.next.next  # Bypass the node with data 17

# # Traverse and print the linked list after deletions
# current = head
# while current:
#     print(current.data, end=" -> ")
#     current = current.next
# print("None")

 