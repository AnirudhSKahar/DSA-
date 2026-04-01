class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
# creating the nodes
node1=Tree(10)
node2=Tree(20)
node3=Tree(30)
node4=Tree(40)
node5=Tree(50)
node6=Tree(60)
node7=Tree(70)

# connecting the nodes
node1.left=node2
node1.right=node3
node2.left=node4
node2.right=node5
node3.left=node6
node3.right=node7
