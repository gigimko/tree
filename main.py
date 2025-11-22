class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
    
    def add(self, child_node):
        self.children.append(child_node)
    
    def display(self, level):
      
        indent = "  " * level
        print(indent + '|_' + str(self.data))
        for child in self.children:
            child.display(level + 1)



electronics = Node('electronics')

tvsNode = Node("TVs")
tvsNode.add(Node("sony"))

electronics.add(tvsNode)
electronics.add(Node('Test'))
electronics.display(0)
