# doubly linked list implementation in python   
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
head = Node(5)
ele2 = Node(10)
ele3 = Node(15)
head.next = ele2
ele2.prev = head    
ele2.next = ele3
ele3.prev = ele2
# traversing the list
current = head
while current is not None:
    print(current.data )
    current = current.next
print(" after insertion at the beginning")
  
# insertion at the beginning
new_node = Node(3)
new_node.next = head
head.prev = new_node
head = new_node

# after insertion at the beginning
current = head
while current is not None:
    print(current.data)
    current = current.next
    
# insertion at the end
print(" after insertion at the end")    
new_node2 = Node(20)
current = head
while current.next is not None:
    current = current.next
current.next = new_node2
new_node2.prev = current
# after insertion at the end
current = head
while current is not None:
    print(current.data)
    current = current.next
    
# # deletion at the beginning
# print(" after deletion at the beginning")   
# current = head
# head = head.next
# head.prev = None
# # after deletion at the beginning    
# current = head
# while current is not None:
#     print(current.data)
#     current = current.next

# deletion at the end
# print(" after deletion at the end") 
# current = head
# while current.next is not None:
#     current = current.next
# current.prev.next = None
    
# # after deletion at the end
# current = head
# while current is not None:
#     print(current.data)
#     current = current.next
# deletion at a specific position
print(" after deletion at a specific position")
pos=3
count=1
current = head
while current is not None:
    if count == pos:
        current.prev.next = current.next
        if current.next is not None:
            current.next.prev = current.prev
        break
    count += 1
    current = current.next
# after deletion at a specific position
current = head
while current is not None:
    print(current.data)
    current = current.next
