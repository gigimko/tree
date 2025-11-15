class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
    def add(self, data):
        self.children.append(data)
    def display(self):
        print(self.data)
        if self.children:
            for child in self.children:
                child.display()
        
            
            

electronics = Node('electronics')
tvsNode = Node("TVs")
tvsNode.add(Node("sony"))
electronics.add(tvsNode)

electronics.display()